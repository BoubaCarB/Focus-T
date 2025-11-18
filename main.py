# main.py

from timer import Timer
from methods import choose_mins_presets

def get_minutes():
    print("Choose mode:")
    print("  1) Choose from presets")
    print("  2) Type your own number")
    while True:
        mode = input("Select 1 or 2: ").strip()
        if mode == "1":
            return choose_mins_presets()
        if mode == "2":
            while True:
                raw = input("Enter mins: ").strip()
                if raw.isdigit() :
                    return int(raw)
                print("Positive whole number.")
        print(" Enter 1 or 2.")

def main():
    print("=== FocusT — Timer ===")
    minutes = get_minutes()
    t = Timer()
    t.start(minutes)

if __name__ == "__main__":
    main()