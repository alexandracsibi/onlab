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
bar_width = 0.2
r = [0]

# Create subplots with three touching bars for each type of latency
fig, axs = plt.subplots(nrows=1, ncols=3, figsize=(15, 6))
plt.rcParams['font.size'] = 15

# Minimum Latency subplot
axs[0].bar(r, [eu_min_latency], color='purple', width=bar_width)
axs[0].bar([r[0] + bar_width], [us_min_latency], color='blue', width=bar_width)
axs[0].set_xticks([r[0], r[0] + bar_width])
axs[0].set_xticklabels(['Közvetett', 'Közvetlen'])
axs[0].set_xlabel('Elérési mód')
axs[0].set_ylabel('Minimum késleltetés (ms)')
axs[0].set_title('Minimum késleltetés')

# Average Latency subplot
axs[1].bar(r, [eu_avg_latency], color='purple', width=bar_width)
axs[1].bar([r[0] + bar_width], [us_avg_latency], color='blue', width=bar_width)
axs[1].set_xticks([r[0], r[0] + bar_width])
axs[1].set_xticklabels(['Közvetett', 'Közvetlen'])
axs[1].set_xlabel('Elérési mód')
axs[1].set_ylabel('Átlagos késleltetés (ms)')
axs[1].set_title('Átlagos késleltetés')

# Maximum Latency subplot
axs[2].bar(r, [eu_max_latency], color='purple', width=bar_width)
axs[2].bar([r[0] + bar_width], [us_max_latency], color='blue', width=bar_width)
axs[2].set_xticks([r[0], r[0] + bar_width])
axs[2].set_xticklabels(['Közvetett', 'Közvetlen'])
axs[2].set_xlabel('Elérési mód')
axs[2].set_ylabel('Maximum késleltetés (ms)')
axs[2].set_title('Maximum Késleltetés')

# Adjust the spacing between subplots
plt.subplots_adjust(wspace=0.4)

plt.savefig('latency-comparison.png', dpi=300)
plt.show()
