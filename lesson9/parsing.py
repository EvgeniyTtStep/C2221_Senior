import requests


response = requests.get("https://coinmarketcap.com/")

resp_text = response.text

resp_pars = resp_text.split("<span>")

for elem in resp_pars:
    if elem.startswith("$"):
        for elem2 in elem.split("</span>"):
             if elem2.startswith("$") and elem2[1].isdigit():
                 print(elem2)

