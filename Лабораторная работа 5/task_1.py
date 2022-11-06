from pprint import pprint

spis = []
for i in range(16):
    dic = {'dec':i, 'bin':bin(i), 'oct':oct(i), 'hex':hex(i)}
    spis.append(dic)

pprint(spis)



