from bs4 import BeautifulSoup
import requests
import pandas as pd
import time

start_time = time.time()

initial_request = requests.get("https://nextspaceflight.com/launches/past/?page=1&search=")
initial_soup = BeautifulSoup(initial_request.text, "html.parser")

buttons = initial_soup.select(selector="button.mdc-button.mdc-button--raised")
button_spans = initial_soup.select(selector="button.mdc-button.mdc-button--raised span")
for i, span in enumerate(button_spans):
    if span.text == "last »":
        last_button = buttons[i]

try:
    last_page_number = int(last_button.get("onclick").split("&")[0].split("=")[2])
except NameError:
    print("Website layout has changed")
else:
    for i in range(1, last_page_number+1):
        iteration_time = time.time()
        data = []
        page_response = requests.get(f"https://nextspaceflight.com/launches/past/?page={i}&search=")
        page_soup = BeautifulSoup(page_response.text, "html.parser")
        cards = page_soup.select(selector="div.mdl-grid div.mdl-cell.mdl-cell--6-col")
        # Looping through all cards
        for card in cards:
            card_data = {}
            # Get organization name from card preview
            organization = card.select(selector="div.mdl-card__title-text span")[0].text.strip()

            # searching for button "Details"
            detail_btns = card.select(selector="button.mdc-button")
            for btn in detail_btns:
                if btn.select(selector="span")[0].text.strip() == "Details":
                    detail_btn = btn
                    break

            # Get value of launch id
            try:
                launch_id = detail_btn.get("onclick").split("/")[3].strip("'")
                id_response = requests.get(f"https://nextspaceflight.com/launches/details/{launch_id}")
                details_soup = BeautifulSoup(id_response.text, "html.parser")
            except NameError:
                print("Something wrong with card")
            else:
                # Looking for price
                price = None
                rocket_status = None
                for detail in details_soup.select(selector="div.mdl-cell.mdl-cell--6-col-desktop.mdl-cell--12-col-tablet"):
                    if detail.text.startswith("Price"):
                        price = detail.text.split(" ")[1].strip("$")
                    elif detail.text.startswith("Status"):
                        rocket_status = detail.text.split(" ")[1]

                # Looking for Location
                titles = details_soup.select(selector="h3.section--center.mdl-grid.title")

                for j, title in enumerate(titles):
                    if title.text == "Location":
                        loc_title = titles[j]
                        break
                try:
                    location = loc_title.find_next("h4").text
                except NameError:
                    print("No location")
                    location = None

                # Looking for status
                status = details_soup.select_one(selector="h6.rcorners.status span")
                if status is not None:
                    status = status.text
                    if status != "Success" and status != "Failure":
                        status = None
                # Looking for date
                date = details_soup.find(id="localized")
                if date is not None:
                    date = date.text

                card_data = dict([("organization", organization), ("location", location), ("date", date),
                                  ("rocket_status", rocket_status), ("price", price), ("mission_status", status)])
                #print(f"Organization: {organization}\nLocation: {location}\nDate: {date}\nRocket status: {rocket_status}\nPrice: {price}\nMission status: {status}\n\n\n")
                data.append(card_data)
        pd.DataFrame(data).to_csv("mission_launches.csv", mode="a", header=False, index=False)
        print(f"page number: {i} ----- {time.time() - start_time}s ----- ({time.time() - iteration_time})")
