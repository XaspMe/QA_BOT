from Core.Controller import DB_Handle

var = DB_Handle.Handler()

var.add_communications_record(user_message='test', bot_response='test', chat_id=1)