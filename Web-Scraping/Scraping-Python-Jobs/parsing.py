from bs4 import BeautifulSoup
import requests
import csv
import json

def fetch_page(url: str) -> str:
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.text

def parse_jobs(html: str) -> list[dict]:
    web = BeautifulSoup(html, "html.parser")
    job_list = web.find(name="ol", class_="list-recent-jobs")
    jobs = job_list.find_all("li")
    list_jobs = []
    for job in jobs:
        title = job.find("a").text
        link = f"https://www.python.org{job.find('a').get('href')}"
        location = job.find("span", class_="listing-location").text
        company = list(job.find("span", class_="listing-company-name").stripped_strings)[-1]
        publish_date = job.find("time").text
        list_jobs.append({
            "title": title,
            "company": company,
            "location": location,
            "date": publish_date,
            "link":link
        })
    return list_jobs

def save_csv(jobs: list[dict]) -> None:
    with open("jobs.csv","w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["title","company","location","date","link"])
        for job in jobs:
            writer.writerow(
                [
                    job["title"],
                    job["company"],
                    job["location"],
                    job["date"],
                    job["link"]
                ]
            )


def save_json(jobs: list[dict]) -> None:
    with open("jobs.json", "w", encoding="utf-8") as file:
        json.dump(jobs ,file, indent=4)

def main() -> None:
    url = "https://www.python.org/jobs/"
    html = fetch_page(url)
    jobs_list = parse_jobs(html)
    save_csv(jobs_list)
    save_json(jobs_list)

if __name__ == "__main__":
    main()