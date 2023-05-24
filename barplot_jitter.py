import pandas as pd
import matplotlib.pyplot as plt

# Read the data from server_report_eu.csv and server_report_us.csv
df_eu = pd.read_csv('server_report_eu.csv', delimiter=',')
df_us = pd.read_csv('server_report_us.csv', delimiter=',')

# Calculate minimum, average, and maximum jitter for EU and US
eu_min_jitter = df_eu['Jitter'].min()
us_min_jitter = df_us['Jitter'].min()
eu_avg_jitter = df_eu['Jitter'].mean()
us_avg_jitter = df_us['Jitter'].mean()
eu_max_jitter = df_eu['Jitter'].max()
us_max_jitter = df_us['Jitter'].max()

# Set the bar width and the positions of the bars on the x-axis
bar_width = 0.2
r = [0]

# Create subplots with three touching bars for each type of jitter
fig, axs = plt.subplots(nrows=1, ncols=3, figsize=(15, 6))
plt.rcParams['font.size'] = 15

# Minimum Jitter subplot
axs[0].bar(r, [eu_min_jitter], color='green', width=bar_width)
axs[0].bar([r[0] + bar_width], [us_min_jitter], color='blue', width=bar_width)
axs[0].set_xticks([r[0], r[0] + bar_width])
axs[0].set_xticklabels(['Közvetett', 'Közvetlen'])
axs[0].set_xlabel('Elérési mód')
axs[0].set_ylabel('Minimum jitter (ms)')
axs[0].set_title('Minimum jitter')

# Average Jitter subplot
axs[1].bar(r, [eu_avg_jitter], color='green', width=bar_width)
axs[1].bar([r[0] + bar_width], [us_avg_jitter], color='blue', width=bar_width)
axs[1].set_xticks([r[0], r[0] + bar_width])
axs[1].set_xticklabels(['Közvetett', 'Közvetlen'])
axs[1].set_xlabel('Elérési mód')
axs[1].set_ylabel('Átlagos jitter (ms)')
axs[1].set_title('Átlagos jitter')

# Maximum Jitter subplot
axs[2].bar(r, [eu_max_jitter], color='green', width=bar_width)
axs[2].bar([r[0] + bar_width], [us_max_jitter], color='blue', width=bar_width)
axs[2].set_xticks([r[0], r[0] + bar_width])
axs[2].set_xticklabels(['Közvetett', 'Közvetlen'])
axs[2].set_xlabel('Elérési mód')
axs[2].set_ylabel('Maximum jitter (ms)')
axs[2].set_title('Maximum jitter')

# Adjust the spacing between subplots
plt.subplots_adjust(wspace=0.4)

plt.savefig('jitter-comparison.png', dpi=300)
plt.show()
