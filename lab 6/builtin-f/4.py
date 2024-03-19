import time
import math

def delayed_sqrt(n, ms):
    time.sleep(ms / 1000)
    result = math.sqrt(n)
    print(f"Square root of {n} after {ms} milliseconds is {result}")

def main():
    number = int(input())
    milliseconds = int(input("Enter milliseconds to wait: "))
    delayed_sqrt(number, milliseconds)

main()
