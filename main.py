import csv
from classes.riscVProgram import riscVProgram
from classes.riscVInstruction import riscVInstruction
file = open("ROM", 'r')
#csvFile = open("result.csv", 'w', newline='')
#csvFile.write("sep = , \n")
#writer = csv.writer(csvFile)
#writer.writerow(["TIPO", "OPCODE", "RD", "FUNCT3", "RS1", "RS2", "IMD", "FUNCT7"])

program : riscVProgram = riscVProgram(False)

#exit()
for line in file:
    binario = str(bin(int(line, 16)).zfill(8))[2:].rjust(32,"0")
    instruction = riscVInstruction(binario)
    program.addInstruction(instruction)

#program.reordenateInstructions()
#program.delayBranches()
newFile = open("InsertedNops.txt" , "w")
newFile.write(program.getFullProgram())
    