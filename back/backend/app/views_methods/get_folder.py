from os import walk
import os
from flask import jsonify,request

def get_folder():
    folder = request.args.get('folder').replace(' ','')
    f = []
    files = {}
    mypath = 'app/static/img/' + folder
    for (dirpath, dirnames, filenames) in walk(mypath):
        f.extend(filenames)
        break
    f = map(lambda x:'../static/img/' + folder + '/'+ x,f)
    files['file'] = f
    if len(f) == 0:
        files['file'] = 'Nessun file presente'
    return jsonify(files)
    
    
def remove(file):
    try:
        msg=''
        if os.path.isfile(file):
            os.remove(file)
            msg = 'removed'
            return msg
        else:
            print('file not found')
            msg = 'file not found'
            return msg
    except:
        print('error')
    return msg