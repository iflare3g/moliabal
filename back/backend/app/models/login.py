from app.config.utils import *
from app.config.config import EMAIL

def login(username,pwd):
    res = None
    connection = connect()
    if connection is not None:
        if not username in EMAIL.get('mail',None) and username != None:
            data = [username,pwd]
            query = 'select * from customers where username=%s and pwd=%s;'
            res = safety_get_query(connection,query,data)
            param = None
            return res,param
        else:
            data = [username,pwd]
            query = 'select * from admin where username=%s and pwd=%s;'
            res = safety_get_query(connection,query,data)
            print 'boss'
            param = 'boss'
            return res,param
    else:
        return None
        
