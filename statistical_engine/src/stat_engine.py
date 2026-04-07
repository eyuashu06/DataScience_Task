from typing import List, Union
import math


Number = Union[int, float]


class StatEngine:
    def __init__(self, data):
        """
        Initialize with raw data and clean it.
        """
        self.data = self._clean_data(data)

        if len(self.data) == 0:
            raise ValueError("Data cannot be empty after cleaning.")

    # --------------------------
    # Data Cleaning
    # --------------------------
    def _clean_data(self, data):
        """
        Remove invalid entries and ensure numeric values only.
        """
        if not isinstance(data, (list, tuple)):
            raise TypeError("Input data must be a list or tuple.")

        cleaned = []

        for item in data:
            if isinstance(item, (int, float)):
                cleaned.append(item)
            else:
                # Try converting string numbers
                try:
                    converted = float(item)
                    cleaned.append(converted)
                except (ValueError, TypeError):
                    raise TypeError(
                        f"Invalid data type detected: {item} (must be numeric)"
                    )

        return cleaned

    # --------------------------
    # Central Tendency
    # --------------------------
    def get_mean(self) -> float:
        return sum(self.data) / len(self.data)

    def get_median(self) -> float:
        sorted_data = sorted(self.data)
        n = len(sorted_data)
        mid = n // 2

        if n % 2 == 0:
            return (sorted_data[mid - 1] + sorted_data[mid]) / 2
        else:
            return sorted_data[mid]

    def get_mode(self):
        frequency = {}

        for num in self.data:
            frequency[num] = frequency.get(num, 0) + 1

        max_freq = max(frequency.values())

        # If all values appear once → no mode
        if max_freq == 1:
            return "No mode (all values are unique)"

        modes = [k for k, v in frequency.items() if v == max_freq]
        return modes

    # --------------------------
    # Dispersion
    # --------------------------
    def get_variance(self, is_sample=True) -> float:
        n = len(self.data)

        if n < 2 and is_sample:
            raise ValueError("Sample variance requires at least 2 data points.")

        mean = self.get_mean()

        squared_diff_sum = 0
        for x in self.data:
            squared_diff_sum += (x - mean) ** 2

        if is_sample:
            return squared_diff_sum / (n - 1)  # Bessel's correction
        else:
            return squared_diff_sum / n

    def get_standard_deviation(self, is_sample=True) -> float:
        variance = self.get_variance(is_sample)
        return math.sqrt(variance)

    # --------------------------
    # Outlier Detection
    # --------------------------
    def get_outliers(self, threshold=2) -> List[Number]:
        mean = self.get_mean()
        std_dev = self.get_standard_deviation()

        outliers = []

        for x in self.data:
            z_score = abs((x - mean) / std_dev)
            if z_score > threshold:
                outliers.append(x)

        return outliers
    
