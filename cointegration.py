from statsmodels.tsa.vector_ar.vecm import coint_johansen


def run_johansen(prices):

    rank = 0

    johansen_test = coint_johansen(prices,det_order=0,k_ar_diff=1)

    Trace_statistics = johansen_test.lr1

    print(Trace_statistics)

    percentage_ninety_five = (
        johansen_test.cvt[:, 1]
    )

    print("95% critical value")

    print(percentage_ninety_five)

    for i in range(
        len(Trace_statistics)
    ):

        if (
            Trace_statistics[i]
            >
            percentage_ninety_five[i]
        ):

            rank = rank + 1

    print("rank is ")

    print(rank)

    print("\nCointegration Vectors ")

    print(johansen_test.evec)

    return johansen_test, rank


def build_spread(prices,johansen_test):

    first_vector = (
        johansen_test.evec[:, 0]
    )

    print(first_vector)

    spread = (
        prices.values@first_vector
    )

    spread_mean = spread.mean()

    spread_std = spread.std()

    z_score = (
        spread - spread_mean
    ) / spread_std

    print("\nLatest Z-Score:")

    print(z_score[-1])

    return (
        spread,
        spread_mean,
        spread_std,
        z_score
    )