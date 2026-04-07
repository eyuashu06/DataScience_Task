# 📊 Statistical Engine Project

## 🚀 Project Overview
This project implements a custom **Statistical Engine** using only Python standard libraries. It processes raw one-dimensional numerical data and provides key statistical computations such as:

- Central Tendency (Mean, Median, Mode)
- Dispersion (Variance, Standard Deviation)
- Outlier Detection (Z-score method)
- Monte Carlo Simulation (Server crash probability)

Additionally, the project demonstrates real-world statistical concepts like the **Law of Large Numbers** using simulation.

---

## 🧮 Mathematical Logic

### 1. Variance Formula

Variance measures how spread out the data points are from the mean.

- **Population Variance:**
  
  σ² = Σ(x - μ)² / N

- **Sample Variance (with Bessel’s Correction):**
  
  s² = Σ(x - x̄)² / (N - 1)

Where:
- x = each data point
- μ = population mean
- x̄ = sample mean
- N = number of data points

👉 In this project:
- If `is_sample=True`, we divide by **(N - 1)**
- If `is_sample=False`, we divide by **N**

---

### 2. Median (Even vs Odd Handling)

To compute the median:

- **Odd number of elements:**
  - Select the middle value after sorting

- **Even number of elements:**
  - Take the average of the two middle values

Example:
- `[1, 2, 3]` → Median = 2  
- `[1, 2, 3, 4]` → Median = (2 + 3) / 2 = 2.5  

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/statistical_engine.git
cd statistical_engine