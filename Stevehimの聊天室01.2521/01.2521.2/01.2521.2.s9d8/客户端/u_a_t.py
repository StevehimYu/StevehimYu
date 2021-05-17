import json
token = {
    'token':"",
}
token['token'] = input("自己的token")
with open('token.json', 'w') as f_obj:
    json.dump(token, f_obj)

