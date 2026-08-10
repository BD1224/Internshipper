# database helper methods
import sqlite3
from config import DB_PATH, RESET, GREEN

def print_data():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # make list non global of words
    cursor.execute("SELECT * FROM site_words")
    rows = cursor.fetchall()
    words_by_site = {}  # dict with key site_id: value list of words
    for row in rows:
        if row[3] == 0:  # row[3] is the is_global col
            site_id = row[1]
            if site_id not in words_by_site:  # searches keys
                words_by_site[site_id] = []  # adds list if not a key
            words_by_site[site_id].append(row[2]) # appends word to list

    # print data and corresponding words
    cursor.execute("SELECT * FROM sites")
    sites = cursor.fetchall()
    print("\nID   URL" + " " * 30 + "FOUND?  GLOBAL?  WORDS")
    for site in sites:
        if site[2] == 1:
            found_application = "YES"
            color = GREEN
        else:
            found_application = "NO"
            color = RESET
        if site[3] == 1:
            includes_globals = "YES"
        else:
            includes_globals = "NO"
        if site[0] not in words_by_site:
            words_by_site[site[0]] = []  # creates empty list for sites with no words
        print(
            f"{site[0]:<5}"
            f"{site[1][:30]:<33}"
            f"{color}{found_application:<8}{RESET}"
            f"{includes_globals:<9}"
            f"{words_by_site[site[0]]}"
        )
    print()  # prints one newline as its a different print()

    conn.commit()
    conn.close()
            
    return 0

def print_words():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM site_words")
    rows = cursor.fetchall()

    print("\nID   WORD           SITE ID   URL")
    for row in rows:
        if row[3] == 1:  # row[3] is the is_global col
            site_id = "global"
            URL = "-"
        else:
            site_id = row[1]  # row[1] is site_id col
            URL = get_url_from_id(site_id)

        print(f"{row[0]:<5}{row[2]:<15}{site_id:<10}{URL[:30]}")  # did not limit length, may be messy if words are long, but I'd rather display the whole word
    print()  # prints one newline as its a different print()

    conn.commit()
    conn.close()

    return 0

def print_global_words():
    print("\nID   WORD")
    for word in get_global_words():
        print(f"{word[0]:<5}{word[2]}")
    print() # prints one newline as its a different print()

    return 0

def print_non_global_words():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM site_words")
    rows = cursor.fetchall()

    print("\nID   WORD           SITE ID   URL")
    for row in rows:
        if row[3] == 0:  # row[3] is the is_global col
            URL = get_url_from_id(row[1])
            print(f"{row[0]:<5}{row[2]:<15}{row[1]:<10}{URL[:30]}")
    print()  # prints one newline as its a different print()

    conn.commit()
    conn.close()

    return 0

def print_prev():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute(
        "SELECT value FROM settings WHERE key = ?",
        ("prev_print",)
    )
    prev_print = cursor.fetchone()
    print(f"{prev_print[0]}")

    conn.commit()
    conn.close()

    return 0

def print_url_from_id(id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute(
        "SELECT url FROM sites WHERE id = ?",
        (id,)
    )
    url_print = cursor.fetchone()
    if url_print is None:
        print("\nUnable to print\n")
    else:
        print(f"\n{url_print[0]}\n")

    conn.commit()
    conn.close()

    return 0

def get_url_from_id(id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute(
        "SELECT url FROM sites WHERE id = ?",
        (id,)
    )
    url_get = cursor.fetchone()

    conn.commit()
    conn.close()

    if url_get is None:
        return "-"

    return url_get[0]

def get_urls():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM sites WHERE found_application = ?",
        (False,)
    )
    sites = cursor.fetchall()

    conn.commit()
    conn.close()

    return sites

def get_global_words():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM site_words WHERE is_global = ?",
        (True,)
    )
    words = cursor.fetchall()

    conn.commit()
    conn.close()

    return words

def get_words(site_id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM site_words WHERE site_id = ?",
        (site_id,)
    )
    words = cursor.fetchall()

    conn.commit()
    conn.close()

    return words

def add_url(url):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO sites (url, found_application, includes_global_words) VALUES (?, ?, ?)",
        (url, False, True)
    )
    ret = cursor.rowcount  # 1 if success, 0 if did not work

    conn.commit()
    conn.close()

    return ret

def remove_url(site_id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM sites WHERE id = ?",
        (site_id,)
    )  # comma after site_id to make it a tuple
    ret = cursor.rowcount

    conn.commit()
    conn.close()

    return ret

def add_global_word(word):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO site_words (word, is_global) VALUES (?, ?)",
        (word, True)
    )
    ret = cursor.rowcount

    conn.commit()
    conn.close()

    return ret

def remove_global_word(word):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM site_words WHERE word = ? AND is_global = ?",
        (word, True)
    )
    ret = cursor.rowcount

    conn.commit()
    conn.close()

    return ret

def add_word(site_id, word):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO site_words (site_id, word, is_global) VALUES (?, ?, ?)",
        (site_id, word, False)
    )
    ret = cursor.rowcount

    conn.commit()
    conn.close()

    return ret

def remove_word_id(word_id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM site_words WHERE id = ?",
        (word_id,)
    )
    ret = cursor.rowcount

    conn.commit()
    conn.close()

    return ret

def remove_word(word):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM site_words WHERE word = ?",
        (word,)
    )
    ret = cursor.rowcount  # may return more than 1

    conn.commit()
    conn.close()

    return ret

def include_global_words(site_id, bool):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    if bool=="t":
        set_to = True
    elif bool=="f":
        set_to = False
    else:
        return 0
    
    cursor.execute(
        "UPDATE sites SET includes_global_words = ? WHERE id = ?",
        (set_to, site_id)
    )
    ret = cursor.rowcount

    conn.commit()
    conn.close()

    return ret

def found_application(URL):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE sites SET found_application = ? WHERE url = ?",
        (True, URL)
    )

    conn.commit()
    conn.close()

    return 0

def update_prev_print(prev_print):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE settings SET value = ? WHERE key = ?",
        (prev_print, "prev_print")
    )

    conn.commit()
    conn.close()

    return 0

def delete_all():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("DELETE FROM sites")
    cursor.execute("DELETE FROM site_words")

    conn.commit()
    conn.close()

    return 0