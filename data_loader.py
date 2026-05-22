import yfinance as yf


def load_data():

    stocks = ["AAPL","MSFT","NVDA","AMD","QCOM","INTC"]

    data = yf.download(
        stocks,
        start="2022-01-01",
        end="2025-01-01"
    )

    prices = data["Close"]

    return prices