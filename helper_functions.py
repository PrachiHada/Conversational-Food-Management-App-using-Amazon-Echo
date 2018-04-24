import pymongo
import requests
import json
import functools
from pymongo import MongoClient
from bson.objectid import ObjectId
from collections import defaultdict
from pprint import pprint
from collections import OrderedDict
from operator import itemgetter
import sys
from datetime import datetime
import alexa_responses
import config

# --------------Helper that help to make requests to the backend ---------------------------

MONGODB_URI = "mongodb://consumitDev:consumitNov2017#@ds259085.mlab.com:59085/consumitdev"
client = MongoClient(MONGODB_URI, connectTimeoutMS=30000)
db = client.get_default_database()
collection = db['food_items']

def alexa_login(alexa_id):
    url = '/users/alexa/{}'.format(alexa_id)
    r = requests.get(build_url(url))
    return r

def alexa_register(alexa_code, alexa_id):
    url = '/users/alexa/registration'
    r = requests.put(build_url(url),
                     data=json.dumps({config.ALEXA_CODE: alexa_code, config.ALEXA_ID:alexa_id}),
                     headers={'Content-Type': 'application/json'})
    if r.status_code != 200:
        message = r.status_code
        raise ValueError(r.status_code)
    return r

def get_user_profile(user_id, access_token):
    url = '/users/{}'.format(user_id)
    r = requests.get(build_url(url),
                     headers={config.USER_ID: user_id, config.ACCESS_TOKEN: access_token})
    return r

def get_user_inventory(user_id, access_token):
    collection = db["food_items"]  # collection = db['food_items']
    user_id = ObjectId(user_id)
    cursor = collection.find({"user_id": user_id})
    item_dict = defaultdict(list)
    for document in cursor:
        cur_quant = document['quantity']
        today = datetime.now().date()
        today = datetime(today.year, today.month, today.day)
        if document['exp_date'] >= today and cur_quant != 0:
            item_dict[document['name']].append(cur_quant)
    rollUp_on_item = {}  # dictionary which stores sum of values from consumed_dict
    print(item_dict)


    for key, value in item_dict.items():
        numbers = value
        numbers_sum = sum(numbers)
        rollUp_on_item[key] = numbers_sum
    return rollUp_on_item


def get_item_quantity(user_id, access_token, foodItem):
    inventory = get_user_inventory(user_id, access_token)
    count = 0
    for key, value in inventory.items():
        if key == foodItem:
            count = value
        elif key == foodItem[:-1]:
            count = value
        elif key == foodItem[:-2]:
            count = value
    return count

def put_add_item(user_id, access_token, name, quantity, quantity_type, type):
    quantity = int(quantity)
    if type == 'fruit':
        expiry = 7
    elif type == 'vegetable':
        expiry = 10
    else:
        expiry = 5

    if name !=  'not Supported':
        url = '/food-items'
        r = requests.post(build_url(url),
                          data=json.dumps({'type': type, 'name': name, 'exp_days': expiry, 'quantity': quantity,
                                           'quantity_type': quantity_type}),
                          headers={config.USER_ID: user_id, config.ACCESS_TOKEN: access_token, 'Content-Type': 'application/json'})
        print(build_url(url))
        if r.status_code != 201:
            raise ValueError(r.status_code)




    '''

    item_id = '5ad572fc009089000b5adc6a'
    url = '/food-items/5ad572fc009089000b5adc6a/quantity'
    print("url {}". format(url))
    r = requests.put(build_url(url),
                      data=json.dumps({'amount': 2, 'action': 'eat', 'message': 'from ChatBot'}),
                      headers={USER_ID: user_id, ACCESS_TOKEN: access_token, 'Content-Type': 'application/json'})
    if r.status_code != 200:
        raise ValueError(r.status_code)
    return r
    '''
    '''
    url = '/analysis/most_wasted_consumed'
    r = requests.get(build_url(url),headers={USER_ID: user_id, ACCESS_TOKEN: access_token, 'Content-Type': 'application/json'})
    if r.status_code != 200:
        raise ValueError(r.status_code)
    return r
    '''


def update_item(user_id, access_token, name, amount_eaten, quantityType):
    collection = db["food_items"]  # collection = db['food_items']
    user_id = ObjectId(user_id)
    #cursor = collection.find({"user_id": user_id, "name": name, "quantity_type": quantityType})
    cursor = collection.find({"user_id": user_id, "name": name, "quantity_type": quantityType}).sort("input_date",pymongo.ASCENDING)
    today = datetime.now().date()
    today = datetime(today.year, today.month, today.day)


    print("cursor: {}".format(cursor.count()))
    if cursor.count() > 0:
        for document in cursor:
            cur_quant = document['quantity']
            if document['exp_date'] >= today and cur_quant != 0:
                print(document['name'], document['quantity_type'], cur_quant, document['_id'], document["input_date"])

                if cur_quant >= amount_eaten and amount_eaten > 0:
                    print("call put function for {} {}".format(document['_id'], cur_quant))
                    #call_api_to_update_food_item(document['_id'], amount_eaten, user_id, access_token)
                    amount_eaten = amount_eaten - cur_quant
                    print("inside if amt: {}".format(amount_eaten))
                    break
                else:
                    print("call put function for {} {}".format(document['_id'], cur_quant))
                    #call_api_to_update_food_item(document['_id'], amount_eaten, user_id, access_token)
                    amount_eaten = amount_eaten - cur_quant
                    print("inside else amt: {}".format(amount_eaten))
        message = "food item updated"
    else:
        message = "no items found with matching criteria"
    #print(message)
    return message

def call_api_to_update_food_item(item_id, amount_eaten, user_id, access_token):
    #item_id = '5ad572fc009089000b5adc6a'
    url = ('/food-items/{}/quantity').format(item_id)
    print("url {}".format(url))
    user_id = str(user_id)

    r = requests.put(build_url(url),
                     data=json.dumps({'amount': amount_eaten, 'action': 'eat', 'message': 'from ChatBot'}),
                     headers={config.USER_ID: user_id, config.ACCESS_TOKEN: access_token, 'Content-Type': 'application/json'})
    if r.status_code != 200:
        raise ValueError(r.status_code)



# --------------- authen decorator ----------------------

def verify_alexa_login():
    """
    decorator for alexa
    check if session attribute contain user_id field meaning log-in
    if not log-in, performm login
    if unable to login, response with welcome message
    
    decorate any function requiring login, the function needs to have 1 parameters
    and session has to be the second parameter
    """
    def verify(f):
        @functools.wraps(f)
        def decorated_function(*args, **kwds):
            session = args[1]
            session_attributes = get_session_attributes(session)
            alexa_id = get_alexa_user_id(session)
            if not session_attributes.get(config.USER_ID, ''):
                # login before proceeding
                r = alexa_login(alexa_id)
                if r.status_code != 200:
                    return alexa_responses.get_invalid_login_response()
                # inject user id and access token
                content = r.json()
                save_authen(session, content[config.MG_ID], content[config.ACCESS_TOKEN])
            return f(*args, **kwds)
        return decorated_function
    return verify

# --------------- other helpers ----------------------

def get_host():
    return config.HOST + config.VERSION

def cleanse_path(path):
    p = path
    if p and p[0] == '/':
        p = p[1:]
    return p

def build_url(path=''):
    return '{}/{}'.format(get_host(), cleanse_path(path))

def get_session_attributes(session):
    #print("returning from sessin_attributes {}".format(session))
    return session.get(config.SESSION_ATTRIBUTES, {})

def set_session_attribute(session, session_attributes):
    session[config.SESSION_ATTRIBUTES] = session_attributes

def get_alexa_user_id(session):
    return session['user']['userId']

def get_authen(session):
    #print("sending to get session {}".format(session))
    session_attributes = get_session_attributes(session)
    #print("printing session attributes {}".format(session_attributes))
    return (session_attributes[config.USER_ID], session_attributes[config.ACCESS_TOKEN])

def save_authen(session, user_id, access_token):
    session_attributes = get_session_attributes(session)
    session_attributes[config.USER_ID] = user_id
    session_attributes[config.ACCESS_TOKEN] = access_token
    set_session_attribute(session, session_attributes)

if __name__ == '__main__':
    print(alexa_register('946596','testing'))
