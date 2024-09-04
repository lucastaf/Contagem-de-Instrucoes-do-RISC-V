import csv
from riscVInstruction import riscVInstruction
file = open("ROM", 'r')
csvFile = open("result.csv", 'w', newline='')
csvFile.write("sep = , \n")
writer = csv.writer(csvFile)

writer.writerow(["TIPO", "OPCODE", "RD", "FUNCT3", "RS1", "RS2", "IMD", "FUNCT7"])

aluInstructions = ["0010011","0110011", "0011011", "0111011"] #addi, add, addiw, addw, addi
jumpInstructions = ["1101111", "1100111"] #jal, jalr
branchInstructions = ["1100011"] #beq
memoryInstructions = ["0000011", "0100011"] #lw ,sw
instructionStatistics = {
    "ALU" : 0,
    "JUMP" : 0,
    "BRANCH" : 0,
    "MEMORY" : 0,
    "OTHER" : 0,
}
#exit()
for line in file:
    binario = str(bin(int(line, 16)).zfill(8))
    binario = binario[3:]
    binario = binario.rjust(32,"0")
    instruction = riscVInstruction(binario)
    print(instruction.getInstructionDetails())
    if instruction.opcode in aluInstructions:
        instructionStatistics["ALU"] += 1
    elif instruction.opcode in branchInstructions:
        instructionStatistics["BRANCH"] += 1
    elif instruction.opcode in jumpInstructions:
        instructionStatistics["JUMP"] += 1
    elif instruction.opcode in memoryInstructions:
        instructionStatistics["MEMORY"] += 1
    else:
        instructionStatistics["OTHER"] += 1
    writer.writerow(instruction.getAllInfo())
    
staticsFile = open("statics.txt", 'w')
totalInstructions = instructionStatistics["ALU"] + instructionStatistics["BRANCH"] + instructionStatistics["JUMP"] + instructionStatistics["MEMORY"] + instructionStatistics["OTHER"] 
staticsFile.write("TOTAL DE INSTRUÇÕES: " + str(totalInstructions) + ", ALU: " + str(instructionStatistics["ALU"]) + ", BRANCH: " + str(instructionStatistics["BRANCH"]) + ", JUMP: " + str(instructionStatistics["JUMP"]) + ", MEMORY: " + str(instructionStatistics["MEMORY"]) + ", OTHER: " + str(instructionStatistics["OTHER"]))