from statsmodels.tsa.vector_ar.vecm import coint_johansen


def monitor_cointegration_rank(prices):
    window_size = 500
    ranks_through_time = []
    for start in range(0,len(prices) - window_size):

        window_data = prices.iloc[start:start + window_size]
        test = coint_johansen(window_data,det_order=0,k_ar_diff=1)
        trace_stats = test.lr1
        critical_vals = (test.cvt[:, 1])
        rolling_rank = 0
        for i in range(len(trace_stats)):
            if (trace_stats[i]>critical_vals[i]):
                rolling_rank += 1

        ranks_through_time.append(rolling_rank)

    if ranks_through_time[-1] == 0:

        print("WARNING: Cointegration breakdown detected.")

        print("Liquidating all positions.")

    return ranks_through_time