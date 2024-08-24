
file = open("ROM", 'r')


line = file.readline()
binario = str(bin(int(line, 16)).zfill(8))
binario = binario[3:]
binario = binario.rjust(32,"0")
#binario = "A123456789DC1234567B0101F001001F"
print(binario)
opcode = binario[31-6::]
rd = binario[31-11:31-6]
funct3 = binario[31-14: 31-11]
rs1 = binario[31-19:31-14]
rs2 = binario[31-24:31-19]
funct7 = binario[31-31:31-24]
ITypeImd = funct7+rs2
StypeImd = funct7+rd
BTypeImd = (binario[0]+binario[31-7]+binario[1:32-25]+binario[31-11:31-7]+ "0")
UTypeImd = funct7 + rs2 + rs1 + funct3 + "00000000000"
JTypeImd = binario[0] + binario[31-19:31-11] + binario[11] + binario[1:11]

print(JTypeImd)
