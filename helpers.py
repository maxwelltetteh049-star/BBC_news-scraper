import requests
import logging
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import time


url = "https://web-cdn.api.bbci.co.uk/xd/content-collection/07cedf01-f642-4b92-821f-d7b324b8ba73"

headers = {
    "accept": "*/*",
    "accept-language": "en-US,en;q=0.9",
    "origin": "https://www.bbc.com",
    "priority": "u=1, i",
    "referer": "https://www.bbc.com/news/world",
    "sec-ch-ua": "\"Google Chrome\";v=\"147\", \"Not.A/Brand\";v=\"8\", \"Chromium\";v=\"147\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36"
}


class Helper:
    def load_site(self,page):
        querystring = {"page":f"{page}","size":"9","path":"/news/world"}

        atmp = 1
        atmps = 5
        while atmp <= atmps:
            try:
                response = requests.request("get", url, headers=headers, params=querystring, timeout=40)
                if response.status_code == 200:
                    logging.info("request.get success")
                    break
                else:
                    logging.warning(f"STATUS CODE ERROR : {response.status_code}=={response.reason}")
                    if response.status_code == 429:
                        print("Too many requests")
                        time.sleep(100)
            except requests.exceptions.Timeout:
                logging.info("Requests loading timeout")
                time.sleep(4)
                logging.info("Retring again ...")
                time.sleep(5)
            except requests.exceptions.RequestException:
                logging.info("CONNECTION IS NOT GOOD")
                if atmp == atmps:
                    input("Retrying not helping, do you want to retry again? (click any key to start retrying)")
                    atmp = 1
                else:
                    logging.info("Retrying in 20 secs, wait ..")
                    time.sleep(20)
                    atmp += 1
                    logging.info("START")
    
        return response  

    def email_container(self, title, summary, d_link, image):
        data = f'''
<table
                    width="100%"
                    cellpadding="0"
                    cellspacing="0"
                    border="0"
                    class="news-item">
                    <tr>
                        <td class="news-content">
                            <h3 class="news-title">
                                <a href={d_link}>
                                    {title}
                                </a>
                            </h3>
                            <p class="summary">
                                {summary}
                            </p>
                            <a href={d_link} class="read-more">
                                Read more
                            </a>
                        </td>

                        <td width="105" valign="top">

                            <img
                                src={image}
                                alt="News image"
                                class="news-image"
                            >

                        </td>
                    </tr>
                </table>

'''
        return data

    def send_email(self, subject, body):
        sender = "SENDER_EMAIL"
        password = "APP_PASSWORD"
        receiver = "RECEIVER_EMAIL"

        msg = MIMEMultipart("alternative")
        msg["Subject"] = subject
        msg["From"] = sender
        msg["To"] = receiver

        msg.attach(MIMEText(body, "html"))

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(sender, password)
            smtp.send_message(msg)
        logging.info("Email message is been sent to receiver")

    def email_body(self, inside_body):
        body = '''
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>BBC News Alert</title>

    <style>
        body {
            margin: 0;
            padding: 0;
            background-color: #2b2b2b;
            font-family: Arial, Helvetica, sans-serif;
            color: #ffffff;
        }

        .email-wrapper {
            width: 100%;

            padding: 25px 0;
            background-color: #2b2b2b;
        }

        .email-container {
            width: 92%;
            max-width: 620px;
            margin: 0 auto;
            background-color: #333333;
        }

        /* Header */
        .header {
            padding: 22px 25px;
            border-bottom: 1px solid #555555;
        }

        .header h1 {
            margin: 0;
            font-size: 22px;
            line-height: 1.3;
            color: #ffffff;

        }

        .header p {
            margin: 7px 0 0;
            font-size: 13px;
            color: #cfcfcf;
        }

        /* Category */
        .category {
            padding: 15px 25px 10px;
        }

        .category-title {
            margin: 0;
            font-size: 16px;
            color: #ffffff;
            font-weight: bold;
        }

        .category-line {
            width: 100%;

            height: 1px;
            background-color: #555555;
            margin-top: 9px;
        }

        /* News item */
        .news-item {
            padding: 15px 25px;
            border-bottom: 1px solid #555555;
        }

        .news-content {
            vertical-align: top;
            padding-right: 15px;
        }

        .news-title {
            margin: 0 0 7px;
            font-size: 15px;
            line-height: 1.35;
        }

        .news-title a {
            color: #ffffff;
            text-decoration: none;
        }

        .summary {
            margin: 0;
            font-size: 12px;
            line-height: 1.55;
            color: #cccccc;
        }

        .read-more {
            display: inline-block;
            margin-top: 8px;
            font-size: 11px;
            color: #ffffff;
            text-decoration: underline;
        }

        /* Image */
        .news-image {

            width: 105px;
            height: 70px;
            object-fit: cover;
            display: block;
        }

        /* Footer */
        .footer {
            padding: 18px 25px;
            text-align: center;
            color: #999999;
            font-size: 11px;
            line-height: 1.5;
        }

        .footer a {
            color: #cccccc;
        }

        @media only screen and (max-width: 480px) {

            .email-wrapper {

                padding: 10px 0;
            }

            .email-container {
                width: 96%;
            }

            .header {
                padding: 18px;
            }

            .category {
                padding: 13px 18px 8px;
            }

            .news-item {
                padding: 13px 18px;
            }

            .news-image {
                width: 90px;
                height: 62px;

            }

            .news-content {
                padding-right: 10px;
            }

            .news-title {
                font-size: 14px;
            }

            .summary {
                font-size: 11px;
            }
        }
    </style>
</head>

<body>

<div class="email-wrapper">

    <table

        class="email-container"
        cellpadding="0"
        cellspacing="0"
        border="0"
        align="center"
    >
        <tr>
            <td>

                <!-- HEADER -->
                <div class="header">

                    <h1>
                        Here's today's news update from BBC
                    </h1>

                    <p>
                        Your daily selection of the latest news.
                    </p>

                </div>


                <!-- WORLD NEWS -->
                <div class="category">

                    <h2 class="category-title">
                        WORLD NEWS
                    </h2>

                    <div class="category-line"></div>

                </div>

                '''+ str(inside_body) +'''
       

                <!-- FOOTER -->
                <div class="footer">

                    You are receiving this email because you
                    subscribed to BBC News alerts.

                    <br><br>

                    <a href="#">
                        Manage your email preferences
                    </a>

                </div>

            </td>
        </tr>
    </table>

</div>

</body>
</html>

'''
        return body

