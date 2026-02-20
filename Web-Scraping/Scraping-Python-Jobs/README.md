# Python.org Jobs Web Scraper

A simple and clean Python web scraper that extracts the latest job listings from the official Python job board and saves them to CSV and JSON files.

## Features

* Fetches live job data from https://www.python.org/jobs/
* Extracts key information:

  * Job Title
  * Company Name
  * Location
  * Date Posted
  * Job Link
* Saves data in:
  * CSV format (`jobs.csv`)
  * JSON format (`jobs.json`)
* Uses type hints and modular functions
* Beginner-friendly and easy to extend

---

## Technologies Used

* Python 3
* requests
* BeautifulSoup4
* csv
* json

---

## Project Structure

```
python-jobs-scraper/

scraper.py
jobs.csv
jobs.json
README.md
```

---

## How It Works

The script performs 3 main steps:

1. Fetches the HTML page using `requests`
2. Parses the HTML using `BeautifulSoup`
3. Saves the extracted data into CSV and JSON files

---

## Example Output

### CSV

```
title,company,location,date,link
Infrastructure Engineer,Python Software Foundation,Remote,2025-02-15,https://www.python.org/jobs/8044/
```

### JSON

```
[
    {
        "title": "Infrastructure Engineer",
        "company": "Python Software Foundation",
        "location": "Remote",
        "date": "2025-02-15",
        "link": "https://www.python.org/jobs/8044/"
    }
]
```

---

## What I Learned

* Web scraping fundamentals
* HTML parsing
* Working with CSV and JSON
* Writing clean, modular Python code
* Using type hints

---

## Futur
