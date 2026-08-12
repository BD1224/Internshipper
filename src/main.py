from cli.display import display
from scraper.provide_status import provide_status
from config import SCRAPING_FREQUENCY
import threading
import readline  # even though no code is written with this, it still controls input(), so keys like ^R dont print or interfere

def run_status(stop_flag, recent_print_flag, lock):  # flag is pass by reference
    wait_time = 3  # SCRAPING_FREQUENCY*60*60
    stop_flag.wait(wait_time)  # like sleep, but gets woken when flag is changed

    while not stop_flag.is_set():  # is_set return if the flag is True/False
        with lock:  # handles .aquire() and .release() and errors
            recent_print_flag.set()  # tells other thread there was a recent print
            print()
            provide_status()
            print("Press enter to continue ", end="", flush=True)  # prints this after the status, to avoid saved input buffer
        stop_flag.wait(wait_time)
    return 0

def main():
    stop_flag = threading.Event()  # communication between threads (default value is False)
    recent_print_flag = threading.Event()
    lock = threading.Lock()  # used to avoid clashes when outputting

    scrape_thread = threading.Thread(target=run_status, args=(stop_flag, recent_print_flag, lock))  # define thread
    scrape_thread.start()  # run thread

    display(recent_print_flag, lock) # on main thread run cli display. Will run until user types 'close'

    stop_flag.set()  # sets flag to True/tells thread to stop
    scrape_thread.join()  # waits for thread to return

    return 0

if __name__ == "__main__":
    main()


