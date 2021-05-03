# Cowin vaccination tracker

- A tracker to automatically check vaccination appointment availability on Cowin website. 

- When appointment slots are found, it will play a notification sound and print the slot details in the console.
  
- This tracker has been made possible due to the public api's hosted by [Cowin Public API](https://apisetu.gov.in/public/marketplace/api/cowin)

# Installation

```bash
pip install pandas requests schedule playsound
```

# Usage

```python
python vaccination_slot_tracker.py
```

# Settings

- Change the below timer to 1 if you want to check the website every one minute.

```py
schedule_minutes = 5
```

- Add the pincode in the below list for which you want to check the slots.

```py
pincodes_list = [400706, 400703]
```

- Change the below flag to false if you don't want to play any notification. 

```py
play_sound_notification=True
```