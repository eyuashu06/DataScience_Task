import json
import os
from src.stat_engine import StatEngine
from src.monte_carlo import simulate_crashes, run_experiments


def load_data():
    base_dir = os.path.dirname(__file__)
    file_path = os.path.join(base_dir, "data", "sample_salaries.json")

    with open(file_path) as f:
        return json.load(f)


def main():
    data = load_data()

    # -------- Monte Carlo Experiments --------
    print("----- Monte Carlo Simulation (Experiments) -----")
    run_experiments()

    # -------- Statistical Analysis --------
    engine = StatEngine(data)

    print("\n----- Statistical Analysis -----")
    print("Mean:", engine.get_mean())
    print("Median:", engine.get_median())
    print("Mode:", engine.get_mode())
    print("Variance:", engine.get_variance())
    print("Standard Deviation:", engine.get_standard_deviation())
    print("Outliers:", engine.get_outliers())

    # -------- Single Simulation --------
    print("\n----- Monte Carlo Simulation (Single Run) -----")

    crashes, probability = simulate_crashes(1000)

    print(f"Days: 1000")
    print(f"Total Crashes: {crashes}")
    print(f"Estimated Crash Probability: {probability:.4f}")


if __name__ == "__main__":
    main()