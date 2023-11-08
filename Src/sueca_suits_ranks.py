# -*- coding: utf-8 -*-


suits = ['H','C','S','D']
ranks = ['2','3','4','5','6','Q','J','K','7','A']


def valid_suit(s):
    if s in suits: 
        return True
    else:
        return False



def valid_rank(r):
    if r in ranks: 
        return True
    else:
        return False



def suit_full_name(s):
    if s == 'H' :
        return 'Hearts'
    elif s == 'C' :
        return 'Clubs'
    elif s == 'S' :
        return 'Spades'
    elif s == 'D' :
        return 'Diamonds'
    else:
        raise ValueError('Invalid suit symbol %s' %s )
    
    
    
def rank_points(r):
    if r == 'A' :
        return 11
    elif r == '7' :
        return 10
    elif r == 'K' :
        return 4
    elif r == 'J' :
        return 3
    elif r == 'Q' :
        return 2
    elif r == '6' :
        return 0
    elif r == '5' :
        return 0
    elif r == '4' :
        return 0
    elif r == '3' :
        return 0
    elif r == '2' :
        return 0
    else:
        raise ValueError('Invalid rank symbol %s' %r )
    
    
    
def rank_higher_than(r1,r2):
        if valid_rank(r1[0]) == False: 
            raise ValueError('Invalid rank symbol: %s' %r1[0])
        if valid_rank(r2[0]) == False:
            raise ValueError('Invalid rank symbol: %s' %r2[0])
        if ranks.index(r1[0]) > ranks.index(r2[0]):
            return True
        else:
            return False 
  
   
      
        


