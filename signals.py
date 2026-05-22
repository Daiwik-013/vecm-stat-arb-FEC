def generate_signals(z_score):

    position = 0

    signals = []

    for z in z_score:

        if z > 2:

            position = -1

        elif z < -2:

            position = 1

        elif abs(z) < 0.5:

            position = 0

        signals.append(position)

    print("\nLatest Signal:")

    print(signals[-1])

    return signals