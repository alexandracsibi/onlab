import subprocess
import argparse
import re

def iperf_out(output_file):
    start_bw = 18
    step = 1
    num_iterations = 8

    for i in range(1, num_iterations + 1):
        bw = start_bw + i * step
        cmd = ["iperf", "-c", "localhost", "-p", "5000", "-u", "-l", "1250", "-b", f"{bw}m", "-t", "40"]
        with open(output_file, "a") as output_f:
            subprocess.call(cmd, stdout=output_f, stderr=subprocess.DEVNULL)

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

def clear_output_file(output_file):
    with open(output_file, "w") as file:
        file.write("")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--region", type=int, help="Specify the region (1 for EU, 2 for US)")
    args = parser.parse_args()
    iperf_output_file = "output.txt"

    if args.region == 1:
        server_report_file = "server_report_eu.csv"
    elif args.region == 2:
        server_report_file = "server_report_us.csv"
    else:
        print("Invalid region specified.")
        exit(1)

    iperf_out(iperf_output_file)
    write_result(iperf_output_file, server_report_file)
    clear_output_file(iperf_output_file)
