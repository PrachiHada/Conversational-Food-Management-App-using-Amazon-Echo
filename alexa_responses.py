

# --------------- Helpers that build all of the responses ----------------------

def build_speechlet_response(title, output, reprompt_text='', should_end_session=False):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'card': {
            'type': 'Simple',
            'title': "SessionSpeechlet - " + title,
            'content': "SessionSpeechlet - " + output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }


def build_response(session_attributes, speechlet_response):
    return {
        'version': '1.0',
        'sessionAttributes': session_attributes,
        'response': speechlet_response
    }

# --------------- speechlet responses ----------------------

def get_welcome_response():
    """ If we wanted to initialize the session to have some attributes we could
    add those here
    """
    session_attributes = {}

    card_title = "Welcome"

    speech_output = 'Welcome to consume it food management system. You have logged in successfully. ' \
                    'What would you like consumit to do for you. You can either directly go to the task or listen to options. ' \
                    'to listen to menu options say: View Main Menu'
    reprompt_text = 'Sorry, I did not receive any response. What would you like consumit to do for you?'

    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text))

def get_main_menu_response():
    card_title = 'View Main Menu'
    speech_output = 'Welcome to consume it food management system. ' \
                    'You can choose one of the following 8 activities: ' \
                    'View Main Menu, Check Profile, Add Inventory, View Inventory, Update Inventory, Ask question about Inventory, ' \
                    'What should I buy, Create new Shopping List, Add to Shopping List, Remove from Shopping List, View Shopping List,' \
                    'View Most Consumed Food Items, View Most Wasted Food Items,' \
                    'Please say the task you would like consume it to do for you '
    reprompt_text = 'I have not received a response. To repeat main menu say: View Main Menu'
    return build_response({}, build_speechlet_response(card_title, speech_output, reprompt_text))

def get_invalid_login_response():
    card_title = 'Invalid Login'
    speech_output = 'Welcome to consume it food management system. '\
                    'You have not registered this device or the code is invalid, please get the code from mobile app first. '\
                    'To register, please say, the registration code is. '
    reprompt_text = 'To register, get the code from your mobile app and say the registration code is.'
    return build_response({}, build_speechlet_response(card_title, speech_output, reprompt_text))

def get_profile_response(profile):
    card_title = 'CheckProfile'
    name = profile['display_name'] or 'Khoa'
    end_statement = 'What else would you like to do: to listen to menu options say: View Main Menu'
    speech_output = 'Your name is {}. {}'.format(name, end_statement)
    print(profile)
    return build_response({}, build_speechlet_response(card_title,speech_output))

def get_viewInventory_response(result):
    card_title = 'ViewInventory'
    item_list = result
    end_statement = 'What else would you like to do: to listen to menu options say: View Main Menu'
    speech_output = 'Your have {}. {}'.format(item_list, end_statement)
    return build_response({}, build_speechlet_response(card_title,speech_output))

def addInventory_response():
    card_title = 'AddInventory'
    speech_output = 'You have chosen to add inventory. Please provide input in format: quantity type food item expiry.'\
                    'Example: 4 apples or 1 lb apples or 2 count apples expiry may twenty fifth'
    return build_response({}, build_speechlet_response(card_title,speech_output))

def askQuestion_response():
    card_title = 'AskQuestion'
    speech_output = 'Please ask your question in format: How many food item do I have.'\
                    'Example: How many apples do I have'
    return build_response({}, build_speechlet_response(card_title,speech_output))

def get_questFormat_response(item, count):
    card_title = 'QuestionResponse'
    end_statement = 'What else would you like to do: to listen to menu options say: View Main Menu'
    speech_output = 'you have {} {}. {}'.format(count, item, end_statement)
    return build_response({}, build_speechlet_response(card_title,speech_output))

def add_item_response(res):
    card_title = 'AddItem'
    speech_output =  res
    print(speech_output)
    return build_response({}, build_speechlet_response(card_title,speech_output))

def updateInventory_response(intent, session):
    card_title = 'UpdateInventory'
    speech_output = 'You have chosen to update inventory. Please provide amount of food consumed in format: update ' \
                    'quantity quantity type food item. Example: update 4 count apples or update 1 pound apples'
    return build_response({}, build_speechlet_response(card_title,speech_output))

def updateItem_response(res):
    card_title = 'UpdateItem'
    end_statement = 'What else would you like to do: to listen to menu options say: View Main Menu'
    speech_output = '{}. {}'.format(res, end_statement)
    print(speech_output)
    return build_response({}, build_speechlet_response(card_title, speech_output))

def get_most_consumed_response(res):
    card_title = 'MostConsumed'
    end_statement = 'What else would you like to do: to listen to menu options say: View Main Menu'
    speech_output = '{}. {}'.format(res, end_statement)
    print(speech_output)
    return build_response({}, build_speechlet_response(card_title, speech_output))

def get_most_wasted_response(res):
    card_title = 'MostWasted'
    end_statement = 'What else would you like to do: to listen to menu options say: View Main Menu'
    speech_output = '{}. {}'.format(res, end_statement)
    print(speech_output)
    return build_response({}, build_speechlet_response(card_title, speech_output))

def get_suggest_shopping_list_response(res):
    card_title = 'MostWasted'
    end_statement = 'What else would you like to do: to listen to menu options say: View Main Menu'
    speech_output = '{}. {}'.format(res, end_statement)
    print(speech_output)
    return build_response({}, build_speechlet_response(card_title, speech_output))

def get_view_shopping_list_response(res):
    card_title = 'MostWasted'
    end_statement = 'What else would you like to do: to listen to menu options say: View Main Menu'
    speech_output = '{}. {}'.format(res, end_statement)
    print(speech_output)
    return build_response({}, build_speechlet_response(card_title, speech_output))

def get_create_shopping_list_response():
    card_title = 'CreateNewShoppingList'
    #end_statement = 'What else would you like to do: to listen to menu options say: View Main Menu'
    res = 'This option will overwrite old shopping list. To create new shopping list say: Create shopping list: followed by item names. Example: Create shopping list: apple, mango, onions '
    speech_output = '{}.'.format(res)
    print(speech_output)
    return build_response({}, build_speechlet_response(card_title, speech_output))

def get_remove_item_shopping_list_response(res):
    card_title = 'RemoveFromShoppingList'
    end_statement = 'to listen to menu options say: View Main Menu'
    speech_output = '{}. {}'.format(res, end_statement)
    print(speech_output)
    return build_response({}, build_speechlet_response(card_title, speech_output))

def get_add_item_shopping_list_response(res):
    card_title = 'AddToShoppingList'
    end_statement = 'To listen to shopping list say: View Shopping List. to listen to menu options say: View Main Menu'
    speech_output = '{}. {}'.format(res, end_statement)
    print(speech_output)
    return build_response({}, build_speechlet_response(card_title, speech_output))

def get_test_date_response(res):
    card_title = 'testDate'
    end_statement = 'What else would you like to do: to listen to menu options say: View Main Menu'
    speech_output = 'The date which you have input is {} and its type is {}.'.format(res, type(res))
    print(speech_output)
    return build_response({}, build_speechlet_response(card_title, speech_output))