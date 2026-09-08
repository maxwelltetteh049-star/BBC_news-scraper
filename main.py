import mysql.connector
from helpers import Helper
import logging
import time, random

logging.basicConfig(level=logging.INFO)
helper = Helper()

messages = []
datas = []

#========DATABASE AUTHORIZATION=======

conn = mysql.connector.connect(
    host = "YOUR_HOST",
    user = "YOUR_USERNAME",
    password = "PASSWORD",
    database = "DATABASE"
)
cursor = conn.cursor()
cursor.execute("SET sql_safe_updates = 0")


#=========================== LOAD DATA FROM MYSQL==========================
logging.info("Loading old news from DATABASE")
old_data = {}

query = "SELECT * FROM bbc"

cursor.execute(query)
result = cursor.fetchall()
for row in result:
    title = row[0]
    detail_link = row[2]  
    old_data[detail_link] = title
logging.info("DONE loading")
time.sleep(4)
logging.info("BEGINNING Extraction")

pages = 6

#================================ LOOP THROUGH PAGES =======================

for page in range(1, pages):
    data = []

    response = helper.load_site(page)
    logging.info(f"Starting SCRAPING page {page}")

    response = response.json()
    
    
    data = response.get("data", [])
        
    for index in range(len(data)):
        news = data[index]
        try:
            title = news.get("title")
            summary = news.get("summary")
            path = news.get("path")
            d_link = f"https://www.bbc.com{path}"
            image = news.get("indexImage", {}).get("model", {}).get("blocks").get("src")
        except:
            continue

        #print(title)
        #print(summary)
        #print(d_link)
        #print(image)


        if d_link not in old_data:
            print(f"added news {index + 1}")
            message = helper.email_container(title, summary, d_link, image)
            messages.append(message)

            info = ((title, summary, d_link))
            data.append(info)
        else:
            pass

    datas.extend(data)
    logging.info(f"Done with page {page}")
    time.sleep(random.uniform(2.5, 4.5))


logging.info("Scraped all Asigned PAGES")
full_message = "\n".join(messages)
email_body = helper.email_body(full_message)

if messages:
    helper.send_email(
        subject="BBC NEWS UPDATE",
        body = email_body
    )
else:
    logging.info("No New News was SEEN")

input("do you want to continue")
query = "DELETE FROM bbc"
cursor.execute(query)

cursor.execute("SET sql_safe_updates = 1")

query1 = '''
INSERT INTO bbc(Title, Summary, Detail_link)
VALUES(%s, %s, %s)
'''
cursor.executemany(query1, datas)
conn.commit()
logging.info("New NEWS info is PUSHED into DATAbase")







