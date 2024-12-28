import time
import random

def mix_codes(codes):
    
    mixed = ''.join(random.sample(codes, len(codes)))
    return mixed

def main():
    
    user_input = input("Please enter your codes (comma separated): ")
    codes = user_input.split(',')

    print("Mixing codes...")
    time.sleep(3)

    mixed_code = mix_codes(codes)
    print(f"Your mixed code: {mixed_code}")

    
    link = f"http://FILTER.RUBIKA/mixed_code/{mixed_code}"
    print(f"Mixed code link: {link}")

if __name__ == "__main__":
    main()
