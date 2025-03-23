from bs4 import BeautifulSoup
import requests
import sqlite3
import csv

def scrape_jobs():
    url = "https://realpython.github.io/fake-jobs"

    response = requests.get(url=url)

    soup = BeautifulSoup(response.content, features="html.parser")

    job_tags = soup.find_all("div", class_="card-content")

    # print(soup[])

    # print(location_tag[0]['location'])

    # print(job_tags[0])

    jobs = []

    for job_tag in job_tags:
        job_title = job_tag.find("h2").text.strip()
        company = job_tag.find("h3").text.strip()
        location = job_tag.find("p", class_="location").text.strip()


        apply_link = job_tag.find('a', string='Apply')['href']
        job_response = requests.get(url=apply_link)

        soup2 = BeautifulSoup(job_response.content, features="html.parser")
        job_conent = soup2.find("div", class_="content")
        job_description = job_conent.find("p").text
        
        jobs.append({
            'title': job_title,
            'company': company,
            'location': location,
            'description': job_description,
        })
        
        
    return jobs


def create_database():
    conn = sqlite3.connect(r"C:\Users\ids\Desktop\PythonHomework\lesson-12\homework\jobs.db")

    cur = conn.cursor()

    cur.execute('''
                CREATE TABLE IF NOT EXISTS jobs (
                    title TEXT,
                    company TEXT,
                    location TEXT,
                    description TEXT,
                    UNIQUE(title, company, location, description)
                    )
                    '''
                    )

    conn.commit()
    conn.close()


def insert_or_update_data(jobs):
    conn = sqlite3.connect(r"C:\Users\ids\Desktop\PythonHomework\lesson-12\homework\jobs.db")
    cursor = conn.cursor()

    for job in jobs:
        cursor.execute('''
            SELECT description 
            FROM jobs
            WHERE title = ? AND company = ? AND location = ?
        ''', (job['title'], job['company'], job['location']))

        existing_job = cursor.fetchone()

        if existing_job:
            if existing_job[0] != job['description']:
                cursor.execute('''
                    UPDATE jobs
                    SET description = ?
                    WHERE title = ? AND company = ? AND location = ?
                ''', (
                    job['description'],
                    job['title'], 
                    job['company'], 
                    job['location']
                ))
                print(f"Updated: {job['title']} at {job['company']}")
            else:
                print(f"No changes for: {job['title']} at {job['company']}")
        else:
            cursor.execute('''
                INSERT INTO jobs (title, company, location, description)
                VALUES (?, ?, ?, ?)
            ''', (
                job['title'], 
                job['company'], 
                job['location'], 
                job['description'],
            ))
            print(f"Inserted: {job['title']} at {job['company']}")

    conn.commit()
    conn.close()


def filter_jobs(filter_type, filter_value):
    conn = sqlite3.connect(r"C:\Users\ids\Desktop\PythonHomework\lesson-12\homework\jobs.db")
    cursor = conn.cursor()

    query = f"SELECT * FROM jobs WHERE {filter_type} = ?"
    cursor.execute(query, (filter_value,))

    jobs = cursor.fetchall()
    conn.close()

    return jobs

def export_to_csv(jobs, filename="C:\Users\ids\Desktop\PythonHomework\lesson-12\homework\iltered_jobs.csv"):
    with open(filename, mode='w') as file:
        writer = csv.writer(file)
        writer.writerow(["Title", "Company", "Location", "Description"])
        writer.writerows(jobs)
        
create_database()
filtered_jobs = filter_jobs("location", "South Jorgeside, AP")
export_to_csv(jobs=filtered_jobs)
print("Filtered!")