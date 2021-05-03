from typing import List
import requests
from datetime import date
import pandas as pd
import time
import schedule
from playsound import playsound

# SETTINGS

# RUN EVERY x minutes
schedule_minutes = 5

# PINCODE
pincodes_list = [400706, 400703]

# PLAY SOUND on update
play_sound_notification=True

# ================================================================================================================

today = date.today()
# dd/mm/YY
todays_date = today.strftime(r"%d-%m-%Y")
print("DATE =", todays_date)


def check_slots_by_pincodes(pincodes_list:List = pincodes_list):
    print(f"---"*20)
    now = time.strftime(r"%d/%m/%Y %H:%M:%S")
    print(f"Checking slots at : {now}")
    centers_list = []

    for pincode in pincodes_list:

        PINCODE_URL = f"https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode={pincode}&date={todays_date}"
        r = requests.get(url=PINCODE_URL)

        try:
            data = r.json()
        except:
            print("Error in decoding")
            continue
        centers = data["centers"]
        centers_list = centers_list + centers

    # print(centers_list)
    available_centers = []
    for center in centers_list:
        sessions = center['sessions']
        for session in sessions:
            if session['min_age_limit'] == 18 and session['available_capacity'] > 0:
                available_centers.append([center['name'],center['state_name'],center['district_name'], center['pincode'], center['fee_type'],session['available_capacity'], session['min_age_limit'], session['vaccine'],session['date'], session['slots'] ])
    
    if len(available_centers) > 0:
        available_centers_df = pd.DataFrame(available_centers, columns=['name','state_name','district_name', 'pincode', 'fee_type','available_capacity', 'min_age_limit', 'vaccine', 'date','slots'])

        print("=="*10+' AVAIABLE CENTERS '+"=="*10)
        print(available_centers_df)
        if play_sound_notification:
            playsound("./notification.mp3")
    else:
        print("No slots found")

# Run 1 time on praogram start.
check_slots_by_pincodes()

# Schedule every x min.
schedule.every(schedule_minutes).minutes.do(check_slots_by_pincodes)


while True:
    schedule.run_pending()
    time.sleep(1)