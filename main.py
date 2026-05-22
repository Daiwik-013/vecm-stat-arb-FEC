from data_loader import load_data

from cointegration import (run_johansen,build_spread)

from signals import (generate_signals)

from backtester import (backtest_strategy,performance_metrics)

from rank_monitor import (monitor_cointegration_rank)

from plotting import (plot_prices,plot_spread,plot_zscore,plot_strategy,plot_rolling_rank)


prices = load_data()

johansen_test, rank = (run_johansen(prices))

(spread,spread_mean,spread_std,z_score) = build_spread(prices,johansen_test)

signals = generate_signals(z_score)

(cumulative_returns,spread_returns) = backtest_strategy(spread,signals)

performance_metrics(cumulative_returns,spread_returns)

ranks_through_time = (monitor_cointegration_rank(prices))

plot_prices(prices)
plot_spread(spread)
plot_zscore(z_score)
plot_strategy(cumulative_returns)

plot_rolling_rank(ranks_through_time)