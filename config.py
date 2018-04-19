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

# ------------------ requests ---------------------------

# HOST = 'http://756b375e.ngrok.io'
#HOST = 'http://52.53.230.217:5000'
HOST = 'http://54.152.119.134:5000'
VERSION = '/api/v1.0'

# ---------------------- sameple data ------------------------

ALEXA_ID_SAMPLE = 'amzn1.ask.account.AFYQD22YHE24VWCDZS2NWK5HOE2UL7GVKRMYBV62LNA7NMGOMDTKMXEITKNTCUW2EXVNJLIGEJSQM6DBU5NIF2JWEVP75MOZSVKC7RBXIMVJYGU62MBHURSEDN6U35JDJIXOJAMCFBCOSUPP5JFZMOW4EQUIGHR76VQEGNOC7SSF5567X6W65N57IZGIMV6LNJWD4B7XTV7BZKA'
#ALEXA_ID_SAMPLE = 'amzn1.ask.account.AHHIQNBPLOVKEQ4TCQTI5EGBHEXTS4GUZEQEDLZOITF4B3UXMJQYIMRJ3QXDEPU5L46K3223S3G3EJH4TFEA7'\
#    'ZDTUFTBBRO4CRTO5E52RKCK6SC7FQ2LM7YSS7QHEVSFVM6AJMQ5N6KSHZXHJWEZIHG3UFNCCHCW4DY5GRRHVHH6LMTGGG7JC2MXVFI4CWDRQLSDABJSE4RDYSY'
REGISTRATION_CODE_SAMPLE = 115255
FOOD_ITEM_SAMPLE = 'apples'

#----------------------------------------------------------------

FOOD_ITEM_DICT = [{"slot_value":"apple","name":"apple","type":"fruit"},
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

SEQUENCE_LIST = ['One', 'Two', 'Three', 'Four', 'Five']