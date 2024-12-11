import time
from datetime import datetime, timedelta
import os
import pyfiglet

try:
    while True:
        now = datetime.now()
        current_time = now.strftime("%H : %M : %S")
        ascii_art = pyfiglet.figlet_format(current_time)
        os.system('cls' if os.name == 'nt' else 'clear')
        print(ascii_art)
        
        # 다음 초까지 더 정확한 대기 시간 계산
        next_second = (now + timedelta(seconds=1)).replace(microsecond=0)
        sleep_seconds = (next_second - datetime.now()).total_seconds()
        if sleep_seconds > 0:
            time.sleep(sleep_seconds)
except KeyboardInterrupt:
    print("\nExit the program...")
