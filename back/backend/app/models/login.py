from app.config.utils import *

def login(username,pwd):
    res = None
    connection = connect()
    if connection is not None:
        if not username in 'boss@gmail.com':
            data = [username,pwd]
            query = 'select * from customers where username=%s and pwd=%s;'
            res = safety_get_query(connection,query,data)
            print 'customers'
            return res
        else:
            data = [username,pwd]
            query = 'select * from admin where username=%s and pwd=%s;'
            res = safety_get_query(connection,query,data)
            print 'boss'
            return res
    else:
        return None
        
