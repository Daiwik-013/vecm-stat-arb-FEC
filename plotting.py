import matplotlib.pyplot as plt


def plot_prices(prices):

    prices.plot(figsize=(12, 6))
    plt.title("Stock Prices")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.savefig("graphs/Stock Prices.png")
    plt.show()


def plot_spread(spread):
    plt.figure(figsize=(12, 6))
    plt.plot(spread)
    plt.title("Cointegrated Spread")
    plt.xlabel("Time")
    plt.ylabel("Spread")
    plt.axhline(spread.mean(),color='red',linestyle='--')

    plt.savefig(
        "graphs/Spread Analysis.png"
    )
    plt.show()


def plot_zscore(z_score):
    plt.figure(figsize=(12, 6))
    plt.plot(z_score)
    plt.axhline(2,color='red',linestyle='--')

    plt.axhline(-2,color='green',linestyle='--')

    plt.axhline(0,color='black')
    plt.title("Z-Score of Spread")
    plt.xlabel("Time")
    plt.ylabel("Z-Score")
    plt.savefig("graphs/Z Score.png")
    plt.show()


def plot_strategy(cumulative_returns):

    plt.figure(figsize=(12, 6))
    plt.plot(cumulative_returns)

    plt.title("Strategy Performance")
    plt.xlabel("Time")
    plt.ylabel("Cumulative Returns")
    plt.savefig("graphs/Strategy Performance.png")
    plt.show()


def plot_rolling_rank(ranks_through_time):

    plt.figure(figsize=(12, 6))
    plt.plot(ranks_through_time)
    plt.title("Rolling Cointegration Rank")
    plt.xlabel("Time")
    plt.ylabel("Rank")
    plt.savefig("graphs/Rolling rank.png")
    plt.show()