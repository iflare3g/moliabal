from app.config.utils import *

def login(username,pwd):
    res = None
    connection = connect()
    if connection is not None:
        data = [username,pwd]
        query = 'select * from customers where username=%s and pwd=%s;'
        res = safety_get_query(connection,query,data)
        return res
    else:
        return None
        
        