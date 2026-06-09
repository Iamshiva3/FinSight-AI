import { useState } from "react";
import axios from "axios";
import StockChart from "./components/StockChart";
import "./App.css";

function App() {
  const [symbol, setSymbol] = useState("");
  const [company, setCompany] = useState(null);
  const [loading, setLoading] = useState(false);
  const [news, setNews] = useState(null);
  const [chartData, setChartData] = useState(null);
  const [recommendation, setRecommendation] = useState(null);
  const [newsSentiment, setNewsSentiment] = useState(null);
  const [fundamentals, setFundamentals] = useState(null);
  const [aiAnalysis, setAiAnalysis] = useState(null);
  const fetchCompany = async () => {
    try {
      setLoading(true);

  const response = await axios.get(
  `http://127.0.0.1:8000/api/company/${symbol}`
);

setCompany(response.data);

const chartResponse = await axios.get(
  `http://127.0.0.1:8000/api/historical/${symbol}`
);

setChartData(chartResponse.data);

const recResponse = await axios.get(
  `http://127.0.0.1:8000/api/recommendation/${symbol}`
);

setRecommendation(recResponse.data);
const newsResponse = await axios.get(
  `http://127.0.0.1:8000/api/news-sentiment/${symbol}`
);

setNewsSentiment(newsResponse.data);

const fundamentalsResponse = await axios.get(
  `http://127.0.0.1:8000/api/fundamentals/${symbol}`
);

setFundamentals(fundamentalsResponse.data);
const aiResponse = await axios.get(
  `http://127.0.0.1:8000/api/ai-analysis/${symbol}`
);

setAiAnalysis(aiResponse.data);

} catch (error) {
    console.error(error);

    if (error.response) {
        alert(`API Error: ${error.response.status}`);
    } else {
        alert(error.message);
    }
  } finally {
    setLoading(false);
  }
};

  return (
    <div className="app">
      <h1>📈 FinSight AI</h1>

      <div className="search-box">
        <input
          type="text"
          placeholder="Enter Stock Symbol"
          value={symbol}
          onChange={(e) => setSymbol(e.target.value)}
        />

        <button onClick={fetchCompany}>
          Search
        </button>
      </div>

      {loading && <h3>Loading...</h3>}

      {company && (
        <div className="card">
          <h2>{company.name}</h2>

          <div className="grid">
            <div className="info-box">
              <h4>Symbol</h4>
              <p>{company.symbol}</p>
            </div>

            <div className="info-box">
              <h4>Current Price</h4>
              <p>${company.currentPrice}</p>
            </div>

            <div className="info-box">
              <h4>Sector</h4>
              <p>{company.sector}</p>
            </div>

            <div className="info-box">
              <h4>Market Cap</h4>
              <p>{company.marketCap}</p>
            </div>

            <div className="info-box">
              <h4>P/E Ratio</h4>
              <p>{company.peRatio}</p>
            </div>

            <div className="info-box">
              <h4>EPS</h4>
              <p>{company.eps}</p>
            </div>

            <div className="info-box">
              <h4>Profit Margin</h4>
              <p>{company.profitMargin}</p>
            </div>

            <div className="info-box">
              <h4>Revenue Growth</h4>
              <p>{company.revenueGrowth}</p>
            </div>

            <div className="info-box">
              <h4>52W High</h4>
              <p>{company.fiftyTwoWeekHigh}</p>
            </div>

            <div className="info-box">
              <h4>52W Low</h4>
              <p>{company.fiftyTwoWeekLow}</p>
            </div>
          </div>
        </div>
      )}
      {chartData && (
        <div className="card">
          <h2>📈 Price History</h2>
          <StockChart chartData={chartData} />
        </div>
     )}
     {recommendation && (
       <div className="card">
         <h2>🤖 AI Recommendation</h2>

         <h1
            style={{
              color:
                recommendation.recommendation === "BUY"
                  ? "lime"
                  : recommendation.recommendation === "HOLD"
                  ? "orange"
                  : "red",
            }}
         >
           {recommendation.recommendation}
         </h1>

         <h3>Score: {recommendation.score}/100</h3>
      </div>
)}
      {newsSentiment && (
  <div className="card">
    <h2>📰 News Sentiment</h2>

    <p>🟢 Positive: {newsSentiment.positive}</p>
    <p>🟡 Neutral: {newsSentiment.neutral}</p>
    <p>🔴 Negative: {newsSentiment.negative}</p>

    <h3>
      Overall Sentiment: {newsSentiment.overall}
    </h3>
  </div>
)}
{newsSentiment && (
  <div className="card">
    <h2>📰 News Sentiment</h2>

    <p>🟢 Positive: {newsSentiment.positive}</p>
    <p>🟡 Neutral: {newsSentiment.neutral}</p>
    <p>🔴 Negative: {newsSentiment.negative}</p>

    <h3>
      Overall Sentiment: {newsSentiment.overall}
    </h3>
  </div>
)}
{newsSentiment && (
  <div className="card">
    <h2>📰 Latest Headlines</h2>

    {newsSentiment.headlines.map((headline, index) => (
      <p key={index}>
        • {headline}
      </p>
    ))}
  </div>
)}
{fundamentals && (
  <div className="card">
    <h2>📊 Fundamental Analysis</h2>

    <p>P/E Ratio: {fundamentals.peRatio}</p>
    <p>P/B Ratio: {fundamentals.pbRatio}</p>
    <p>ROE: {fundamentals.roe}</p>
    <p>Profit Margin: {fundamentals.profitMargin}</p>
    <p>Debt To Equity: {fundamentals.debtToEquity}</p>
  </div>
)}
{aiAnalysis && (
  <div className="card">
    <h2>🤖 AI Analysis</h2>

    <div style={{ whiteSpace: "pre-line" }}>
      {aiAnalysis.analysis}
    </div>
  </div>
)}

    </div>
  );
}

export default App;