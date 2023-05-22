import subprocess
import argparse
import re

def iperf_out():
    start_bw = 10
    step = 10
    num_iterations = 8

    for i in range(1, num_iterations + 1):
        bw = start_bw + i * step
        cmd = ["iperf", "-c", "localhost", "-p", "5000", "-u", "-l", "1000", "-b", f"{bw}m", "-t", "60"]
        with open("output.txt", "a") as output_file:
            subprocess.call(cmd, stdout=output_file, stderr=subprocess.DEVNULL)

def write_result(input_file, output_file):

    with open(input_file, "r") as in_f, open(output_file, "a") as out_f:
        lines = in_f.readlines()
        for i in range(len(lines)):
            if "Server Report" in lines[i]:
                parts = lines[i+2].split()

                int_st, int_end = parts[2].split("-")
                lost, total = parts[10].split("/")
                l_avg, l_min, l_max, l_stdev = parts[12].split("/")
                percentage = parts[11][1:-2]
                values = [int_end, parts[4], parts[6], parts[8], lost, total, percentage, l_avg, l_min, l_max, l_stdev, parts[14]]
                output_line = ','.join(values) + '\n'
                out_f.write(output_line)
if __name__ == "__main__":
    iperf_out()
    write_result("output.txt", "server_report.csv")
