from Core.Controller import DB_Handle

var = DB_Handle.Handler()
var.make_user_admin(108)
if(var.user_is_admin(108)):
    print("Some text after warning")

