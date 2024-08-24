import csv
from riscVInstruction import riscVInstruction
file = open("ROM", 'r')
csvFile = open("result.csv", 'w', newline='')
csvFile.write("sep = , \n")
writer = csv.writer(csvFile)

writer.writerow(["TIPO", "OPCODE", "RD", "FUNCT3", "RS1", "RS2", "IMD", "FUNCT7"])
#exit()
for line in file:
    binario = str(bin(int(line, 16)).zfill(8))
    binario = binario[3:]
    binario = binario.rjust(32,"0")
    instruction = riscVInstruction(binario)
    print(instruction.getInstructionDetails())
    writer.writerow(instruction.getAllInfo())