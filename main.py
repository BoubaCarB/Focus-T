# main

from timer import FocusTimer


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
        print("Please enter 1 or 2.")

def main():
    print("=== FocusTrack — Timer ===")
    minutes = get_minutes()
    t = FocusTimer()
    t.start(minutes)

if __name__ == "__main__":
    main()