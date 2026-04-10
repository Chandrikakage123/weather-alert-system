import requests

def check_weather():
    url = "https://api.open-meteo.com/v1/forecast?latitude=28.61&longitude=77.20&current_weather=true&hourly=relativehumidity_2m,windspeed_10m"
    data = requests.get(url).json()

    # Temperature
    temp = data["current_weather"]["temperature"]

    # Wind
    wind = data["current_weather"]["windspeed"]

    # Humidity (first value from hourly)
    humidity = data["hourly"]["relativehumidity_2m"][0]

    print(f"🌡️ Temperature: {temp}°C")
    print(f"💧 Humidity: {humidity}%")
    print(f"🌪️ Wind Speed: {wind} km/h\n")

    # Alerts
    if temp > 35:
        print("🔥 Heat Alert!")

    if humidity > 80:
        print("💧 High Humidity Alert!")

    if wind > 40:
        print("🌪️ Strong Wind Alert!")

    if humidity > 70:
        print("🌧️ Possible Rain Alert!")

    if temp <= 35 and humidity <= 70 and wind <= 40:
        print("✅ Weather Normal")


if __name__ == "__main__":
    check_weather()
