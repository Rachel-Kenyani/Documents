class Looting:
    def __init__(self,draft,crew):
        self.draft=draft
        self.crew=crew
    def is_worth_it(self):
        people_weight=self.crew*1.5
        ship_weight=self.draft-people_weight
        if ship_weight>20:
            return "The Ship  is worth a try."
        else:
            return "The Ship has little gold."
        
titanic=Looting(40,5)
print(titanic.is_worth_it())

titanic2=Looting(25,5)
print(titanic2.is_worth_it())


# You're running an online business and a big part of your day is fulfilling orders. As your volume picks up 
# that's been taking more of your time, and unfortunately lately you've been running into situations where you 
# take an order but can't fulfill it.You've decided to write a function fillable() that takes three arguments: 
# //a dictionary stock representing all the merchandise you have in stock, a string merch representing the thing
# // your customer wants to buy, and an integer n representing the number of units of merch they would like to buy. 
# //Your function should return True if you have the merchandise in stock to complete the sale, otherwise it should 
# //return False.Valid data will always be passed in and n will always be >= 1.
class Shop:
    def __init__(self, stock):
        self.stock = stock

    def fillable(self, item, n):
        if item in self.stock.keys() and self.stock[item] >= n:
            print(True) 
        else:
            print(False) 

shop1 = Shop({"Cabbages": 4, "Phones": 45, "Sweets": 5, "Pens": 7})
shop1.fillable("Pencils", 8)