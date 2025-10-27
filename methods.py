# methods.py
# A simple list of session lengths stored as strings for display.
# When the user pick one, return it as an integer to the caller.

PRESET_STRINGS = ["15", "25", "50", "60", "90"]  # displayed as strings

def choose_mins_presets():
    """Print the preset strings, ask the user to pick one, and return minutes as int."""
    print("Choose a session length:")
    for i, s in enumerate(PRESET_STRINGS, start=1):
        print(f"  {i}) {s}")

    while True:
        choice = input("Select option number: ").strip()
        if choice.isdigit():
            idx = int(choice)
            if 1 <= idx <= len(PRESET_STRINGS):
                # convert the chosen string into int and return
                return int(PRESET_STRINGS[idx - 1])
        print("Please choose a valid option (enter the option number).")