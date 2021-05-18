import json
import os
def OJ():
    try:
        with open('users.json') as f_obj:
            users = json.load(f_obj)
        with open('token.json') as f_obj:
            token = json.load(f_obj)
    except FileNotFoundError:
        os.system("u_a_t.py")
        with open('users.json') as f_obj:
            users = json.load(f_obj)
        with open('token.json') as f_obj:
            token = json.load(f_obj)
    return token,users

def dumpJson(token):
    with open('token.json','w') as f_obj:
        json.dump(token, f_obj)