
from sueca_suits_ranks import valid_rank
from sueca_suits_ranks import valid_suit
from sueca_suits_ranks import rank_points
from sueca_suits_ranks import rank_higher_than





class CardInvalid(ValueError):
    pass


def parseCard(cs):      
    if valid_rank(cs[0]) and valid_suit(cs[1]) == True and len(cs) == 2:
        return Card(cs[0] + cs[1])
    else:
        raise CardInvalid ("Card '%s' is Invalid!" %cs)





        

class Card:
    def __init__(self,rs):
        self.rs = rs
    def show(self):
        return self.rs
    def points(self):
        if len(self.rs) == 2:
            return rank_points(self.rs[0])    
    def higher_than(self,other,s,t):
        r1 = self.show()
        r2 = other
        if r1[1] == r2.show()[1]:
            return rank_higher_than(r1, r2.show())
        else:
            if t == r1[1] :
                return True
            elif t == r2.show()[1]:
                return False
            elif s == r1[1] :
                return True
            elif s == r2.show()[1]:
                return False
    




    
            
            
    