
file = open("ROM", 'r')


line = file.readline()
binario = str(bin(int(line, 16)).zfill(8))
binario = binario[3:]
binario = binario.rjust(32,"0")
print(binario)
