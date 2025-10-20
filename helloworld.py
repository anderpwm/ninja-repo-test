import time
import sys

def stealth_print(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.05)
    print()

stealth_print("Ninja deployment: Hello World!")
