import random
from scipy import stats
import numpy as np
import sys
random_size = 10000
class RandomBinomialProb:
    import numpy as np
    def __init__(self,prob1):
        self.prob1 = prob1
        self.R = []

    def get_number(self):
        if len(self.R) == 0:
            self.generate()
        num = self.R[0]
        self.R = np.delete(self.R,0)
        return num
    
    def generate(self):
        n, p = 1, self.prob1
        self.R = np.random.binomial(n, p, 10000)


def run_exp(total_wealth, player1_init_wealth, prob_1,total_no_games,show):
    player1_total_win = 0
    random_prob = RandomBinomialProb(prob_1) 
    for i in range(0,total_no_games):
        count = 0
        player1_wealth = player1_init_wealth
        while player1_wealth != 0 and player1_wealth != total_wealth:
            count += 1
            step = random_prob.get_number()
            if step == 1:
                player1_wealth += 1
            else:
                player1_wealth -= 1

        if player1_wealth == 0:
            if show == True:
                print("Player 2 wins in",count,"steps")
            else:
                pass
        else:
            if show == True:
                print("Player 1 wins in",count,"steps")
            player1_total_win += 1
    print("Player 1 wins",player1_total_win,"Rounds in",total_no_games, "games")
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description="Simulation of Gambler's Rurn Game")
    parser.add_argument("total_wealth", help="Total Wealth of two players", type = int)
    parser.add_argument("player1_init_wealth", help="Player 1 initial wealth", type = int)
    parser.add_argument("prob_1", help="Player 1's winning probablity for each game", type = float)
    parser.add_argument("total_no_games", help="Total Number of Games", type = int)
    parser.add_argument("--show", help="Show each game",type = bool)
    args = parser.parse_args()
     
    if args.total_wealth < args.player1_init_wealth:
        print('Total Wealth can not be less than player 1 initial wealth')
    elif args.prob_1 < 0 or args.prob_1 > 1:
        print('Player 1 winning probability must be between 0 and 1')
    else:
        run_exp(args.total_wealth,args.player1_init_wealth,args.prob_1,args.total_no_games,args.show)
