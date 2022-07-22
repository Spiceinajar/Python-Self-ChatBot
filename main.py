import requests
import pyttsx3

#you need to install these /\

#credit to rapidapi for the bot
#this code is modified by spiceinajar, original code from rapidapi

url = "https://random-stuff-api.p.rapidapi.com/ai"
res = "="
speech = pyttsx3.init()

while True:
    if res == "=":
        message = input("Enter msg:")
    else:
        message = res

    querystring = {"msg": message, "bot_name": "Ed",
                   "bot_gender": "male", "bot_master": "Spiceinajar", "bot_age": "0",
                   "bot_company": "Spiceinajar", "bot_location": "Spiceinajar's hard drive",
                   "bot_email": "None", "bot_build": "Public (OPTIONAL)",
                   "bot_birth_year": "2022", "bot_birth_date": "7/23/2022",
                   "bot_birth_place": "United States", "bot_favorite_color": "Purple",
                   "bot_favorite_book": "None", "bot_favorite_band": "None",
                   "bot_favorite_artist": "Jack Stauber", "bot_favorite_actress": "None",
                   "bot_favorite_actor": "Dwayne Johnson", "id": "For customised response for each user"}

    #customize bot info /\

    headers = {
        "Authorization": "AUTHORIZATION HERE",
        "X-RapidAPI-Host": "random-stuff-api.p.rapidapi.com",
        "X-RapidAPI-Key": "YOUR API KEY HERE"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    res = response.text.split('"')[37]

    print(res)

    speech.say(res)
    speech.runAndWait()
