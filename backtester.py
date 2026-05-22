import pandas as pd


def backtest_strategy(
    spread,
    signals
):

    spread_returns = []

    for i in range(1,len(spread)):

        change = (spread[i]-spread[i - 1])

        transaction_cost = 0.01

        borrow_cost = 0.005

        pnl = (signals[i - 1]*change)

        if signals[i - 1] != 0:
         pnl -= transaction_cost

        if signals[i - 1] == -1:

            pnl -= borrow_cost

        spread_returns.append(pnl)

    cumulative_returns = (pd.Series(spread_returns).cumsum())

    return (cumulative_returns,spread_returns)


def performance_metrics(
    cumulative_returns,
    spread_returns
):

    total_return = (
        cumulative_returns.iloc[-1]
    )

    returns_series = pd.Series(
        spread_returns
    )

    sharpe_ratio = (returns_series.mean()/returns_series.std()) * (252 ** 0.5)

    rolling_max = (
        cumulative_returns.cummax()
    )

    drawdown = (cumulative_returns- rolling_max)

    max_drawdown = (drawdown.min())

    print("\nTotal Return:")

    print(total_return)

    print("\nSharpe Ratio:")

    print(sharpe_ratio)

    print("\nMax Drawdown:")

    print(max_drawdown)

    return (total_return,sharpe_ratio,max_drawdown)