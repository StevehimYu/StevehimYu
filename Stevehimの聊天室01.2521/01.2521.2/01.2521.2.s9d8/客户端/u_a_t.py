import json
token = {
    'token':"",
    'passwd':""
}

with open('token.json', 'w') as f_obj:
    json.dump(token, f_obj)

