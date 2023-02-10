import threading
import requests, websocket, json, random, string

status = ""

def __init__():
    pass

class bot:
    def join_e(code, name, blook):
        rnd = ('').join(random.choices(string.digits, k=5))
        gameName = f"{name}_{rnd}"
        d = {"id":code,"name":gameName}
        s = requests.session()
        s.get("https://play.blooket.com/play")
        r = s.put("https://fb.blooket.com/c/firebase/join", json=d)
        res = r.json()
        verif = res["fbToken"]
        end_part = res["fbShardURL"]
        end_part2 = end_part.replace("https://", "")
        ns = end_part2.replace(".firebaseio.com/", "")

        d2 = {"token":verif,"returnSecureToken":True}
        r2 = s.post("https://identitytoolkit.googleapis.com/v1/accounts:signInWithCustomToken?key=AIzaSyCA-cTOnX19f6LFnDVVsHXya3k6ByP_MnU", json=d2)
        res2 = r2.json()
        cred = res2["idToken"]

        ws1 = websocket.WebSocket()
        ws1.connect(f'wss://s-usc1c-nss-200.firebaseio.com/.ws?v=5&ns={ns}')
        dat = json.loads(ws1.recv())
        ws1.close()
        server = dat["d"]["d"]
        newUrl = f"wss://{server}/.ws?v=5&p=1:741533559105:web:b8cbb10e6123f2913519c0&ns={ns}"
        ws = websocket.WebSocket()
        ws.connect(newUrl)
        msg1 = {"t":"d","d":{"r":1,"a":"s","b":{"c":{"sdk.js.9-16-0":1}}}}
        ws.send(json.dumps(msg1))
        msg2 = {"t":"d","d":{"r":2,"a":"auth","b":{"cred":cred}}}
        ws.send(json.dumps(msg2))
        msg3 = {"t":"d","d":{"r":3,"a":"q","b":{"p":f"/{code}","h":""}}}
        ws.send(json.dumps(msg3))
        msg4 = {"t":"d","d":{"r":4,"a":"n","b":{"p":f"/{code}"}}}
        ws.send(json.dumps(msg4))
        msg5 = {"t":"d","d":{"r":5,"a":"p","b":{"p":f"/{code}/c/{gameName}","d":{"b":blook}}}}
        ws.send(json.dumps(msg5))
        msg6 = {"t":"d","d":{"r":6,"a":"q","b":{"p":f"/{code}/c","h":""}}}
        ws.send(json.dumps(msg6))
        msg7 = {"t":"d","d":{"r":7,"a":"q","b":{"p":f"/{code}/stg","h":""}}}
        ws.send(json.dumps(msg7))
        msg8 = {"t":"d","d":{"r":8,"a":"p","b":{"p":f"/{code}/c/{gameName}","d":{"b":blook}}}}
        ws.send(json.dumps(msg8))
        ws.close()

    def join(code, name, blook):
        try:
            x = threading.Thread(target=bot.join_e, args=(code,name,blook))
            x.start()
            return True
        except:
            pass
            return False
        