f = open("vs_chart.csv", 'r')
while True:
    line = f.readline()
    if not line: break
    print(line)
f.close()