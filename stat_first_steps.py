# coding: utf-8
import sys, re, os



# /home/deng106/work/alpha_go/data/b20c256-s99990784-d35173134/sgfs


# only consider 贴木 ranges in [6.5, 7, 7.5]
KM = set(['6.5', '7', '7.5'])

# study the first several steps 
steps = 10

# rotation table
r = {'a': 'i', 'b': 'h', 'c': 'g', 'd': 'f', 'e': 'e', 'f': 'd', 'g': 'c', 'h': 'b', 'i': 'a', '0': '0'}

fout_000 = open('./output/first_steps_statistics_000', 'w+')
fout_090 = open('./output/first_steps_statistics_090', 'w+')
fout_180 = open('./output/first_steps_statistics_180', 'w+')
fout_270 = open('./output/first_steps_statistics_270', 'w+')


for ith, folder in enumerate(os.listdir('./data')):
    print(ith, folder)
    for filename in os.listdir('./data/' + folder + '/sgfs/'):
        for i, l in enumerate(open('./data/' + folder + '/sgfs/' + filename)):
            syntax = 'B\[([a-i]*)\].*?W\[([a-i]*)\].*?' * steps
            m = re.search(r'.*KM\[(.*?)\].*RE\[(.*?)\].*?' + syntax, l)
            if m:
                km = m.group(1)
                if km not in KM:
                    continue
                result = m.group(2)
                output_000 = 'km_' + km + '_win_' + result[0]
                output_090 = output_000
                output_180 = output_000
                output_270 = output_000
                for _ in range(steps):
                    bb = m.group(3 + _ * 2)
                    ww = m.group(4 + _ * 2)
                    if bb == '':
                        bb = '00'
                    if ww == '':
                        ww = '00'
                    output_000 += '_' + bb[0] + bb[1] + '_' + ww[0] + ww[1]
                    output_090 += '_' + r[bb[0]] + bb[1] + '_' + r[ww[0]] + ww[1]
                    output_180 += '_' + r[bb[0]] + r[bb[1]] + '_' + r[ww[0]] + r[ww[1]]
                    output_270 += '_' + bb[0] + r[bb[1]] + '_' + ww[0] + r[ww[1]]
                fout_000.write(output_000 + '\n')
                fout_090.write(output_090 + '\n')
                fout_180.write(output_180 + '\n')
                fout_270.write(output_270 + '\n')
            else:
                print("Unknown")
