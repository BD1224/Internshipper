The Internshipper

The Internshipper is a local command-line tool that monitors company career pages for internships and other job openings. You provide the career-page URLs and the words or phrases you want to look for, and the program periodically checks those pages for matches.

The goal is to avoid repeatedly checking dozens of company career pages manually.

How It Works

For each company you want to track:

1. Go to the company’s careers page.
2. Search for the type of position you are interested in.
3. Copy the resulting search-page URL.
4. Add that URL to The Internshipper.
5. Add one or more words or phrases that describe the jobs you want the program to find.

The program checks the page for the words or phrases you provide and reports a match if it finds at least one of them. It does not require every tracked word or phrase to appear on the page.

Finding the Right URL

Whenever possible, use the URL produced by the company’s own career search.

For example, if you are looking for internships, search the company’s career site for:

intern

You can also include a location in the company’s search if you only want positions in a particular area.

For example:

intern Boston

Then copy the resulting URL and add it to The Internshipper. Then, in The Internshipper, add a word or phrase such as analyst, software, or another term that describes the specific internship you want. The program will check that internship results page for the term you provide and report when it finds a matching position.

Searching for Broader Job Categories

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

Tracking Phrases

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

Global and Non-Global Words

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

Commands

URLs

Add a URL:

url add <url>

Remove a URL:

url rm <id>

Enable or disable global words for a URL:

url global <id> <t or f>

* t — use global words
* f — ignore global words

Print a specific URL:

url print <id>

Words

Add a word or phrase to a specific URL:

word add <url_id> <word>

Example:

word add 2 "software developer"

Remove a tracked word by its word ID:

word rm <word_id>

Remove every occurrence of a particular word or phrase:

word remove <word>

Add a global word or phrase:

word gadd <word>

Example:

word gadd "summer analyst"

Printing Information

Print the previous result:

print prev

Print all tracked words:

print words

Print global words:

print gwords

Print non-global words:

print ngwords

Print URLs and their associated data:

print urls

Example Workflow

Suppose you want to monitor a company’s careers page for software development internships.

First, go to the company’s careers website and search:

intern

or, for a more targeted search:

software develop

Copy the URL containing those search results.

Then add it:

url add <career-search-url>

Add the actual job wording you want to detect:

word add 1 "software developer"

You could also add:

word add 1 "software development intern"

The important distinction is that the career-site search can be broad, while the tracked phrase should be specific enough to identify a real position.

This reduces false positives while still allowing the company’s career search to return a broad range of potentially relevant jobs.

Limitations

The Internshipper only checks the jobs displayed on the URL you provide. If a career site splits its results across multiple pages, jobs on later pages may not be checked.

This usually has less impact when monitoring for new postings because career sites commonly place newer jobs near the beginning of their results. However, when first adding a URL, an existing job you are interested in could already be on a later page and may not be detected.