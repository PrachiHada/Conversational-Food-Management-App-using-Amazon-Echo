

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
                    'would you like to check profile, view inventory, add inventory, or ask question '
    reprompt_text = 'What would you like to do'

    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text))

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
    end_statement = 'What else would you like to do: view inventory, add inventory, or ask question'
    speech_output = 'Your name is {}. {}'.format(name, end_statement)
    print(profile)
    return build_response({}, build_speechlet_response(card_title,speech_output))

def get_viewInventory_response(result):
    card_title = 'ViewInventory'
    item_list = result
    end_statement = 'What else would you like to do: check profile, add inventory, or ask question'
    speech_output = 'Your have {}. {}'.format(item_list, end_statement)
    return build_response({}, build_speechlet_response(card_title,speech_output))

def addInventory_response():
    card_title = 'AddInventory'
    speech_output = 'You have chosen to add inventory. Please provide input in format 4 apples or 1 lb apples'
    return build_response({}, build_speechlet_response(card_title,speech_output))

def askQuestion_response():
    card_title = 'AskQuestion'
    speech_output = 'Please ask your question in format: How many apples do I have'
    return build_response({}, build_speechlet_response(card_title,speech_output))

def get_questFormat_response(item, count):
    card_title = 'QuestionResponse'
    end_statement = 'What else would you like to do: check profile, add inventory, or view inventory'
    speech_output = 'you have {} {}. {}'.format(count, item, end_statement)
    return build_response({}, build_speechlet_response(card_title,speech_output))

def add_item_response(res):
    card_title = 'AddItem'
    speech_output =  res
    print(speech_output)
    return build_response({}, build_speechlet_response(card_title,speech_output))