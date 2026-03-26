
import asyncio
import aiohttp
import json
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")

URL = "http://api.openweathermap.org/data/2.5/weather"

async def fetch_weather(session, city):
    try:
        params = {"q": city, "appid": API_KEY}
        async with session.get(URL, params=params) as response:
            if response.status != 200:
                raise Exception(f"Invalid city: {city}")
            data = await response.json()
            return data["weather"][0]["main"]
    except Exception as e:
        print(f"Error for {city}: {e}")
        return None

def generate_apology(customer, city, weather):
    return f"Hi {customer}, your order to {city} is delayed due to {weather.lower()}. We appreciate your patience!"

async def process_orders():
    with open("orders.json", "r") as f:
        orders = json.load(f)

    async with aiohttp.ClientSession() as session:
        tasks = [fetch_weather(session, order["city"]) for order in orders]
        results = await asyncio.gather(*tasks)

    for order, weather in zip(orders, results):
        if weather in ["Rain", "Snow", "Extreme"]:
            order["status"] = "Delayed"
            order["message"] = generate_apology(order["customer"], order["city"], weather)

    with open("updated_orders.json", "w") as f:
        json.dump(orders, f, indent=2)

if __name__ == "__main__":
    asyncio.run(process_orders())
