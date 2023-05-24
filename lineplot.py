import pandas as pd
import matplotlib.pyplot as plt

def generate_line_plot(df, title, y_label, save_file):
    df_sorted = df.sort_values('Bandwidth')
    plt.plot(df_sorted['Bandwidth'], df[y_label], marker='o', linestyle='-', linewidth=2,
markersize=4, markerfacecolor='red')
    plt.xlabel('Bandwidth')
    plt.ylabel(y_label)
    plt.title(title)
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(save_file, dpi=300)
    plt.close()

# Read US data from server_report_us.csv
df_us = pd.read_csv('server_report_us.csv', delimiter=',')

# Read EU data from server_report_eu.csv
df_eu = pd.read_csv('server_report_eu.csv', delimiter=',')

plt.figure(figsize=(10, 6))
plt.rcParams['font.size'] = 12

# Generate line plot for average latency (US)
generate_line_plot(df_us, 'Bandwidth vs Average Latency (US)', 'Latency avg', 'lineplot_avg_latency_us.png')

# Generate line plot for maximum latency (US)
generate_line_plot(df_us, 'Bandwidth vs Maximum Latency (US)', 'Latency max', 'lineplot_max_latency_us.png')

# Generate line plot for average latency (EU)
generate_line_plot(df_eu, 'Bandwidth vs Average Latency (EU)', 'Latency avg', 'lineplot_avg_latency_eu.png')

# Generate line plot for maximum latency (EU)
generate_line_plot(df_eu, 'Bandwidth vs Maximum Latency (EU)', 'Latency max', 'lineplot_max_latency_eu.png')
