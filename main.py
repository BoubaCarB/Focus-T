# main.py (small change)
from timer import FocusTimer
from methods import choose_minutes_from_presets  # add this import

def main():
    print("=== FocusTrack — Timer ===")
    minutes = choose_minutes_from_presets()   # get an int back
    t = FocusTimer()
    t.start(minutes)

if __name__ == "__main__":
    main()