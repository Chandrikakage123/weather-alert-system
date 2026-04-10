import requests

def check_weather():
    url = "https://api.open-meteo.com/v1/forecast?latitude=28.61&longitude=77.20&current_weather=true&hourly=relativehumidity_2m,windspeed_10m"
    
    response = requests.get(url)
    
    # Debug: check status
    print("Status Code:", response.status_code)

    data = response.json()
    print("Full API Data:", data)  # 👈 VERY IMPORTANT

    # Safe extraction
    if "current_weather" not in data:
        print("❌ Error: No current weather data found")
        return

    temp = data["current_weather"].get("temperature", "N/A")
    wind = data["current_weather"].get("windspeed", "N/A")

    humidity = data.get("hourly", {}).get("relativehumidity_2m", ["N/A"])[0]

    print(f"\n🌡️ Temperature: {temp}°C")
    print(f"💧 Humidity: {humidity}%")
    print(f"🌪️ Wind Speed: {wind} km/h\n")

    # Alerts
    if temp != "N/A" and temp > 35:
        print("🔥 Heat Alert!")

    if humidity != "N/A" and humidity > 80:
        print("💧 High Humidity Alert!")

    if wind != "N/A" and wind > 40:
        print("🌪️ Strong Wind Alert!")

    if humidity != "N/A" and humidity > 70:
        print("🌧️ Possible Rain Alert!")

    if temp != "N/A" and humidity != "N/A" and wind != "N/A":
        if temp <= 35 and humidity <= 70 and wind <= 40:
            print("✅ Weather Normal")


if __name__ == "__main__":
    check_weather()
