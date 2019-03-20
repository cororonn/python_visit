class Destoroy():
    def __init__(self):
        print("5")

class later(Destoroy):
    def OK(self):
        print("zero")

def IN():
    try:
        print("ok")
        x = 100
        if x != 50:
            print("detatch")
        else:
            print("no")
    except Exception as e:
        raise e
    finally:
        print("Destoroy you watch")
IN()