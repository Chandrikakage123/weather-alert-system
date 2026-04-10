import requests

def check_weather():
    url = "https://api.open-meteo.com/v1/forecast?latitude=28.61&longitude=77.20&current_weather=true"
    data = requests.get(url).json()

    temp = data["current_weather"]["temperature"]

    print(f"Current Temperature: {temp}")

    if temp > 35:
        print("🔥 Heat Alert!")
    else:
        print("✅ Weather Normal")

if __name__ == "__main__":
    check_weather()
