class Assite(object):
    def wget(self):
        self.game()
        
    def game(self):
        print("ok")
        
class S(Assite):
    def game(self):
        print("user command")

if __name__ == "__main__":
    assite = Assite()
    assite.wget()
    s = S()
    s.wget()

print("*******************") #comentout_messagebar
