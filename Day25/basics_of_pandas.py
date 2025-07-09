import pandas

# Read the CSV file
data = pandas.read_csv("weather_data.csv")
print(type(data))
# <class 'pandas.core.frame.DataFrame'>
print(data)

# Convert to dictionary
data_dict = data.to_dict()
print(data_dict)

# Get temperature as list and calculate average manually
temp_list = data["temp"].to_list()
print(temp_list)
# [12, 14, 15, 14, 21, 22, 24]
avg_t = sum(temp_list)/len(temp_list)
print(f"The average temperature is: {avg_t}")

# Calculate average using pandas method
avg_temp = data["temp"].mean()
print(f"The average temperature is: {avg_temp}")


temp = data["temp"]

# Basic Statistical Methods
print("\nBASIC STATISTICAL METHODS:")
print("-" * 30)
print(f"median(): {temp.median()}")       # Middle value
print(f"mode(): {temp.mode().iloc[0]}")       # Most frequent value

# Variability
print(f"std(): {temp.std():.2f}")             # Standard deviation
print(f"var(): {temp.var():.2f}")             # Variance
print(f"sem(): {temp.sem():.2f}")             # Standard error of mean

# Range and Extremes
print(f"min(): {temp.min()}")                 # Minimum value
print(f"max(): {temp.max()}")                 # Maximum value
print(f"range: {temp.max() - temp.min()}")    # Range (max - min)

# Percentiles and Quartiles
print(f"quantile(0.25): {temp.quantile(0.25):.2f}")  # 25th percentile (Q1)
print(f"quantile(0.5): {temp.quantile(0.5):.2f}")    # 50th percentile (median)
print(f"quantile(0.75): {temp.quantile(0.75):.2f}")  # 75th percentile (Q3)

print("\n" + "="*50 + "\n")

print("AGGREGATION METHODS:")
print("-" * 30)

# Sum and Count
print(f"sum(): {temp.sum()}")                 # Sum of all values
print(f"count(): {temp.count()}")             # Count of non-null values
print(f"size: {temp.size}")                   # Total number of elements
print(f"nunique(): {temp.nunique()}")         # Number of unique values

# Product
print(f"prod(): {temp.prod()}")               # Product of all values

# Cumulative operations
print(f"cumsum(): {temp.cumsum().tolist()}")  # Cumulative sum
print(f"cumprod(): {temp.cumprod().tolist()}")# Cumulative product
print(f"cummin(): {temp.cummin().tolist()}")  # Cumulative minimum
print(f"cummax(): {temp.cummax().tolist()}")  # Cumulative maximum

print("\n" + "="*50 + "\n")

print("ADVANCED STATISTICAL METHODS:")
print("-" * 30)

# Moments and Shape
print(f"skew(): {temp.skew():.3f}")           # Skewness (asymmetry)
print(f"kurtosis(): {temp.kurtosis():.3f}")   # Kurtosis (tail heaviness)

print("Note: Humidity correlation skipped - column not in original data")

print("\n" + "="*50 + "\n")

print("COMPREHENSIVE SUMMARY METHODS:")
print("-" * 30)

# Multiple statistics at once
print("describe() - Complete statistical summary:")
print(temp.describe())
print()
print("agg() - Custom aggregations:")
result = temp.agg(['mean', 'std', 'min', 'max'])
print(result)
print()

print("agg() with custom functions:")
result = temp.agg(['mean', lambda x: x.max() - x.min()])
print(result)

print("\n" + "="*50 + "\n")

print("DATAFRAME-SPECIFIC METHODS:")
print("-" * 30)

# Apply to entire DataFrame
print("DataFrame.mean() - mean of all numeric columns:")
print(data.mean(numeric_only=True))
print()

print("DataFrame.describe() - summary of all numeric columns:")
print(data.describe())
print()

# FIXED: Remove humidity from agg since it doesn't exist in original data
print("DataFrame.agg() - multiple functions on temp column:")
result = data.agg({
    'temp': ['mean', 'std', 'min', 'max']
})
print(result)

print("\n" + "="*50 + "\n")

print("ROLLING AND EXPANDING WINDOW METHODS:")
print("-" * 30)

# Rolling (moving) statistics
print("rolling(3).mean() - 3-day moving average:")
print(temp.rolling(3).mean())
print()

print("rolling(3).std() - 3-day rolling standard deviation:")
print(temp.rolling(3).std())
print()

# Expanding window (cumulative from start)
print("expanding().mean() - expanding mean:")
print(temp.expanding().mean())

print("\n" + "="*50 + "\n")

print("GROUPBY AGGREGATIONS:")
print("-" * 30)

# FIXED: Only group by condition and analyze temp (no humidity)
grouped_stats = data.groupby('condition').agg({
    'temp': ['mean', 'std', 'count']
})
print("Grouped statistics by weather condition:")
print(grouped_stats)

print("\n" + "="*50 + "\n")

print("PRACTICAL EXAMPLES:")
print("-" * 30)

# Find days with temperature above average
avg_temp = data['temp'].mean()
hot_days = data[data['temp'] > avg_temp]
print(f"Days with temperature above average ({avg_temp:.1f}°C):")
print(hot_days[['day', 'temp']].to_string(index=False))
print()

# Temperature statistics by condition
print("Temperature statistics by weather condition:")
temp_by_condition = data.groupby('condition')['temp'].agg(['count', 'mean', 'min', 'max'])
print(temp_by_condition)
print()

# Percentile analysis
print("Temperature percentiles:")
percentiles = [10, 25, 50, 75, 90]
for p in percentiles:
    value = data['temp'].quantile(p/100)
    print(f"{p}th percentile: {value:.1f}°C")