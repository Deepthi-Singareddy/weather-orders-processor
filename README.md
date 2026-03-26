# 🌦️ Weather-Based Order Delay System

A simple yet powerful Python automation project that processes customer orders and determines delays based on real-time weather conditions.

---

## 🚀 Project Overview

This system reads customer orders from a JSON file, checks the weather for each city, and updates order status accordingly.

If severe weather conditions are detected, the system:

* Marks the order as **Delayed**
* Generates a personalized apology message

---

## 🧠 Problem Statement

Logistics and delivery systems often face delays due to unpredictable weather conditions.

This project simulates a real-world solution where:

* Weather data influences delivery timelines
* Customers are proactively informed

---

## 🛠️ Tech Stack

* 🐍 Python
* 🌐 OpenWeatherMap API
* 📁 JSON (Data Storage)
* ⚙️ dotenv (Environment Variables)

---

## 📂 Project Structure

```
weather-order-processor/
│
├── main.py                # Core logic
├── orders.json            # Input data
├── updated_orders.json    # Output data
├── requirements.txt       # Dependencies
├── AI_LOG.txt             # Logs
├── .gitignore             # Ignore secrets
├── .env.example           # API key template
└── README.md              # Documentation
```

---

## ⚙️ How It Works

1. Load orders from `orders.json`
2. Fetch weather using OpenWeather API
3. Analyze weather condition:

   * Rain / Snow / Extreme → Delay
   * Clear / Clouds → No delay
4. Update order status
5. Generate apology message if delayed
6. Save results to `updated_orders.json`

---

## 🌍 Weather Logic

| Weather Condition | Action  |
| ----------------- | ------- |
| Rain              | Delayed |
| Snow              | Delayed |
| Extreme           | Delayed |
| Clear             | Pending |
| Clouds            | Pending |

---

## 🔐 Environment Setup

Create a `.env` file:

```
OPENWEATHER_API_KEY=your_api_key_here
```

---

## ▶️ How to Run

```bash
pip install -r requirements.txt
python main.py
```

---

## 📊 Sample Output

```json
{
  "order_id": "1001",
  "status": "Delayed",
  "message": "Hi Alice Smith, your order is delayed due to rain."
}
```

---

## 📌 Key Features

✔ Real-time weather integration
✔ Automated decision making
✔ Clean JSON processing
✔ Error handling for invalid cities
✔ Modular and readable code

---

## ⚠️ Edge Cases Handled

* Invalid city names
* API failures
* Missing weather data

---

## 🎥 Demo

👉 Screen recording showing:

* Code execution
* API response
* Output file generation

---

## 📈 Future Improvements

* Add UI Dashboard
* Integrate SMS/Email notifications
* Add delivery ETA prediction
* Use database instead of JSON

---

## 🙌 Author

**Deepthi Singareddy**

---

## ⭐ Final Note

This project demonstrates practical automation using APIs and data processing, simulating real-world logistics decision-making.

---
