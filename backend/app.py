# backend/main.py
import os
import google.generativeai as genai
import feedparser
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import yfinance as yf
from dotenv import load_dotenv

load_dotenv()
print("API KEY:", os.getenv("GEMINI_API_KEY"))

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://localhost:3001",
        "http://localhost:3002",
        "http://127.0.0.1:3000",
        "http://127.0.0.1:3001",
        "http://127.0.0.1:3002"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Sample company data
COMPANIES = {
    "AAPL": "Apple Inc.",
    "TSLA": "Tesla Inc.",
    "RELIANCE.NS": "Reliance Industries",
    "TCS.NS": "Tata Consultancy Services",
    "INFY.NS": "Infosys Limited",
    "HDFCBANK.NS": "HDFC Bank Limited"
}

@app.get("/api/health")
def health_check():
    return {"status": "ok"}

@app.get("/api/company/{symbol}")
def get_company_data(symbol: str):
    """Get company overview and basic data"""
    if symbol.upper() not in COMPANIES:
        return {"error": "Company not found"}
    
    try:
        ticker = yf.Ticker(symbol)
        info = ticker.info
        
        return {
            "symbol": symbol.upper(),
            "name": info.get("longName", "N/A"),
            "sector": info.get("sector", "N/A"),
            "industry": info.get("industry", "N/A"),
            "marketCap": info.get("marketCap", "N/A"),
            "currentPrice": info.get("currentPrice", "N/A"),

            "peRatio": info.get("trailingPE", "N/A"),
            "eps": info.get("trailingEps", "N/A"),
            "dividendYield": info.get("dividendYield", "N/A"),
            "profitMargin": info.get("profitMargins", "N/A"),
            "revenueGrowth": info.get("revenueGrowth", "N/A"),
            "fiftyTwoWeekHigh": info.get("fiftyTwoWeekHigh", "N/A"),
            "fiftyTwoWeekLow": info.get("fiftyTwoWeekLow", "N/A"),

            "currency": info.get("currency", "USD")
        }
    except Exception as e:
        return {"error": str(e)}

@app.get("/api/stock-price/{symbol}")
def get_stock_price(symbol: str):
    """Get current stock price"""
    try:
        ticker = yf.Ticker(symbol)
        data = ticker.history(period="1d")
        
        if data.empty:
            return {"error": "No data found"}
        
        return {
            "symbol": symbol,
            "price": float(data['Close'].iloc[-1]),
            "open": float(data['Open'].iloc[-1]),
            "high": float(data['High'].iloc[-1]),
            "low": float(data['Low'].iloc[-1]),
            "volume": float(data['Volume'].iloc[-1])
        }
    except Exception as e:
        return {"error": str(e)}

@app.get("/api/historical/{symbol}")
def get_historical_data(symbol: str, period: str = "1y"):
    """Get historical data for charts"""
    try:
        ticker = yf.Ticker(symbol)
        data = ticker.history(period=period)
        
        return {
            "symbol": symbol,
            "dates": data.index.strftime('%Y-%m-%d').tolist(),
            "closes": data['Close'].round(2).tolist(),
            "volumes": data['Volume'].tolist()
        }
    except Exception as e:
        return {"error": str(e)}
@app.get("/api/recommendation/{symbol}")
def get_recommendation(symbol: str):
    try:
        ticker = yf.Ticker(symbol)
        info = ticker.info

        pe = info.get("trailingPE", 0)
        growth = info.get("revenueGrowth", 0)
        margin = info.get("profitMargins", 0)

        score = 0

        if pe and pe < 30:
            score += 30

        if growth and growth > 0.10:
            score += 35

        if margin and margin > 0.15:
            score += 35

        if score >= 70:
            recommendation = "BUY"
        elif score >= 40:
            recommendation = "HOLD"
        else:
            recommendation = "SELL"

        return {
            "score": score,
            "recommendation": recommendation
        }

    except Exception as e:
        return {"error": str(e)}
@app.get("/api/news-sentiment/{symbol}")
def get_news_sentiment(symbol: str):

    analyzer = SentimentIntensityAnalyzer()

    feed = feedparser.parse(
        f"https://news.google.com/rss/search?q={symbol}+stock"
    )

    positive = 0
    negative = 0
    neutral = 0

    headlines = []

    for entry in feed.entries[:10]:

        title = entry.title

        score = analyzer.polarity_scores(title)["compound"]

        headlines.append(title)

        if score > 0.05:
            positive += 1
        elif score < -0.05:
            negative += 1
        else:
            neutral += 1

    if positive > negative:
        sentiment = "Positive"
    elif negative > positive:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    return {
        "positive": positive,
        "negative": negative,
        "neutral": neutral,
        "overall": sentiment,
        "headlines": headlines
    }
@app.get("/api/news-sentiment/{symbol}")
def get_news_sentiment(symbol: str):

    analyzer = SentimentIntensityAnalyzer()

    feed = feedparser.parse(
        f"https://news.google.com/rss/search?q={symbol}+stock"
    )

    positive = 0
    negative = 0
    neutral = 0

    headlines = []

    for entry in feed.entries[:10]:

        title = entry.title

        score = analyzer.polarity_scores(title)["compound"]

        headlines.append(title)

        if score > 0.05:
            positive += 1
        elif score < -0.05:
            negative += 1
        else:
            neutral += 1

    if positive > negative:
        sentiment = "Positive"
    elif negative > positive:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    return {
        "positive": positive,
        "negative": negative,
        "neutral": neutral,
        "overall": sentiment,
        "headlines": headlines
    }
@app.get("/api/fundamentals/{symbol}")
def get_fundamentals(symbol: str):
    try:
        ticker = yf.Ticker(symbol)
        info = ticker.info

        return {
            "peRatio": info.get("trailingPE"),
            "pbRatio": info.get("priceToBook"),
            "roe": info.get("returnOnEquity"),
            "profitMargin": info.get("profitMargins"),
            "debtToEquity": info.get("debtToEquity")
        }

    except Exception as e:
        return {"error": str(e)}
@app.get("/api/ai-analysis/{symbol}")
def ai_analysis(symbol: str):
    try:
        ticker = yf.Ticker(symbol)
        info = ticker.info

        company = info.get("longName", symbol)
        sector = info.get("sector", "")
        pe = info.get("trailingPE", "N/A")
        market_cap = info.get("marketCap", "N/A")
        margin = info.get("profitMargins", "N/A")

        model = genai.GenerativeModel("gemini-1.5-flash-lite")
        prompt = f"""
        Analyze this stock.

        Company: {company}
        Sector: {sector}
        P/E Ratio: {pe}
        Market Cap: {market_cap}
        Profit Margin: {margin}

        Provide:
        - Strengths
        - Risks
        - Short-term outlook
        - Long-term outlook
        - Buy/Hold/Sell recommendation

        Keep under 200 words.
        """

        response = model.generate_content(prompt)

        return {
            "analysis": response.text
        }

    except Exception as e:
        return {
        "analysis": f"""
    AI service unavailable.

    Company: {company}
    Sector: {sector}

    P/E Ratio: {pe}

    Recommendation: HOLD

    Reason:
    The stock has stable fundamentals but AI analysis
    is temporarily unavailable.
    """
       }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)