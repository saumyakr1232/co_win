from urllib.request import urlopen, Request
import json
from datetime import datetime, timedelta
import time
import sys
from Model.Center import Center
import winsound
from termcolor import cprint
import webbrowser
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3",
    "Connection": "keep-alive",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "en-Us,en;q=0.5"
}

def search_by_pincode(pincode):
    today = datetime.now() + timedelta(1)
    tommorow = today.strftime(f"%d-%m-%Y")
    print(tommorow)
    url = f"https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode={pincode}&date={tommorow}"
    req = Request(url= url, headers=headers)
    webUrl = urlopen(req)
    data  = urlopen(req).read()
    encoding = webUrl.info().get_content_charset('utf-8')
    j_data = json.loads(data.decode(encoding))
    return j_data


def main(pincode= 841440, age=18):
    while True:
        try:
            print("Refreshing")
            j_data = search_by_pincode(pincode)
            for c in j_data['centers']:
                print(c)
                center = Center.from_json(c)
                
                if center.get_availablity(age):
                    cprint(f"Vaccine available at {center.name}", 'green')
                    webbrowser.open("https://www.cowin.gov.in/home")
                    winsound.PlaySound("PoliceSirenVariou.wav", winsound.SND_NOSTOP)
                    break
                    
            else:
                cprint(f"Vaccine is not available at {pincode} for age: {age}",'red')  
            time.sleep(4)
        except KeyboardInterrupt:
            print("Exiting...[*]")
            break
                



    
    
    
