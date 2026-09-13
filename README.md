# The Internshipper

The Internshipper is a local command-line tool that monitors company career pages for internships and other job openings. You provide the career-page URLs and the words or phrases you want to look for, and the program periodically checks those pages for matches.

The goal is to avoid repeatedly checking dozens of company career pages manually.

## Getting Started

First, clone this repository and open a terminal in its folder:

```
git clone <this-repository-url>
cd internshipper
```

There are two ways to run The Internshipper. Pick whichever is easier for you — both use the same `data/` folder, so your tracked URLs and words are shared between them.

### Option 1: Run it directly on your computer (macOS or Linux)

This requires Python (version 3.11 or newer) and `bash` already installed, which is why this option is macOS/Linux only. If you're on Windows, use Option 2 below instead.

The first time only, set everything up:

```
source setup
```

This creates an isolated Python environment, installs the required packages, downloads the browser The Internshipper needs, and sets up the database.

Every time after that, just run:

```
source run-local
```

Once it's running, you'll notice `(venv)` at the start of your terminal prompt — that just means the isolated Python environment is active. If you want to get rid of it after you're done, type `deactivate`.

### Option 2: Run it in a container (macOS, Linux, or Windows)

This requires [Podman](https://podman.io/) and `podman-compose` installed, but does **not** require Python — everything runs inside the container instead. If you're on macOS or Windows, you'll also need a running Podman machine (one-time setup: `podman machine init`, then `podman machine start` before each session).

Every time you want to run the app:

```
source run-podman
```

There's no separate setup step for this option — the first run takes a little longer while it downloads what it needs, and every run after that is fast. You'll see some extra setup text scroll by each time you run it — that's just the container installing things inside itself, not on your computer, so there's nothing to worry about there.

The container defaults to the `America/New_York` timezone, which affects when the daily status check runs. If you're in a different timezone, open `podman-compose.yml` and change the `TZ=America/New_York` line to your own timezone (e.g. `TZ=America/Los_Angeles`, `TZ=Europe/London`). This has to be set manually rather than detected automatically because Podman runs containers inside its own internal VM, which doesn't reliably share your computer's actual timezone.

### Closing the app

Whichever option you use, type `close` inside the app to stop it safely. Your tracked URLs and words are saved to a file on your computer either way, so closing the app — or restarting your computer — never loses your data, regardless of whether you last ran it locally or in a container.

## How It Works

For each company you want to track:

1. Go to the company’s careers page.
2. Search for the type of position you are interested in.
3. Copy the resulting search-page URL.
4. Add that URL to The Internshipper.
5. Add one or more words or phrases that describe the jobs you want the program to find.

The program checks the page for the words or phrases you provide and reports a match if it finds at least one of them. It does not require every tracked word or phrase to appear on the page.

## Finding the Right URL

Whenever possible, use the URL produced by the company’s own career search.

For example, if you are looking for internships, search the company’s career site for:

intern

You can also include a location in the company’s search if you only want positions in a particular area.

For example:

intern Boston

Then copy the resulting URL and add it to The Internshipper. Then, in The Internshipper, add a word or phrase such as analyst, software, or another term that describes the specific internship you want. The program will check that internship results page for the term you provide and report when it finds a matching position.

## Searching for Broader Job Categories

For broader job categories, it can be useful to search for only part of the job title on the company’s career site.

For example, instead of searching:

software developer

search:

software develop

This allows the company’s search engine to return variations such as:

Software Developer
Software Development Intern
Software Development Engineer

However, the word tracked by The Internshipper should usually be the finished job title or phrase, such as:

software developer

rather than:

software develop

This helps prevent false matches caused by the partial search term appearing elsewhere on the webpage, including in the search box itself.

In other words:

Career-site search: software develop
Tracked word:       software developer

Use the broad search to make the career page return more possible jobs, and use the more specific tracked phrase to decide whether an actual job you care about appears.

## Tracking Phrases

Words do not have to be a single word. Put text inside quotation marks ("") when you want it treated as one phrase in a command.

For example:

word add 1 "software developer"

This allows you to track specific job titles or more precise job categories rather than only individual words.

Other examples include:

"investment banking"
"summer analyst"
"software engineer"
"wealth management"

Using phrases is especially useful when a single word would produce too many unrelated matches.

## Global and Non-Global Words

A global word is searched for by every URL that is configured to use global words.

For example, if:

intern

is a global word, every URL using global words will look for intern.

Global words are useful for terms that apply to almost every company you are monitoring.

A non-global word belongs to one particular URL. Only that URL looks for the word.

For example, you may want one company’s page to specifically look for:

software developer

while another company’s page looks for:

finance

A URL can also be configured to ignore global words. If global words are disabled for a URL, that URL will only look for its own non-global words.

## Commands

Once the app is running, type `help` at any time to see the full list of commands. `basic` shows a shorter, beginner-friendly list to get started with. This is what `help` shows:

```
Commands:

url add <url>: adds <url> to list of tracked urls
url remove <id>: removes url with <id>
url global <id> <t or f>: enables(t) or disables(f) global words for the url with <id>
url print <id>: prints the url with <id>

word add <id> <word>: adds <word> to the url with <id>
word remove <id>: removes words with <id>
word removeall <word>: removes all occurences of <word>
word gadd <word>: adds <word> as a global word

print prev: prints previous result
print words: prints all tracked words
print gwords: prints all global words
print ngwords: prints all non-global words
print urls: prints urls and their data

clean urls: permanently removes urls which have found a word
clean words: removes non-global words whose urls are non-existent or found a word

status on: turns on periodic status update
status off: turns off periodic status update
status set <hour>: sets the daily status update at <hour> (military time), may take a day to update
status show: display current status settings

close: stops application from running
help: gets you here
basic: displays basic instructions (good when just starting out)
inst: displays instructions
clear: clears screen
run: immediately checks all tracked URLs for any tracked words or phrases
deleteall: use with caution, deletes all urls and words (cannot be taken back)
```

### Example Workflow

Suppose you want to monitor a company’s careers page for software development internships.

First, go to the company’s careers website and search:

intern

or, for a more targeted search:

software develop

Copy the URL containing those search results.

Then add it:

`url add <career-search-url>`

Add the actual job wording you want to detect:

`word gadd "software developer"`

You could also add:

`word gadd "software development intern"`

The important distinction is that the career-site search can be broad, while the tracked phrase should be specific enough to identify a real position.

This reduces false positives while still allowing the company’s career search to return a broad range of potentially relevant jobs.

## Limitations

The Internshipper only checks the jobs displayed on the URL you provide. If a career site splits its results across multiple pages, jobs on later pages may not be checked.

This usually has less impact when monitoring for new postings because career sites commonly place newer jobs near the beginning of their results. However, when first adding a URL, an existing job you are interested in could already be on a later page and may not be detected.

This is exactly why the career-site search itself matters: searching the site for a broad term like "intern" or "software develop" before copying the URL narrows the results down to a page that's actually likely to contain the jobs you care about, rather than relying on The Internshipper to find them buried in an unfiltered, paginated list.
