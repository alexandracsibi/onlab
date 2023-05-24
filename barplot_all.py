import pandas as pd
import matplotlib.pyplot as plt

# Read the data from server_report_eu.csv and server_report_us.csv
df_eu = pd.read_csv('server_report_eu.csv', delimiter=',')
df_us = pd.read_csv('server_report_us.csv', delimiter=',')

# Calculate minimum, average, and maximum latency for EU and US
eu_min_latency = df_eu['Latency min'].min()
us_min_latency = df_us['Latency min'].min()
eu_avg_latency = df_eu['Latency avg'].mean()
us_avg_latency = df_us['Latency avg'].mean()
eu_max_latency = df_eu['Latency max'].max()
us_max_latency = df_us['Latency max'].max()

# Set the bar width and the positions of the bars on the x-axis
bar_width = 0.1
r = [0]

plt.figure(figsize=(12, 5))
plt.rcParams['font.size'] = 17

# Create a bar plot with three touching bars for each type of latency
plt.bar(r, [eu_min_latency], color='purple', width=bar_width, label='Indirect (EU)')
plt.bar([val + bar_width for val in r], [us_min_latency], color='blue', width=bar_width, label='Direct (US)')
plt.bar([val + 2 * bar_width for val in r], [eu_avg_latency], color='purple', width=bar_width)
plt.bar([val + 3 * bar_width for val in r], [us_avg_latency], color='blue', width=bar_width)
plt.bar([val + 4 * bar_width for val in r], [eu_max_latency], color='purple', width=bar_width)
plt.bar([val + 5 * bar_width for val in r], [us_max_latency], color='blue', width=bar_width)

# Customize the plot
plt.ylabel('Value')
plt.title('Latency Comparison (EU vs US)')
plt.legend()

# Add category labels below the bars
plt.text(r[0] + bar_width / 2, -30, 'Minimum Latency', ha='center')
plt.text(r[0] + 5 * bar_width / 2, -30, 'Average Latency', ha='center')
plt.text(r[0] + 9 * bar_width / 2, -30, 'Maximum Latency', ha='center')

plt.xticks([])  # Remove x-axis tick marks

plt.savefig('latency-comp.png', dpi=300)
plt.show()
