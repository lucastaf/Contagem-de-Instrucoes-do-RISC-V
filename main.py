import csv
from classes.riscVInstruction import riscVInstruction
file = open("ROM", 'r')
csvFile = open("result.csv", 'w', newline='')
csvFile.write("sep = , \n")
writer = csv.writer(csvFile)

writer.writerow(["TIPO", "OPCODE", "RD", "FUNCT3", "RS1", "RS2", "IMD", "FUNCT7"])
latestInstructions = []

#exit()
for line in file:
    binario = str(bin(int(line, 16)).zfill(8))
    binario = binario[2:]
    binario = binario.rjust(32,"0")
    instruction = riscVInstruction(binario)
    latestInstructions.insert(0,instruction.opcode)
    latestInstructions = latestInstructions[0:5]
    print(latestInstructions)
    