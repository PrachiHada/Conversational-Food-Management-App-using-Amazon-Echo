import alexa_responses
import intent_handlers
import config
import intent_handlers


# --------------- Events ------------------

def on_session_started(session_started_request, session):
    """ Called when the session starts """
    print("on_session_started requestId={}, sessionId={}"
        .format(session_started_request['requestId'], session['sessionId']))


def on_launch(launch_request, session):
    """ Called when the user launches the skill without specifying what they
    want
    """
    print("on_launch requestId=" + launch_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # Dispatch to your skill's launch
    return intent_handlers.handle_launch_request(launch_request, session)


def on_intent(intent_request, session):
    """ Called when the user specifies an intent for this skill """
    print("on_intent requestId=" + intent_request['requestId'] +
          ", sessionId=" + session['sessionId'])

    intent = intent_request['intent']
    intent_name = intent['name']


    if intent_name == config.Intent.REGISTRATION_INTENT:
        return intent_handlers.handle_alexa_registration(intent, session)
    elif intent_name == config.Intent.CHECK_PROFILE_INTENT:
        return intent_handlers.handle_get_profile(intent, session)
    elif intent_name == config.Intent.VIEW_INVENTORY_INTENT:
        return intent_handlers.handle_view_inventory(intent, session)
    elif intent_name == config.Intent.ADD_INVENTORY_INTENT:
        return alexa_responses.addInventory_response()
    elif intent_name == config.Intent.ASK_QUESTION_INTENT:
        return alexa_responses.askQuestion_response()
    elif intent_name == config.Intent.QUES_FORMAT_INTENT:
        return intent_handlers.handle_quest_format(intent, session)
    elif intent_name == config.Intent.ADD_ITEM_INTENT:
        return intent_handlers.handle_add_item(intent, session)
    else:
        raise ValueError("Invalid intent")


def on_session_ended(session_ended_request, session):
    """ Called when the user ends the session.

    Is not called when the skill returns should_end_session=true
    """
    print("on_session_ended requestId=" + session_ended_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # add cleanup logic here

# --------------- Main handler ------------------

def lambda_handler(event, context):
    """ Route the incoming request based on type (LaunchRequest, IntentRequest,
    etc.) The JSON body of the request is provided in the event parameter.
    """
    print("event.session.application.applicationId=" +
          event['session']['application']['applicationId'])

    """
    Uncomment this if statement and populate with your skill's application ID to
    prevent someone else from configuring a skill that sends requests to this
    function.
    """

    if event['session']['new']:
        on_session_started({'requestId': event['request']['requestId']},
                           event['session'])

    if event['request']['type'] == "LaunchRequest":
        return on_launch(event['request'], event['session'])

    elif event['request']['type'] == "IntentRequest":
        return on_intent(event['request'], event['session'])

    elif event['request']['type'] == "SessionEndedRequest":
        return on_session_ended(event['request'], event['session'])
