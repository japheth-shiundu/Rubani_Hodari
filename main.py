from colorama import init
import random
import time

# Importing the run_round functions from respective modules
from round1 import run_round as round1
from round2 import run_round as round2
from round3 import run_round as round3
from round4 import run_round as round4
from round5 import run_round as round5
from round6 import run_round as round6
from round6 import run_round as round7
from round6 import run_round as round8

# Initialize colorama
init()

# List of rounds (excluding Round 1)
rounds = [round2, round3, round4, round5,round6, round7, round8]

# Run Round 1 six times consecutively
for _ in range(6):
    round1()
    print("\n")
    time.sleep(5)

# Randomly select and run other rounds with a 5-second delay between rounds
while True:
    selected_round = random.choice(rounds)  # Randomly select a round
    selected_round()  # Run the selected round
    #print("\n")
    print("Waiting for 5 seconds before the next round...")
    time.sleep(5)  # Pause for 5 seconds





