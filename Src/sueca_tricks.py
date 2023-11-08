# -*- coding: utf-8 -*-
from sueca_cards import parseCard
from sueca_suits_ranks import rank_points






    
class Trick:
    def __init__(self,rs):
        self.rs = rs
    def points(self):
            return  parseCard(self.rs[0]+self.rs[1]).points() + parseCard(self.rs[3]+self.rs[4]).points() + parseCard(self.rs[6]+self.rs[7]).points() + parseCard(self.rs[9]+self.rs[10]).points()
    def trick_winner(self,t):
        s = []
        s.append(self.rs[0]  + self.rs[1])
        s.append(self.rs[3]  + self.rs[4])
        s.append(self.rs[6]  + self.rs[7])
        s.append(self.rs[9]  + self.rs[10])
        if t in self.rs:
            v = []
            j = []
            if t == self.rs[1]:
                v.append(self.rs[0] + self.rs[1])
            if t == self.rs[4]:
                v.append(self.rs[3] + self.rs[4])
            if t == self.rs[7]:
                v.append(self.rs[6] + self.rs[7])
            if t == self.rs[10]:
                v.append(self.rs[9] + self.rs[10])
            for i in v:
                j.append(rank_points(i[0]))
            x = max(j)
            y = j.index(x)
            z = v[y]
            return s.index(z) + 1
        else:
            v = []
            z = []
            b = 0
            for i in s:
                if self.rs[1] == i[1]:
                    v.append(i)
            for i in v:
                z.append(rank_points(i[0]))
            for i in z:
                b += i
            if b != 0:
                x = max(z)
                y = z.index(x)
                u = v[y]
                return s.index(u) + 1
            else:
                v.sort()
                v.reverse()
                return s.index(v[0]) + 1
    def show(self):
        return self.rs




        
   







def parseTrick(ts):
    s = 0
    for i in ts:
        if i == " ":
            s+= 1
    if s == 3:
        crd1 = ts[0] + ts[1]
        if ts[2] == " ":
            crd2 = ts[3] + ts[4]
        else:
            crd2 = ts[4] + ts[5]
        if ts[5] == " ":
            crd3 = ts[6] + ts[7]
        elif ts[7] == " ":
            crd3 = ts[8] + ts[9]
        else:
            crd3 = ts[7] + ts[8]
        if ts[8] == " " :
            crd4 = ts[9] + ts[10]
        elif ts[9] == " " :
            crd4 = ts[10] + ts[11]
        elif ts[10] == " " :
            crd4 = ts[11] + ts[12]
        elif ts[11] == " " :
            crd4 = ts[12] + ts[13]
        if ts[2] != " ":
            raise parseCard(ts[0]+ts[1]+ts[2])
        if ts[5] != " ":
            raise parseCard(ts[3]+ts[4]+ts[5])
        if ts[8] != " ":
            raise parseCard(ts[6]+ts[7]+ts[8])
        if ts[-3] != " ":
            raise parseCard(ts[-3]+ts[-2]+ts[-1])

        return Trick('%s %s %s %s'%(parseCard(crd1).show() , parseCard(crd2).show(), parseCard(crd3).show(),parseCard(crd4).show()))
    
    else:
        raise ValueError ('A trick string must comprise four cards only; the given trick is : %s' %ts)



 
def parseGameFile(fname):
    try:
        import os 
        file_path = os.path.join(os.getcwd(),fname)
        y = open(file_path,'r')
        z = y.readlines() 
        y.close()
    except FileNotFoundError:
        raise FileNotFoundError("Could not find the file '%s'" %fname)
    if len(z) < 11:
        raise ValueError("Game file '%s' is incomplete. A complete game takes 10 rounds; the given game includes %s rounds only  "%(fname,len(z)-1))
    
    m = []
    a = []
    for i in z[0]:
        a.append(i)
    del a[-1]
    u = ''.join(a)
    k = parseCard(u)
    p = 1
        
    while p < 10:
        b = []
        for i in z[p]:
            b.append(i)
        del b[-1]
        u = ''.join(b)
        m.append(parseTrick(u))
        p+=1
        
    if len(z[10]) == 11:
        b = []
        for i in z[p]:
            b.append(i)
        u = ''.join(b)
        m.append(parseTrick(u))
        p+=1
    else:
        b = []
        for i in z[p]:
            b.append(i)
        del b[-1]
        u = ''.join(b)
        m.append(parseTrick(u))
        p+=1
        
    

    

   

    

   
   
    
        
    
    
    
    
    
    
    
