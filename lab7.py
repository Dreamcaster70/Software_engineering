lines = ['line1', 'line2', 'line3']
with open('laba.txt', 'w') as f:
    for line in lines:
        f.write('\nCycle run ' + line)
    print('Done!')