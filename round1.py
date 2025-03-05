from colorama import Fore, Style
import random
import time
import os

def clear_screen():
    # Use 'cls' for Windows and 'clear' for Unix-based systems
    os.system('cls' if os.name == 'nt' else 'clear')

def run_round():
    terminate_at = round(random.uniform(1.00, 1.29), 2)
    current_number = 1.00

    # Counting loop with white-colored output
    while current_number <= terminate_at:
        print(Fore.WHITE + f"\rCounting: {current_number:.2f}", end="", flush=True)
        time.sleep(0.1)  # Sleep for 0.1 seconds to simulate counting
        current_number += 0.01  # Increment by 0.01

    # Print the final number in blue
    print(Style.RESET_ALL, end="")  # Reset any previous styles
    print(Fore.BLUE + f"\rTerminated at: {current_number:.2f}""x" + Style.RESET_ALL)
    
    
    time.sleep(2)
    clear_screen()   
