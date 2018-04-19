"""
Place to configure and write tests
simple test should be done here, before deployment. for more complex test, go to alexa dev console
"""
import intent_handlers
import config
from helper_functions import put_add_item, get_authen
from alexa_responses import add_item_response

def test():
    pass

def test_check_profile():
    intent = {}
    session = {'user':{'userId':config.ALEXA_ID_SAMPLE}}
    #print(session)
    res = intent_handlers.handle_get_profile(intent, session)
    print(res)

def test_view_inventory():
    intent = {}
    session = {'user':{'userId':config.ALEXA_ID_SAMPLE}}
    print("--------------------------------")
    res = intent_handlers.handle_view_inventory(intent, session)
    print(res)

'''
def test_ques_response():
    intent = {SLOTS: {
        FOOD_ITEM_SLOT: {
            SLOTS_VALUE: FOOD_ITEM_SAMPLE
        }
    }}
    session = {'user':{'userId':ALEXA_ID_SAMPLE}}
    print("--------------------------------")
    res = handle_quest_format(intent, session)
    print(res)
'''

def test_ques_response():
    intent = {'slots': {
        'foodItems': {
            'value': 'apple'
        }
    }}
    session = {'user':{'userId':config.ALEXA_ID_SAMPLE}}
    print("--------------------------------")
    res = intent_handlers.handle_quest_format(intent, session)
    print(res)

def test_addItem_response():
    intent = {}
    session = {'user': {'userId': config.ALEXA_ID_SAMPLE}}
    print("-------------------------------- passing {}".format(session))
    #res1 = get_authen(session)
    #print("print111111111:".format(res1))
    print()
    #user_id = session['session_attributes']['user_id']
    #access_token = session['session_attributes']['access_token']
    res = intent_handlers.handle_add_item(intent, session)
    #put_add_item(*get_authen(session), 'apple', '5', 'lb', 'fruit')

    print(res)


def test_alexa_registration():
    intent = {config.SLOTS: {
        config.REGIS_CODE_SLOT:{
            config.SLOTS_VALUE: config.REGISTRATION_CODE_SAMPLE
        }
    }}
    session={
        'user':{
            'userId': config.ALEXA_ID_SAMPLE
        }
    }
    res = intent_handlers.handle_alexa_registration(intent, session)
    print(res)


if __name__ == '__main__':
    #test_check_profile()
    test_view_inventory()