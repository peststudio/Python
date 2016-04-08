import random
from scipy import stats
import numpy as np
import sys
def run_exp(total_wealth, player1_init_wealth, prob_1):
    count = 0
    player1_wealth = player1_init_wealth
    R = get_random(prob_1)
    temp_count = count
    while player1_wealth != 0 and player1_wealth != total_wealth:
        step = R[temp_count]
        count += 1
        temp_count += 1
        if temp_count >= 10000:
            temp_count -= 10000
            R = get_random(prob_1)
        if step == 0:
            player1_wealth += 1
        else:
            player1_wealth -= 1

    if player1_wealth == 0:
        print("Player 2 wins in",count,"steps")
    else:
        print("Player 1 wins in",count,"steps")

def get_random(prob_1):
    prob_2 = 1 - prob_1
    xk = np.arange(2)
    xp = (prob_1,prob_2)
    custom = stats.rv_discrete(name='custm', values=(xk, xp))
    random_size = 10000
    R = custom.rvs(size=random_size)
    return R
 
if __name__ == '__main__':
    try:
        total_wealth = int(sys.argv[1])
        player1_init_wealth = int(sys.argv[2])
        prob_1 = float(sys.argv[3])
    except ValueError:
        print("Please provide total Wealth, Player 1 initial wealth and player win probablity")
        sys.exit()
    if total_wealth < player1_init_wealth:
        print('Total Wealth can not be less than player 1 initial wealth')
    elif prob_1 < 0 or prob_1 > 1:
        print('Player 1 winning probability must be between 0 and 1')
    else:
        run_exp(total_wealth,player1_init_wealth,prob_1)
