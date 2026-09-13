# BBC News Scraper

## Description
An automated Python scraper that retrieves BBC World News through a BBC API endpoint, stores scraped articles in a MySQL database, detects newly published news, and sends new articles to email in a structured HTML format.To ensure the scraper run each and everyday automatically, I deployed it on APIFY.

This project was built as a practical web-data extraction project to develop skills in API scraping, data storage, duplicate detection, automation, and email notifications.

## 🚀 Features

- Scrapes BBC World News through a BBC API endpoint
- Extracts:
  - News title
  - News summary
  - Article detail link
  - Image URL
- Scrapes up to 5 pages of news
- Stores scraped articles in a MySQL database
- Uses the database to compare previously scraped news with newly scraped news
- Prevents previously sent articles from being sent again
- Sends an email notification when new news is found
- Generates a structured HTML email interface for displaying the news
- Includes retries and error handling to improve reliability
- Designed to run regularly, such as once per day

## 🛠️ Technologies Used

- Python
- Requests – used to make API requests to the BBC endpoint
- MySQL – used to store previously scraped news
- mysql-connector-python – used to connect Python to the MySQL database
- smtplib – used to send email notifications
- Railway – used to deploy the MySQL database
- HTML/CSS – used to structure and style the email interface
- Apify - used to deploy the scraper in the cloud for scheduling to automatically run script.

## 🔄 How It Works

The scraper follows this general workflow:

BBC API
   ↓
API Request
   ↓
Extract News Data
   ↓
Compare with MySQL Database
   ↓
Identify New Articles
   ↓
Store New Articles
   ↓
Generate HTML Email
   ↓
Send Email

1. Request BBC News

The scraper sends API requests to the BBC endpoint and retrieves BBC World News data.

2. Extract Article Information

The scraper extracts the relevant information from each article:

Title
Summary
Article URL
Image URL

3. Check the Database

The extracted articles are compared against previously stored articles in the MySQL database.

This allows the scraper to determine whether an article is new or already processed.

4. Store New Articles

New articles are stored in the MySQL database so they can be recognized during future scraping runs.
And old ones are deleted automatically by using sql query.

5. Send Email Notification

If new articles are found, the scraper creates an HTML-formatted email containing the news articles and sends it through email to receiver.
If no new news is found, previously processed articles are not sent again.

## 🗄️ Database

The project uses a MySQL database deployed on Railway.
The database acts as persistent storage for scraped news.
Its main purpose is not simply to store the data, but also to provide a way to determine whether an article has already been processed.

For example:

Previous scraping:
Article A
Article B
Article C

New scraping:
Article B
Article C
Article D
Article E

New articles:
Article D
Article E

Only the new articles are included in the email notification.

## 📧 Email Output

When new news is detected, the scraper sends an HTML-formatted email.

The email is designed to present the news in a structured interface containing information such as:

- News title
- Summary
- Article link
- News image

This makes the final result easier to read than sending raw scraped data.

## 📄 Scraping Pages

The scraper processes up to 5 pages of BBC World News.

The five-page limit is intentional because the scraper is designed to run regularly, such as once every day. The expected amount of new daily news can generally be covered within those pages.

## 🔁 Reliability

The scraper includes retry mechanisms and error handling to make the scraping process more reliable.

For example, if an API request temporarily fails due to network problems or loading timeout, the scraper can retry the request rather than immediately terminating the entire process.

This is particularly useful for an automated scraper that is expected to run regularly without manual intervention.

## 🔐 Configuration

The scraper requires configuration for services such as:

- Database credentials (mysql)
- Email credentials(app_password)

Sensitive credentials should not be hard-coded or committed to GitHub.

Use environment variables or another secure configuration method to store credentials.

Example:

DB_HOST
DB_PORT
DB_USER
DB_PASSWORD
DB_NAME

EMAIL_USER
EMAIL_PASSWORD
EMAIL_RECEIVER

## ▶️ Running the Scraper

After configuring the required environment variables, run:

python main.py

The scraper will:

1. Request BBC World News data.
2. Process up to five pages.
3. Extract article information.
4. Compare the articles with the MySQL database.
5. Identify new articles.
6. Store new articles in the database.
7. Generate the HTML email.
8. Send the email when new articles are available.

## 🎯 Project Goals

This project was created as a practical portfolio project to strengthen my skills in:

- Python programming
- API-based data extraction
- HTTP requests
- Working with databases
- Data comparison and duplicate detection
- Email automation
- HTML email generation
- Error handling and retries
- Building automated data pipelines

## 📚 What I Learned

Through this project, I gained practical experience building a complete data pipeline rather than simply extracting information from a website.

## ⚠️ Disclaimer

This project is intended for educational and portfolio purposes. When accessing or collecting data from external services, users should respect the service's terms of use, applicable policies, and reasonable request limits.

## 👤 Author

Maxwell Tetteh

This project is part of my journey toward developing practical skills in Python, web data extraction, APIs, databases, and automation.

