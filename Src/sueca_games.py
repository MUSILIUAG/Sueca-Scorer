from sueca_cards import parseCard
from sueca_tricks import parseGameFile


class Game:
    def __init__(self,gf):
        self.gf = gf 
        self.pair1 = 0
        self.pair2 = 0
        self.arrangement = [1]
        self.z = 0
        self.p = 0
        self.p1 = []
        self.p2 = []
        self.p3 = []
        self.p4 = []
        self.deck = ['AH', 'AC', 'AS', 'AD', '7H', '7C', '7S', '7D', 'KH', 'KC', 'KS', 'KD', 
         'JH', 'JC', 'JS', 'JD', 'QH', 'QC', 'QS', 'QD', '6H', '6C', '6S', '6D', 
         '5H', '5C', '5S', '5D', '4H', '4C', '4S', '4D', '3H', '3C', '3S', '3D', 
         '2H', '2C', '2S', '2D']
        self.round = 1
        
        
        
        
        
    def gameTrump(self):
        return self.gf
    def pair1(self):
        return self.pair1
    def pair2(self):
        return self.pair2
    def score(self):
        return (self.pair1,self.pair2)
    def p1(self):
        return self.p1
    def p2(self):
        return self.p2
    def p3(self):
        return self.p3
    def p4(self):
        return self.p4
    
    
    
    
    def playTrick(self,t):
        try:
            a = [t.show()[0] + t.show()[1], t.show()[3] + t.show()[4], t.show()[6] + t.show()[7],t.show()[9] + t.show()[10] ]
            for i in a:
                if i in self.deck:
                    self.deck.remove(i)
                else:
                    raise ValueError 
        except ValueError:
            raise ValueError (' The game is invalid Card %s of round %d has already been played'%(i,self.round))
            
        
        y = t.trick_winner(self.gf.show()[1])
        if self.arrangement[self.p] == 1:
            arrangement = [1,2,3,4]
        elif self.arrangement[self.p] == 2:
            arrangement = [2,3,4,1]
        elif self.arrangement[self.p] == 3:
            arrangement = [3,4,1,2]
        elif self.arrangement[self.p] == 4:
            arrangement = [4,1,2,3]
        self.p += 1   
        self.arrangement.append(arrangement[y-1])
        if self.arrangement[self.p] == 1:
           self.pair1 += t.points()
        if self.arrangement[self.p] == 2:
           self.pair2 += t.points()
        if self.arrangement[self.p] == 3:
           self.pair1 += t.points()
        if self.arrangement[self.p] == 4:
           self.pair2 += t.points()
        
        z =[ts[self.z].show()[0] + ts[self.z].show()[1],ts[self.z].show()[3] + ts[self.z].show()[4],ts[self.z].show()[6] + ts[self.z].show()[7],
            ts[self.z].show()[9] + ts[self.z].show()[10]]   
        self.z += 1
        for i in arrangement:
            if i == 1 :
                h = arrangement.index(i)
                self.p1.append(z[h])
            if i == 2 :
                h = arrangement.index(i)
                self.p2.append(z[h])
            if i == 3 :
                h = arrangement.index(i)
                self.p3.append(z[h])
            if i == 4 :
                h = arrangement.index(i)
                self.p4.append(z[h])
        self.round += 1
            



    def cardsOf(self,p):
        if p > 4:
            raise ValueError ('Player number is invalid')
        elif p == 1 : 
            y = [parseCard(ts[0].show()[0] + ts[0].show()[1]), parseCard(ts[1].show()[0] + ts[1].show()[1]) 
                 , parseCard(ts[2].show()[0] + ts[2].show()[1]), parseCard(ts[3].show()[0] + ts[3].show()[1])
                 , parseCard(ts[4].show()[0] + ts[4].show()[1]), parseCard(ts[5].show()[0] + ts[5].show()[1])
                 , parseCard(ts[6].show()[0] + ts[6].show()[1]), parseCard(ts[7].show()[0] + ts[7].show()[1])
                 , parseCard(ts[8].show()[0] + ts[8].show()[1]), parseCard(ts[9].show()[0] + ts[9].show()[1])]
            return y
        elif p == 2 : 
            y = [parseCard(ts[0].show()[3] + ts[0].show()[4]), parseCard(ts[1].show()[3] + ts[1].show()[4]) 
                 , parseCard(ts[2].show()[3] + ts[2].show()[4]), parseCard(ts[3].show()[3] + ts[3].show()[4])
                 , parseCard(ts[4].show()[3] + ts[4].show()[4]), parseCard(ts[5].show()[3] + ts[5].show()[4])
                 , parseCard(ts[6].show()[3] + ts[6].show()[4]), parseCard(ts[7].show()[3] + ts[7].show()[4])
                 , parseCard(ts[8].show()[3] + ts[8].show()[4]), parseCard(ts[9].show()[3] + ts[9].show()[4])]
            return y
        elif p == 3 : 
            y = [parseCard(ts[0].show()[6] + ts[0].show()[7]), parseCard(ts[1].show()[6] + ts[1].show()[7]) 
                 , parseCard(ts[2].show()[6] + ts[2].show()[7]), parseCard(ts[3].show()[6] + ts[3].show()[7])
                 , parseCard(ts[4].show()[6] + ts[4].show()[7]), parseCard(ts[5].show()[6] + ts[5].show()[7])
                 , parseCard(ts[6].show()[6] + ts[6].show()[7]), parseCard(ts[7].show()[6] + ts[7].show()[7])
                 , parseCard(ts[8].show()[6] + ts[8].show()[7]), parseCard(ts[9].show()[6] + ts[9].show()[7])]
            return y
        elif p == 4 : 
            y = [parseCard(ts[0].show()[9] + ts[0].show()[10]), parseCard(ts[1].show()[9] + ts[1].show()[10]) 
                 , parseCard(ts[2].show()[9] + ts[2].show()[10]), parseCard(ts[3].show()[9] + ts[3].show()[10])
                 , parseCard(ts[4].show()[9] + ts[4].show()[10]), parseCard(ts[5].show()[9] + ts[5].show()[10])
                 , parseCard(ts[6].show()[9] + ts[6].show()[10]), parseCard(ts[7].show()[9] + ts[7].show()[10])
                 , parseCard(ts[8].show()[9] + ts[8].show()[10]), parseCard(ts[9].show()[9] + ts[9].show()[10])]
            return y
    def gameTricks(self):
            return ts
        



try:
 tc, ts = parseGameFile('game1.sueca')
except FileNotFoundError:
    pass



