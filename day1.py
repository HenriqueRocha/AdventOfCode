import sys

times_depth_increased = 0
previous_measurement = int(sys.stdin.readline())

for line in sys.stdin:
    measurement = int(line)
    if measurement > previous_measurement:
        times_depth_increased += 1
    previous_measurement = measurement

print(times_depth_increased)
