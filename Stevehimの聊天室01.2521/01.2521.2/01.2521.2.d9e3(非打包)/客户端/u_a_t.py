import json
try:
    with open('token') as f:
        token = json.load(f)
except FileNotFoundError:
    token = {
        'token':"",
    }
token['token'] = input("自己的token:")
with open('token.json', 'w') as f_obj:
    json.dump(token, f_obj)

