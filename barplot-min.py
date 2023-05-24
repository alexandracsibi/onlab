import pandas as pd
import matplotlib.pyplot as plt

# Read the data from server_report_eu.csv and server_report_us.csv
df_eu = pd.read_csv('server_report_eu.csv', delimiter=',')
df_us = pd.read_csv('server_report_us.csv', delimiter=',')

# Calculate average latency for EU and US
eu_avg_latency = df_eu['Latency min'].min()
us_avg_latency = df_us['Latency min'].min()

# Set the bar width and the positions of the bars on the x-axis
bar_width = 0.2
r = [0]

plt.figure(figsize=(10, 6))
plt.rcParams['font.size'] = 15

# Create a bar plot with two touching bars
plt.bar(r, [eu_avg_latency], color='purple', width=bar_width)
plt.bar([r[0] + bar_width], [us_avg_latency], color='blue', width=bar_width)

# Customize the plot
plt.xticks([r[0], r[0] + bar_width], ['Indirect (EU)', 'Direct (US)'])
plt.xlabel('Methods')
plt.ylabel('Minimum Latency')
plt.title('Minimum Latency Comparison (EU vs US)')

plt.savefig('latency-min_comparison.png', dpi=300) 
