from colorama import Fore, Style
import random
import time

def run_round():
    terminate_at = round(random.uniform(1.50, 5.00), 2)
    current_number = 1.00
    while current_number <= terminate_at:
        print(Fore.WHITE + f"\rCounting: {current_number:.2f}", end="", flush=True)
        time.sleep(0.1)
        current_number += 0.01
    print(Fore.MAGENTA + f"\rTerminated at {current_number:.2f}""x" + Style.RESET_ALL)


