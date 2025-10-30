# timer.py
import time # for the time running
import threading # allow user unput while backround running

class Timer:
    def __init__(self):
        self.paused = False
        self._stop_input_thread = False

    def _input_listener(self):
        while not self._stop_input_thread:
            user_input = input().strip().lower()
            if user_input == 'p':
                self.paused = True
            elif user_input == 'r':
                self.paused = False

    def _render_time(self, mins, secs):
        if self.paused:
            print(f"\r{mins:02d}:{secs:02d}  Paused  ", end="")
        else:
            print(f"\r{mins:02d}:{secs:02d}          ", end="")

    def start(self, minutes):
        """Count down from given minutes to 00:00 ."""
        total_seconds = minutes * 60  # 

        input_thread = threading.Thread(target=self._input_listener, daemon=True)
        input_thread.start()

        print("Controls: Press 'P' + Enter to Pause, 'R' + Enter to Resume")

        while total_seconds >= 0:
            mins, secs = divmod(total_seconds, 60)
            self._render_time(mins, secs)
            if not self.paused:
                time.sleep(0.01)
                total_seconds -= 1
            else:
                time.sleep(0.01)
                continue

        self._stop_input_thread = True
        print("\nDone!")