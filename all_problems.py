#import this

a = 920
b = 992
result = a**2 + b**2
print(result)


string = "Ji0Pn85EphibolusvhBekCvbL9WRaPx1mxgnlJ4CcLEiqEVMRtKn1ahWD7fASscsaqrBUXm9FcffGh43BePySGZexTvokRmc0fxGiIvmxb4wP7OtpvXRt7ybiad0rF98FjBEpwLaAVgQ2qgu2X2Rn8VCZrXVcXarmatakVD."
a = 7
b = 15
c = 158
d = 163

print(f'{string[a:b + 1]} {string[c:d + 1]}')

x = 4256
y = 9088
result = 0
for i in range(x,y + 1):
    if i % 2 != 0:
        result += i
print(result)

#Working with files....
outputFile = []

#with open('village/asdf.txt', 'r') as f:
#    outputFile = [line for pos, line in enumerate(
#        f.readlines()) if pos % 2 != 0]

#with open('village/out.txt', 'w') as f:
#    f.write(''.join(line for line in outputFile))





