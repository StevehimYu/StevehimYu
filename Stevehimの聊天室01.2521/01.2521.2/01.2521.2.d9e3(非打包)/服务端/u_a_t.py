import json
# user格式(不用输入，客户端自动)
users = {
    "在线": {},
    "离线": {},
    "黑名单": {},
}
# token格式
token = {}
while True:
    msg = input("token:")
    name = input("用户名:")
    token[msg] = {
        'name':"",
        'password':"",
    }
    token[msg]['name'] = name
    m = input("回车继续，输入c退出")
    if m == "c":
        break
    else:
        pass
with open('users.json', 'w') as f_obj:
    json.dump(users, f_obj)

with open('token.json', 'w') as f_obj:
    json.dump(token, f_obj)

