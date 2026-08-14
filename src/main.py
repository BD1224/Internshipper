from cli.display import display
from scraper.provide_status import provide_status
from database.database import get_status, get_time
from prompt_toolkit.patch_stdout import patch_stdout
import threading
from datetime import datetime, timedelta

def get_next_call_time(last_call_time): 
    target_hour = int(get_time())  # get time will return a string(text) but it will always be a valid number
    next_call_time = last_call_time.replace(hour=target_hour, minute=0, second=0, microsecond=0)
    if next_call_time <= last_call_time:  # if next target_hour is in the next day, shift target time to next day
        next_call_time += timedelta(days=1)  # timedelta is needed to add times

    return next_call_time

def run_status(stop_flag, status_on_flag, new_time_flag, lock):  # flag is pass by reference
    next_call_time = get_next_call_time(datetime.now())

    while not stop_flag.is_set():  # is_set return if the flag is True/False
        if status_on_flag.is_set():  # status is not turned on
            now = datetime.now()

            if now >= next_call_time:
                with lock:  # handles .aquire() and .release() and errors
                    provide_status()
                next_call_time = get_next_call_time(now)
            else:
                stop_flag.wait(10)  # every 10 seconds it checks
                if new_time_flag.is_set():  # if user set a new time
                    next_call_time = get_next_call_time(now)
                    new_time_flag.clear()
        else:  # status is not set
            status_on_flag.wait()  # waits for user to type 'status on' to start running the status again
    return 0

def main():
    stop_flag = threading.Event()  # communication between threads (default value is False)
    status_on_flag = threading.Event()  # if user wants periodic status updates
    new_time_flag = threading.Event()  # if user changes status time
    if get_status() == "on":
        status_on_flag.set()

    lock = threading.Lock()  # makes sure the multiple print statements are run correctly (std_patch avoids clashes)

    scrape_thread = threading.Thread(target=run_status, args=(stop_flag, status_on_flag, new_time_flag, lock))  # define thread
    scrape_thread.start()  # run thread

    with patch_stdout():  # manages locks, avoids clashes, and keeps input clean
        display(status_on_flag, new_time_flag, lock) # on main thread run cli display. Will run until user types 'close'

    stop_flag.set()  # sets flag to True/tells thread to stop
    status_on_flag.set()  # set so that run_status doesnt wait forever
    scrape_thread.join()  # waits for thread to return

    return 0

if __name__ == "__main__":
    main()


