access_data = {'user':'moliabal', 'password':'secret', 'db':'moliabal', 'host':'127.0.0.1'}
dest_folder = {'path':''}

def get_dest_folder():
    return dest_folder.get('path',None) or None
    
