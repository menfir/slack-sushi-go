class Card:

    def __init__(self, name):
        self.name = name

    def myprint(self):
        print self.name
    
    def __str__(self):
        return self.name
    
    def isPudding(self):
        return self.name =="pudding"