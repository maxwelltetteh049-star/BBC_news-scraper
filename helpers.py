import requests
import logging
import time

logging.basicConfig(level=logging.INFO)

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
                logging.info("request.get success")
                break
            except requests.exceptions.Timeout:
                logging.info("Requests loading timeout")
                time.sleep(4)
                logging.info("Retring again ...")
                time.sleep(5)
            except requests.exceptions.RequestException:
                logging.info("CONNECT IS NOT GOOD")
                if atmp == atmps:
                    input("Retrying not helping, do you want to retry again? (click any key to start retrying)")
                    atmp = 1
                else:
                    logging.info("Retrying in 20 secs, wait ..")
                    time.sleep(20)
                    atmp += 1
                    logging.info("START")
    
        return response           
                


        

