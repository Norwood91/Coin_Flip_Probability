import matplotlib.pyplot as plt
import numpy as np

def flip_coins():
    coin1= ['Heads', 'Tails']
    coin2= ['Heads', 'Tails']

    coin1_result = np.random.choice(coin1)
    coin2_result = np.random.choice(coin2)

    if coin1_result == 'Heads' and coin2_result == 'Heads':
        return 1
    else:
        return 0
# How many times we run the experiment
number_of_trials = 1000
prop = []
flips = []

# Keep track of the number of times both coins are heads during the same flip
both_coins_are_heads = 0
for flip in range(number_of_trials):
    # If both coins are heads, add 1 to the counter
    both_coins_are_heads += flip_coins()
    # Keep track of the proportion of two heads at each flip
    prop.append(both_coins_are_heads / (flip + 1))
    # Keep a list for number of flips
    flips.append(flip + 1)

plt.plot(flips, prop, label='Experimental Probability')
plt.xlabel('Number of Flips')
plt.ylabel('Proportion of Two Heads')

plt.hlines(0.25, 0, number_of_trials, colors='orange', label='True Probability')
plt.legend()
plt.show()


