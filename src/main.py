from cli.display import display
from scraper.provide_status import provide_status
from config import SCRAPING_FREQUENCY
import threading

def run_status(flag):  # flag is pass by reference
    wait_time = 3  # SCRAPING_FREQUENCY*60*60
    flag.wait(wait_time)  # like sleep, but gets woken when flag is changed

    while not flag.is_set():  # is_set return if the flag is True/False
        print("")
        provide_status()
        print(">> ", end="", flush=True)  # prints this after the status, because the cli doesnt reprint
        flag.wait(wait_time)
    return 0

def main():
    flag = threading.Event()  # communication between threads (default value is False)

    scrape_thread = threading.Thread(target=run_status, args=(flag,))  # define thread
    scrape_thread.start()  # run thread

    display() # on main thread run cli display. Will run until user types 'close'

    flag.set()  # sets flag to True/tells thread to stop
    flag.join()  # waits for thread to return

    return 0

if __name__ == "__main__":
    main()


