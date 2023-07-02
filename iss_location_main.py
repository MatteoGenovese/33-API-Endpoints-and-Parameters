import requests
from datetime import datetime
import time
import smtplib
import password

MY_LAT = 46.002352
MY_LONG = 8.742317
MY_EMAIL = "matteo.genovese.91@gmail.com"

parameters = {
    "lat": MY_LAT,
    "long": MY_LONG,
    "formatted": 0
}

issPositionResponse = requests.get(url="http://api.open-notify.org/iss-now.json")
issPositionResponse.raise_for_status()

issPosition = issPositionResponse.json()["iss_position"]
isslatitude = float(issPosition["latitude"])
isslongitude = float(issPosition["longitude"])


def isNigth():
    sunriseSunsetHoursResponse = requests.get(url=f"https://api.sunrise-sunset.org/json", params=parameters)
    sunriseSunsetHoursResponse.raise_for_status()

    sunriseSunsetHours = sunriseSunsetHoursResponse.json()["results"]

    sunrise = int(str(sunriseSunsetHours["sunrise"]).split("T")[1].split(":")[0])
    sunset = int(str(sunriseSunsetHours["sunset"]).split("T")[1].split(":")[0])

    if 0 < time_now.hour < sunrise or time_now.hour > sunset:
        return True
    else:
        return False


def sendEmail():
    # search your smtp information by google it
    with smtplib.SMTP("smtp.gmail.com") as connection:
        # create transport layer security, it protect the connection at our e-mail server
        connection.starttls()
        connection.login(user=MY_EMAIL, password=password.myPassword)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs="matteo.genovese@icloud.com",
                            msg=f"Subject:ISS SOPRA LA TUA TESTA!!!\n\nGuarda in alto")
        connection.close()


def issIsNear():
    latitudeDistance = isslatitude - MY_LAT
    longitudeDistance = isslongitude - MY_LONG

    if -5 < latitudeDistance < +5 and -5 < longitudeDistance < +5:
        return True
    else:
        return False


time_now = datetime.now()

while True:
    if isNigth() and issIsNear():
        sendEmail()
    time.sleep(60)

# If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
