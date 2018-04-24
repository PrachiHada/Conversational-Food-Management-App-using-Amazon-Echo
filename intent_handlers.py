import helper_functions
import alexa_responses
import config


@helper_functions.verify_alexa_login()
def handle_launch_request(launch_request, session):
    return alexa_responses.get_welcome_response()

def handle_alexa_registration(intent, session):
    # session_attributes = get_session_attributes(session)
    alexa_code = intent[config.SLOTS][config.REGIS_CODE_SLOT][config.SLOTS_VALUE]
    alexa_id = helper_functions.get_alexa_user_id(session)
    res = helper_functions.alexa_register(alexa_code, alexa_id)
    if res.status_code == 404:
        return alexa_responses.get_invalid_login_response()
    # inject authen data
    res = res.json()
    helper_functions.save_authen(session, res[config.MG_ID], res[config.ACCESS_TOKEN])
    return alexa_responses.get_welcome_response()


@helper_functions.verify_alexa_login()
def handle_get_profile(intent, session):
    # session_attributes = get_session_attributes(session)
    res1 = helper_functions.get_authen(session)
    print("print1:".format(res1))
    res = helper_functions.get_user_profile(*helper_functions.get_authen(session))
    if res.status_code != 200:
        raise ValueError(res.status_code)
    res = res.json()
    return alexa_responses.get_profile_response(res)

@helper_functions.verify_alexa_login()
def handle_view_inventory(intent, session):
    res = helper_functions.get_user_inventory(*helper_functions.get_authen(session))
    print(res)
    return alexa_responses.get_viewInventory_response(res)

@helper_functions.verify_alexa_login()
def handle_quest_format(intent, session):
    if 'foodItems' in intent['slots']:
        item = intent['slots']['foodItems']['value']
    count = helper_functions.get_item_quantity(*helper_functions.get_authen(session), item)
    return alexa_responses.get_questFormat_response(item, count)

@helper_functions.verify_alexa_login()
def handle_update_item(intent, session):
    #res1 = helper_functions.get_authen(session)
    #print(res1[0])
    #print(type(res1[0]))
    #print(res1[1])
    print("Inside handle_update_item access token: {}".format(session['session_attributes']['access_token']))
    user_id = session['session_attributes']['user_id']
    access_token = session['session_attributes']['access_token']
    '''
    name = 'bananas'
    amount_eaten = 1
    quantity_type = 'count'
    for x in config.FOOD_ITEM_DICT:
        if x["slot_value"] == name:
            print(x["name"])
            name = x["name"]
            print("name : {}".format(name))
    '''
    name = 'not supported'
    amount_eaten = 0
    quantity_type = 'not supported'
    
    if 'quantity' in intent['slots']:
        if 'value' in intent['slots']['quantity']:
            amount_eaten = intent['slots']['quantity']['value']

            if 'quantityType' in intent['slots']:
                if 'value' in intent['slots']['quantityType']:
                    quantity_type = intent['slots']['quantityType']['value']
                    if quantity_type == 'pound':
                        quantity_type = 'lb'

            if 'foodItem' in intent['slots']:
                if 'value' in intent['slots']['foodItem']:
                    name = intent['slots']['foodItem']['value']

            for x in config.FOOD_ITEM_DICT:
                if x["slot_value"] == name:
                    name = x["name"]

    #res = helper_functions.update_item(str(res1[0]), res1[1], name, int(amount_eaten), quantity_type)
    res = helper_functions.update_item(user_id, access_token, name, int(amount_eaten), quantity_type)
    return alexa_responses.updateItem_response(res)

@helper_functions.verify_alexa_login()
def handle_add_item(intent, session):

    print("Inside handle_add_item access token: {}".format(session['session_attributes']['access_token']))
    user_id = session['session_attributes']['user_id']
    access_token = session['session_attributes']['access_token']
    var_count = 'count'
    var_quantityType = 'quantityType'
    var_foodItem = 'foodItem'
    quantity = 0
    var_response = " following items are added to inventory: "

    for x in config.SEQUENCE_LIST:
        count = var_count + x
        quantityType = var_quantityType + x
        foodItem = var_foodItem + x

        if count in intent['slots']:
            if 'value' in intent['slots'][count]:
                quantity = intent['slots'][count]['value']

                if quantityType in intent['slots']:
                    if 'value' in intent['slots'][quantityType]:
                        quantity_type = intent['slots'][quantityType]['value']
                        if quantity_type == 'pound':
                            quantity_type = 'lb'
                    else:
                        quantity_type = 'count'

                if foodItem in intent['slots']:
                    if 'value' in intent['slots'][foodItem]:
                        name_var = intent['slots'][foodItem]['value']

                for x in config.FOOD_ITEM_DICT:
                    if x["slot_value"] == name_var:
                        print(x["name"], x["type"])
                        helper_functions.put_add_item(user_id, access_token, x["name"], quantity, quantity_type, x["type"])
                        var_response = var_response + str(quantity) + " " + quantity_type + " " + x["name"] + ", "



    #put_add_item(user_id, access_token, 'apple', 11, 'count', 'fruit')
    print(var_response)
    return alexa_responses.add_item_response(var_response)