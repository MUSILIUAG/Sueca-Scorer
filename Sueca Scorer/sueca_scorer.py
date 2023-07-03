from sueca_tricks import parseGameFile
from sueca_games import Game
from sueca_suits_ranks import suit_full_name


import sys

def runGame(fname,showCards = False,showGame = False ):
    tc, ts = parseGameFile(fname)
    g = Game(tc)
    for t in ts[:]:
        g.playTrick(t)
    if showCards == showGame == False:
        if g.pair1 > g.pair2:
            print( 'Pair A won the given sueca game')
        elif g.pair1 == g.pair2:
            print('The game resulted in a draw')
        else:
            print( 'Pair B won the given sueca game')
        print( 'Score: %d | %d' %(g.pair1,g.pair2) ) 
    
    if showCards == True:
       a = ", ".join(g.p1)
       b = ", ".join(g.p2)
       c = ", ".join(g.p3)
       d = ", ".join(g.p4)
       if g.pair1 > g.pair2:
           print( 'Pair A won the given sueca game')
       elif g.pair1 == g.pair2:
           print('The game resulted in a draw')
       else:
           print( 'Pair B won the given sueca game')
       print( 'Score: %d | %d' %(g.pair1,g.pair2) ) 
       print("Player's cards in the sueca game")
       print('Player 1 :%s'%a)
       print('Player 2 :%s'%b)
       print('Player 3 :%s'%c)
       print('Player 4 :%s'%d)
    if showGame == True:
       if g.pair1 > g.pair2:
           print( 'Pair A won the given sueca game')
       elif g.pair1 == g.pair2:
           print('The game resulted in a draw')
       else:
           print( 'Pair B won the given sueca game')
       print( 'Score: %d | %d' %(g.pair1,g.pair2) )
       print('%s - %s'%(g.gameTrump().show(),suit_full_name(g.gameTrump().show()[1])))
       print('1: %s'% ts[0].show())
       print('2: %s'% ts[1].show())
       print('3: %s'% ts[2].show())
       print('4: %s'% ts[3].show())
       print('5: %s'% ts[4].show())
       print('6: %s'% ts[5].show())
       print('7: %s'% ts[6].show())
       print('8: %s'% ts[7].show())
       print('9: %s'% ts[8].show())
       print('10: %s'% ts[9].show())


if sys.argv[1] == "-c":
     runGame(sys.argv[2], showCards = True)
elif sys.argv[1] == "-g":
     runGame(sys.argv[2], showGame = True)
elif len(sys.argv[1]) > 2:   
     runGame(sys.argv[1])
else:
    raise ValueError('''
                     invalid option %s
                     Usage: python sueca_scorer.py [-c | -g] <game_file>
                     ''' %sys.argv[1])
    
    


    
    