from riscVInstruction import riscVInstruction
file = open("ROM", 'r')


        
line = file.readline()
binario = str(bin(int(line, 16)).zfill(8))
binario = binario[3:]
binario = binario.rjust(32,"0")
binaryObject = riscVInstruction(binario)
print(binaryObject.get_instruction_type())

#RTYPE  - 011
#ITYPE - 001
#STYPE - 010  
#BTYPE - 110
#UTYPE - 100
#JTYPE - 111

#010, 100