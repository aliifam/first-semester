import requests
import os 

for page in range(5150, 5230):
    x = requests.get("https://web.ctf.rasyidmf.com/chal10/", params={"no":page})
    if page == "CTRF":
        print(page)