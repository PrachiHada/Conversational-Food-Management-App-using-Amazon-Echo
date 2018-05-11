from pymongo import MongoClient
from bson.objectid import ObjectId
from collections import defaultdict
from collections import OrderedDict
from operator import itemgetter
import sys
from datetime import datetime

client = MongoClient()  #client = MongoClient(MONGODB_URI, connectTimeoutMS=30000)
db = client["consumit"] #db = client.get_default_database()


def get_record(user_id):
    collection = db['food_items']
    # ip = userid
    print('getting record of user: {}'.format(user_id))
    # user_id = ObjectId(ip)
    cursor = collection.find({"user_id": ObjectId(user_id)})
    return cursor


def analyze_record(record):
    """
    categorize record into 'percentage wasted', 'most consumed', 'most wasted'
    :param record:
    :return: a dictionary
    """
    perc_list = []
    shop_list = []
    inventory = []
    consumed_dict = defaultdict(list)
    wasted_dict = defaultdict(list)

    today = datetime.now().date()
    today = datetime(today.year, today.month, today.day)

    for document in record:
        pur_quant = _get_purchase_quantity(document)
        cur_quant = document['quantity']
        # consumed meaning not expired
        if _is_consumed(document):
            # Since for consumed, waste final quantity is zero - therefore 0%
            perc_list.append(0)
            shop_list.append(document['name'])
            consumed_dict[document['name']].append(pur_quant)
        elif _is_expired(document):
            # percentage food wasted since document['quantity']) = final quantity left
            perc = 0
            if pur_quant != 0:
                perc = cur_quant/pur_quant
                if perc < 0.4:
                    shop_list.append(document['name'])
            perc_list.append(perc)
            wasted_dict[document['name']].append(cur_quant)

        if document['exp_date'] >= today and cur_quant != 0:
            inventory.append(document['name'])

    # return a dictionary for the ease of understanding
    return {'percentage wasted': percentage_food_wasted(perc_list),
            'most consumed': most_consumed(consumed_dict),
            'most wasted': most_wasted(wasted_dict),
            'suggestive_shopping_list': suggestive_shopping_list(shop_list, inventory)}


def _is_consumed(doc):
    """
    helper function return if the item is consumed or not
    :param doc: document representing the food item
    :return: boolean
    """
    return doc['is_consumed'] is True


def _is_expired(doc):
    """
    helper function return if the item is expired or not
    :param doc: document representing the food item
    :return: boolean
    """
    today = datetime.now().date()
    today = datetime(today.year, today.month, today.day)
    return doc['exp_date'] < today


def _get_purchase_quantity(doc):
    """
    helper function to get the initial quantity when the item was input/purchased
    :param doc: document representing the food item
    :return: number
    """
    return doc['consumption'][0]['quantity']


def percentage_food_wasted(perc_list):
    """
    compute food wasted percentage
    :param perc_list:
    :return:
    """
    perc_food_wasted = 0
    if len(perc_list):
        perc_food_wasted = (sum(perc_list) / len(perc_list))*100
    return round(perc_food_wasted, 2)


def most_consumed(consumed_dict, limit=5):
    """
    filter the most consumed food
    :param consumed_dict:
    :param limit:
    :return:
    """
    most_consumed = {}  # dictionary which stores sum of values from consumed_dict
    for key, value in consumed_dict.items():
        numbers = value
        numbers_sum = sum(numbers)
        most_consumed[key] = numbers_sum
    most_consumed_sort = OrderedDict(sorted(most_consumed.items(), key=itemgetter(1), reverse=True)[:limit])
    return most_consumed_sort


def most_wasted(wasted_dict, limit=5):
    """
    filter the most wasted foods
    :param wasted_dict:
    :param limit:
    :return:
    """
    most_wasted = {}
    for key, value in wasted_dict.items():
        numbers = value
        numbers_sum = sum(numbers)
        most_wasted[key] = numbers_sum
    most_wasted_sort = OrderedDict(sorted(most_wasted.items(), key=itemgetter(1), reverse=True)[:limit])
    return most_wasted_sort

def suggestive_shopping_list(shopList, inventoryList):
    shop_list = list(OrderedDict.fromkeys(shopList))
    inventory = list(OrderedDict.fromkeys(inventoryList))
    suggestive_list = list(set(shop_list) - set(inventory))
    return suggestive_list

def updateRecord(user_id , perc_food_wasted, most_consumed, most_wasted, suggestive_shopping_list):
    """
    update record given user id
    :param user:
    :param perc_food_wasted:
    :param most_consumed:
    :param most_wasted:
    :return:
    """
    mycollection = db["users"]
    analysis ={
        'perc_wasted': perc_food_wasted,
        'most_consumed': most_consumed,
        'most_wasted': most_wasted,
        'suggestive_shopping_list': suggestive_shopping_list
    }
    print('update db of user {} with record:'.format(user_id))
    print(analysis)
    print('-------------------------------------------')
    mycollection.update({'_id': ObjectId(user_id)}, {"$set": {'analysis': analysis}}, upsert=False)

def close_connection():
    client.close()

def analyze(user_id='5a0baf55180916352c946b25'):
    record = get_record(user_id)
    result = analyze_record(record)
    print(user_id, result['percentage wasted'], result['most consumed'], result['most wasted'], result['suggestive_shopping_list'])
    close_connection()

if __name__ == '__main__':
    analyze()