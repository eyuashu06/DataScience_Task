import random


def simulate_crashes(days: int, crash_probability: float = 0.045):
    """
    Simulate server crashes over a given number of days.
    Returns:
        total_crashes, estimated_probability
    """
    crashes = 0

    for _ in range(days):
        # random.random() → value between 0 and 1
        if random.random() < crash_probability:
            crashes += 1

    estimated_probability = crashes / days
    return crashes, estimated_probability


def run_experiments():
    test_days = [100, 1000, 10000]

    print("---- Monte Carlo Server Crash Simulation ----")

    for days in test_days:
        crashes, prob = simulate_crashes(days)
        print(f"\nDays: {days}")
        print(f"Total Crashes: {crashes}")
        print(f"Estimated Probability: {prob:.4f}")