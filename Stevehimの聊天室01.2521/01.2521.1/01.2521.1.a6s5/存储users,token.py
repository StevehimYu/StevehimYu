import json
# user格式(不用输入，客户端自动)
users = {
    "在线": {},
    "离线": {},
    "黑名单": {},
}
# token格式
token = {
    "": {
        'name': '',
        'password': ""
    },
}

with open('users.json', 'w') as f_obj:
    json.dump(users, f_obj)

with open('token.json', 'w') as f_obj:
    json.dump(token, f_obj)