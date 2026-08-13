from cli.display import display
from scraper.provide_status import provide_status
from database.database import get_status, get_time
from config import SCRAPING_FREQUENCY
from prompt_toolkit.patch_stdout import patch_stdout
import threading
import readline  # even though no code is written with this, it still controls input(), so keys like ^R dont print or interfere

def run_status(stop_flag, status_on_flag, lock):  # flag is pass by reference
    wait_time = 3  # SCRAPING_FREQUENCY*60*60
    stop_flag.wait(wait_time)  # like sleep, but gets woken when flag is changed

    while not stop_flag.is_set():  # is_set return if the flag is True/False
        if status_on_flag.is_set():  # status is not turned on
            with lock:  # handles .aquire() and .release() and errors
                provide_status()
            stop_flag.wait(wait_time)
        else:  # status is not set
            status_on_flag.wait()  # waits for user to type 'status on' to start running the status again
    return 0

def main():
    stop_flag = threading.Event()  # communication between threads (default value is False)
    status_on_flag = threading.Event()  # if user wants periodic status updates
    if get_status() == "on":
        status_on_flag.set()
    print(f"{get_status()}")
    lock = threading.Lock()  # makes sure the multiple print statements are run correctly (std_patch avoids clashes)

    scrape_thread = threading.Thread(target=run_status, args=(stop_flag, status_on_flag, lock))  # define thread
    scrape_thread.start()  # run thread

    with patch_stdout():  # manages locks, avoids clashes
        display(status_on_flag, lock) # on main thread run cli display. Will run until user types 'close'

    stop_flag.set()  # sets flag to True/tells thread to stop
    status_on_flag.set()  # set so that run_status doesnt wait forever
    scrape_thread.join()  # waits for thread to return

    return 0

if __name__ == "__main__":
    main()


