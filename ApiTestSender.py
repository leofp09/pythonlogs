import requests

locallink = 'http://localhost:5000/sendlog'


log = {
    "level":"alert",
    "text":"TTTaT",
    
    
}
lista = {
    "logname":"gggg"
}

#res = requests.post(locallink, json=lista)


res = requests.post(locallink, json=log)

if res.ok:
    print(res.json())
else :
    print(res)

