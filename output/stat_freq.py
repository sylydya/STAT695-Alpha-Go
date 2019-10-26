

counter = {}

for l in open('first_steps_statistics_000'):
    l = l.strip()
    if l not in counter:
        counter[l] = 0
    counter[l] += 1

for l in open('first_steps_statistics_090'):
    l = l.strip()
    if l not in counter:
        counter[l] = 0
    counter[l] += 1

for l in open('first_steps_statistics_180'):
    l = l.strip()
    if l not in counter:
        counter[l] = 0
    counter[l] += 1

for l in open('first_steps_statistics_270'):
    l = l.strip()
    if l not in counter:
        counter[l] = 0
    counter[l] += 1

high_freq = {key:val for key, val in counter.items() if val > 500}

for val in high_freq:
    print(val, high_freq[val])
