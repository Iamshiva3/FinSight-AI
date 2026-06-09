# 📈 FinSight AI

FinSight AI is an AI-powered stock market analysis platform that helps investors analyze stocks using real-time market data, technical indicators, sentiment analysis, and AI-generated insights.

## 🚀 Features

### 📊 Stock Analysis

* Real-time stock price tracking
* Historical stock price charts
* Company information and overview
* Market capitalization and sector analysis

### 📈 Technical Analysis

* Historical price visualization
* Stock performance tracking
* Buy / Hold / Sell recommendations
* AI-based stock scoring

### 📰 News Sentiment Analysis

* Latest stock-related news
* Sentiment analysis using NLP
* Positive, Negative, and Neutral sentiment classification

### 🤖 AI-Powered Insights

* Gemini AI integration
* Automated stock analysis
* Investment recommendations
* Risk assessment and market outlook

### 🌍 Multi-Market Support

* US Stocks (NASDAQ, NYSE)
* Indian Stocks (NSE)

---

## 🛠️ Tech Stack

### Frontend

* React.js
* Axios
* Chart.js
* React ChartJS 2

### Backend

* FastAPI
* Python
* Uvicorn

### Data Sources

* Yahoo Finance (yFinance)
* RSS News Feeds

### AI & NLP

* Google Gemini API
* VADER Sentiment Analysis

---

## 📂 Project Structure

```text
FinSight-AI/
│
├── frontend/
│   ├── src/
│   ├── public/
│   └── package.json
│
├── backend/
│   ├── app.py
│   ├── requirements.txt
│   ├── .env
│   └── venv/
│
├── README.md
└── .gitignore
```

## ⚙️ Installation

### 1️⃣ Clone Repository

```bash
git clone https://github.com/Iamshiva3/FinSight-AI.git
cd FinSight-AI
```

### 2️⃣ Backend Setup

```bash
cd backend
python -m venv venv
```

Activate Environment:

Windows:

```bash
venv\Scripts\activate
```

Install Dependencies:

```bash
pip install -r requirements.txt
```

Create `.env` file:

```env
GEMINI_API_KEY=YOUR_API_KEY_HERE
```

Run Backend:

```bash
python -m uvicorn app:app --reload
```

Backend URL:

```text
http://127.0.0.1:8000
```

---

### 3️⃣ Frontend Setup

```bash
cd frontend
npm install
npm start
```

Frontend URL:

```text
http://localhost:3000
```

---

## 🔍 Supported Stock Symbols

### US Stocks

```text
AAPL
TSLA
MSFT
NVDA
GOOGL
AMZN
```

### Indian Stocks

```text
RELIANCE.NS
TCS.NS
INFY.NS
HDFCBANK.NS
ICICIBANK.NS
SBIN.NS
```

---

## 🎯 Future Enhancements

* Portfolio Tracker
* Watchlist Management
* Stock Price Prediction using Machine Learning
* PDF Report Generation
* User Authentication
* Cloud Deployment
* Mobile Responsive Design

---

## 👨‍💻 Author

Shiva

GitHub:
https://github.com/Iamshiva3

---

## 📜 License

This project is developed for educational and learning purposes.
