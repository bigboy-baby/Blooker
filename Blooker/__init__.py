import threading
from .modules.join import join_e, status

def __init__():
    pass

class bot:
    def join(code, name, blook):
        try:
            x = threading.Thread(target=join_e, args=(code,name,blook))
            x.start()
            return True
        except:
            pass
            return False
        