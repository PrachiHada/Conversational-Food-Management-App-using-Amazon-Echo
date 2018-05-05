"""
Place to store all constants and configuration
"""
# -------------------------------------------------

ALEXA_CODE = 'alexa_code'
ALEXA_ID = 'alexa_id'
USER_ID = 'user_id'
ACCESS_TOKEN = 'access_token'
MG_ID = '_id'

# ------------------ alexa service --------------------

REGIS_CODE_SLOT = 'registration_code'
SESSION_ATTRIBUTES = 'session_attributes'
SLOTS = 'slots'
SLOTS_VALUE = 'value'
FOOD_ITEM_SLOT = 'foodItems'
#There are 8 custom slot types and 51 other slots so no point of writing such a big list here

# --------------------- intent ------------------------
"""
put all intents here for easy access
"""
class Intent():
    REGISTRATION_INTENT = 'Registration'
    CHECK_PROFILE_INTENT = 'CheckProfile'
    ADD_INVENTORY_INTENT = 'AddInventory'
    VIEW_INVENTORY_INTENT = 'ViewInventory'
    ASK_QUESTION_INTENT = 'AskQuestion'
    QUES_FORMAT_INTENT = 'QuesFormat'
    ADD_ITEM_INTENT = 'AddItems'
    UPDATE_INVENTORY_INTENT = 'UpdateInventory'
    UPDATE_ITEM_INTENT = 'UpdateItem'
    MAIN_MENU_INTENT = 'MainMenu'
    MOST_CONSUMED_INTENT = 'MostConsumed'
    MOST_WASTED_INTENT = 'MostWasted'
    SUGGEST_SHOPPING_LIST_INTENT = 'SuggestShoppingList'
    VIEW_SHOPPING_LIST_INTENT = 'ViewShoppingList'
    CREATE_SHOPPING_LIST_INTENT = 'CreateNewShoppingList'
    ADD_ITEM_NEW_SHOPPING_LIST_INTENT = 'AddItemsNewShoppingList'
    REMOVE_FROM_LIST_INTENT = 'RemoveFromShoppingList'
    ADD_TO_SHOPPING_LIST_INTENT = 'AddToShoppingList'

# ------------------ requests ---------------------------

# HOST = 'http://756b375e.ngrok.io'
#HOST = 'http://52.53.230.217:5000'
#apr2#HOST = 'http://54.152.119.134:5000'
HOST = 'http://consumit-TCP-load-balancer-e91db1be6adc1ff0.elb.us-east-1.amazonaws.com:5000'
VERSION = '/api/v1.0'

# ---------------------- sameple data ------------------------

ALEXA_ID_SAMPLE = 'amzn1.ask.account.AFYQD22YHE24VWCDZS2NWK5HOE2UL7GVKRMYBV62LNA7NMGOMDTKMXEITKNTCUW2EXVNJLIGEJSQM6DBU5NIF2JWEVP75MOZSVKC7RBXIMVJYGU62MBHURSEDN6U35JDJIXOJAMCFBCOSUPP5JFZMOW4EQUIGHR76VQEGNOC7SSF5567X6W65N57IZGIMV6LNJWD4B7XTV7BZKA'
#ALEXA_ID_SAMPLE = 'amzn1.ask.account.AHHIQNBPLOVKEQ4TCQTI5EGBHEXTS4GUZEQEDLZOITF4B3UXMJQYIMRJ3QXDEPU5L46K3223S3G3EJH4TFEA7'\
#    'ZDTUFTBBRO4CRTO5E52RKCK6SC7FQ2LM7YSS7QHEVSFVM6AJMQ5N6KSHZXHJWEZIHG3UFNCCHCW4DY5GRRHVHH6LMTGGG7JC2MXVFI4CWDRQLSDABJSE4RDYSY'
REGISTRATION_CODE_SAMPLE = 115255
FOOD_ITEM_SAMPLE = 'apples'

#----------------------------------------------------------------

SEQUENCE_LIST = ['One', 'Two', 'Three', 'Four', 'Five']
SHOPPING_SEQUENCE_LIST = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten']

FOOD_ITEM_DICT = [{"slot_value":"apple","name":"apple","type":"fruit", "expiry":10},
 {"slot_value":"apples","name":"apple","type":"fruit", "expiry":10},
 {"slot_value":"avocado","name":"avocado","type":"fruit", "expiry":10},
 {"slot_value":"banana","name":"banana","type":"fruit", "expiry":10},
 {"slot_value":"bananas","name":"banana","type":"fruit", "expiry":10},
 {"slot_value":"grapes","name":"grapes","type":"fruit", "expiry":10},
 {"slot_value":"guava","name":"guava","type":"fruit", "expiry":10},
 {"slot_value":"guavas","name":"guava","type":"fruit", "expiry":10},
 {"slot_value":"mango","name":"mango","type":"fruit", "expiry":10},
 {"slot_value":"mangoes","name":"mango","type":"fruit", "expiry":10},
 {"slot_value":"orange","name":"orange","type":"fruit", "expiry":10},
 {"slot_value":"oranges","name":"orange","type":"fruit", "expiry":10},
 {"slot_value":"papaya","name":"papaya","type":"fruit", "expiry":10},
 {"slot_value":"pear","name":"pear","type":"fruit", "expiry":10},
 {"slot_value":"pears","name":"pear","type":"fruit", "expiry":10},
 {"slot_value":"watermelon","name":"watermelon","type":"fruit", "expiry":10},
 {"slot_value":"watermelons","name":"watermelon","type":"fruit", "expiry":10},
 {"slot_value":"blackberries","name":"blackberries","type":"fruit", "expiry":10},
 {"slot_value":"blueberries","name":"blueberries","type":"fruit", "expiry":10},
 {"slot_value":"grapefruit","name":"grapefruit","type":"fruit", "expiry":10},
 {"slot_value":"grapefruits","name":"grapefruit","type":"fruit", "expiry":10},
 {"slot_value":"lemon","name":"lemon","type":"fruit", "expiry":10},
 {"slot_value":"lemons","name":"lemon","type":"fruit", "expiry":10},
 {"slot_value":"lime","name":"lime","type":"fruit", "expiry":10},
 {"slot_value":"limes","name":"lime","type":"fruit", "expiry":10},
 {"slot_value":"nectarine","name":"nectarine","type":"fruit", "expiry":10},
 {"slot_value":"nectarines","name":"nectarine","type":"fruit", "expiry":10},
 {"slot_value":"peach","name":"peach","type":"fruit", "expiry":10},
 {"slot_value":"peaches","name":"peach","type":"fruit", "expiry":10},
 {"slot_value":"pineapple","name":"pineapple","type":"fruit", "expiry":10},
 {"slot_value":"pineapples","name":"pineapple","type":"fruit", "expiry":10},
 {"slot_value":"plum","name":"plum","type":"fruit", "expiry":10},
 {"slot_value":"plums","name":"plum","type":"fruit", "expiry":10},
 {"slot_value":"raspberries","name":"raspberries","type":"fruit", "expiry":10},
 {"slot_value":"strawberries","name":"strawberries","type":"fruit", "expiry":10},
 {"slot_value":"strawberrry","name":"strawberries","type":"fruit", "expiry":10},
 {"slot_value":"onion","name":"onion","type":"vegetable", "expiry":7},
 {"slot_value":"onions","name":"onion","type":"vegetable", "expiry":7},
 {"slot_value":"zucchini","name":"zucchini","type":"vegetable", "expiry":7},
 {"slot_value":"zucchinis","name":"zucchini","type":"vegetable", "expiry":7},
 {"slot_value":"tomato","name":"tomato","type":"vegetable", "expiry":7},
 {"slot_value":"tomatoes","name":"tomato","type":"vegetable", "expiry":7},
 {"slot_value":"pepper","name":"pepper","type":"vegetable", "expiry":7},
 {"slot_value":"peppers","name":"pepper","type":"vegetable", "expiry":7},
 {"slot_value":"bell pepper","name":"bell pepper","type":"vegetable", "expiry":7},
 {"slot_value":"bell peppers","name":"bell pepper","type":"vegetable", "expiry":7},
 {"slot_value":"mushroom","name":"mushroom","type":"vegetable", "expiry":7},
 {"slot_value":"mushrooms","name":"mushroom","type":"vegetable", "expiry":7},
 {"slot_value":"garlic","name":"garlic","type":"vegetable", "expiry":7},
 {"slot_value":"carrot","name":"carrot","type":"vegetable", "expiry":7},
 {"slot_value":"carrots","name":"carrot","type":"vegetable", "expiry":7},
 {"slot_value":"cabbage","name":"cabbage","type":"vegetable", "expiry":7},
 {"slot_value":"broccoli","name":"broccoli","type":"vegetable", "expiry":7},
 {"slot_value":"beet","name":"beet","type":"vegetable", "expiry":7},
 {"slot_value":"beets","name":"beet","type":"vegetable", "expiry":7},
 {"slot_value":"asparagus","name":"asparagus","type":"vegetable", "expiry":7},
 {"slot_value":"potato","name":"potato","type":"vegetable", "expiry":7},
 {"slot_value":"potatoes","name":"potato","type":"vegetable", "expiry":7},
 {"slot_value":"cauliflower","name":"cauliflower","type":"vegetable", "expiry":7},
 {"slot_value":"cauliflowers","name":"cauliflower","type":"vegetable", "expiry":7},
 {"slot_value":"celery","name":"celery","type":"vegetable", "expiry":7},
 {"slot_value":"celeries","name":"celery","type":"vegetable", "expiry":7},
 {"slot_value":"cucumber","name":"cucumber","type":"vegetable", "expiry":7},
 {"slot_value":"cucumbers","name":"cucumber","type":"vegetable", "expiry":7},
 {"slot_value":"garlic","name":"garlic","type":"vegetable", "expiry":7},
 {"slot_value":"green bean","name":"green bean","type":"vegetable", "expiry":7},
 {"slot_value":"green beans","name":"green bean","type":"vegetable", "expiry":7},
 {"slot_value":"green onion","name":"green onion","type":"vegetable", "expiry":7},
 {"slot_value":"green onions","name":"green onion","type":"vegetable", "expiry":7},
 {"slot_value":"lettuce","name":"lettuce","type":"vegetable", "expiry":7},
 {"slot_value":"spinach","name":"spinach","type":"vegetable", "expiry":7},
 {"slot_value":"sweet potato","name":"sweet potato","type":"vegetable", "expiry":7},
 {"slot_value":"sweet potatoes","name":"sweet potato","type":"vegetable", "expiry":7},
 {"slot_value":"ginger","name":"ginger","type":"vegetable", "expiry":7},
 {"slot_value":"green chilly","name":"green chillies","type":"vegetable", "expiry":7},
 {"slot_value":"green chillies","name":"green chillies","type":"vegetable", "expiry":7},
 {"slot_value": "butter", "name": "butter", "type": "dairy", "expiry": 12},
 {"slot_value": "cheese", "name": "cheese", "type": "dairy", "expiry": 12},
 {"slot_value": "cream", "name": "cream", "type": "dairy", "expiry": 12},
 {"slot_value": "ice cream", "name": "ice cream", "type": "dairy", "expiry": 12},
 {"slot_value": "margarine", "name": "margarine", "type": "dairy", "expiry": 12},
 {"slot_value": "milk", "name": "milk", "type": "dairy", "expiry": 12},
 {"slot_value": "paneer", "name": "paneer", "type": "dairy", "expiry": 12},
 {"slot_value": "sour cream", "name": "sour cream", "type": "dairy", "expiry": 12},
 {"slot_value": "whipped cream", "name": "whipped cream", "type": "dairy", "expiry": 12},
 {"slot_value": "yogurt", "name": "yogurt", "type": "dairy", "expiry": 12},
 {"slot_value":"bacon","name":"bacon","type":"meat", "expiry":15},
 {"slot_value":"beef","name":"beef","type":"meat", "expiry":15},
 {"slot_value":"chicken","name":"chicken","type":"meat", "expiry":15},
 {"slot_value":"egg","name":"eggs","type":"meat", "expiry":15},
 {"slot_value":"eggs","name":"eggs","type":"meat", "expiry":15},
 {"slot_value":"lamb","name":"lamb","type":"meat", "expiry":15},
 {"slot_value":"pork","name":"pork","type":"meat", "expiry":15},
 {"slot_value":"salami","name":"salami","type":"meat", "expiry":15},
 {"slot_value":"shrimp","name":"shrimp","type":"meat", "expiry":15},
 {"slot_value":"sausage","name":"sausage","type":"meat", "expiry":15},
 {"slot_value":"sausages","name":"sausage","type":"meat", "expiry":15},
 {"slot_value":"turkey","name":"turkey","type":"meat", "expiry":15},
 {"slot_value":"barley","name":"barley","type":"grain", "expiry":30},
 {"slot_value":"maize","name":"maize","type":"grain", "expiry":30},
 {"slot_value":"oat","name":"oats","type":"grain", "expiry":30},
 {"slot_value":"oats","name":"oats","type":"grain", "expiry":30},
 {"slot_value":"wheat","name":"wheat","type":"grain", "expiry":30},
 {"slot_value":"rice","name":"rice","type":"grain", "expiry":30},
 {"slot_value":"beans","name":"beans","type":"grain", "expiry":60},
 {"slot_value":"chickpeas","name":"chickpeas","type":"grain", "expiry":60},
 {"slot_value":"lentils","name":"lentils","type":"grain", "expiry":60},
 {"slot_value":"peas","name":"peas","type":"grain", "expiry":60},
 {"slot_value":"soybean","name":"soybean","type":"grain", "expiry":60},
 {"slot_value":"oil","name":"oil","type":"oil", "expiry":90},
 {"slot_value":"cornflakes","name":"cornflakes","type":"cereals", "expiry":90},
 {"slot_value":"cereals","name":"cereals","type":"cereals", "expiry":90},
 {"slot_value":"biscuits","name":"biscuits","type":"bakery", "expiry":90},
 {"slot_value":"cookies","name":"cookies","type":"bakery", "expiry":90},
 {"slot_value":"cake","name":"cake","type":"bakery", "expiry":90},
 {"slot_value":"coffee","name":"coffee","type":"beverage", "expiry":120},
 {"slot_value":"tea","name":"tea","type":"beverage", "expiry":120},
 {"slot_value":"sugar","name":"sugar","type":"sugar", "expiry":120},
 {"slot_value":"salt","name":"salt","type":"salt", "expiry":120},
]


FOOD_ITEM_DICT_OLD = [{"slot_value":"apple","name":"apple","type":"fruit"},
 {"slot_value":"apples","name":"apple","type":"fruit"},
 {"slot_value":"avocado","name":"avocado","type":"fruit"},
 {"slot_value":"banana","name":"banana","type":"fruit"},
 {"slot_value":"bananas","name":"banana","type":"fruit"},
 {"slot_value":"grapes","name":"grapes","type":"fruit"},
 {"slot_value":"guava","name":"guava","type":"fruit"},
 {"slot_value":"guavas","name":"guava","type":"fruit"},
 {"slot_value":"mango","name":"mango","type":"fruit"},
 {"slot_value":"mangoes","name":"mango","type":"fruit"},
 {"slot_value":"orange","name":"orange","type":"fruit"},
 {"slot_value":"oranges","name":"orange","type":"fruit"},
 {"slot_value":"papaya","name":"papaya","type":"fruit"},
 {"slot_value":"pear","name":"pear","type":"fruit"},
 {"slot_value":"pears","name":"pear","type":"fruit"},
 {"slot_value":"watermelon","name":"watermelon","type":"fruit"},
 {"slot_value":"watermelons","name":"watermelon","type":"fruit"},
 {"slot_value":"onion","name":"onion","type":"vegetable"},
 {"slot_value":"onions","name":"onion","type":"vegetable"},
 {"slot_value":"zucchini","name":"zucchini","type":"vegetable"},
 {"slot_value":"tomato","name":"tomato","type":"vegetable"},
 {"slot_value":"tomatoes","name":"tomato","type":"vegetable"},
 {"slot_value":"pepper","name":"pepper","type":"vegetable"},
 {"slot_value":"peppers","name":"pepper","type":"vegetable"},
 {"slot_value":"mushroom","name":"mushroom","type":"vegetable"},
 {"slot_value":"mushrooms","name":"mushroom","type":"vegetable"},
 {"slot_value":"garlic","name":"garlic","type":"vegetable"},
 {"slot_value":"carrot","name":"carrot","type":"vegetable"},
 {"slot_value":"carrots","name":"carrot","type":"vegetable"},
 {"slot_value":"cabbage","name":"cabbage","type":"vegetable"},
 {"slot_value":"broccoli","name":"broccoli","type":"vegetable"},
 {"slot_value":"beet","name":"beet","type":"vegetable"},
 {"slot_value":"beets","name":"beet","type":"vegetable"},
 {"slot_value":"asparagus","name":"asparagus","type":"vegetable"},
 {"slot_value":"potato","name":"potato","type":"vegetable"},
 {"slot_value":"potatoes","name":"potato","type":"vegetable"}
]