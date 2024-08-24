from riscVInstruction import riscVInstruction
file = open("ROM", 'r')

#exit()
for line in file:
    binario = str(bin(int(line, 16)).zfill(8))
    binario = binario[3:]
    binario = binario.rjust(32,"0")
    binaryObject = riscVInstruction(binario)
    print(binaryObject.getInstructionDetails())