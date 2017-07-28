from os import walk
import os
from flask import jsonify

def get_folder():
    f = []
    files = {}
    mypath = 'app/static/img/showroom/'
    for (dirpath, dirnames, filenames) in walk(mypath):
        f.extend(filenames)
        break
    f = map(lambda x:'../static/img/showroom/' + x,f)
    files['file'] = f
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