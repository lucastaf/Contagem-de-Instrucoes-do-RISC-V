from ast import List, Set
from classes.riscVInstruction import riscVInstruction, nopInstruction
from functions.common import haveSharedItems

class riscVProgram:
    def __init__(self, haveForward : bool):
        self.haveForward : bool = haveForward
        self.instructions : list[riscVInstruction] = []
    
    def addInstruction(self, newInstruction : riscVInstruction):
        #M2A:
        self.nopInsertion(newInstruction)
        self.instructions.append(newInstruction)
        if self.haveForward and newInstruction.type in ["B" , "J"] :
            self.instructions.append(nopInstruction)
            self.instructions.append(nopInstruction)
    
    def reordenateInstructions(self):
        for index, instruction in enumerate(self.instructions):
            if index >= len(self.instructions) - 1:
                break
            if instruction.fullInstructions == nopInstruction.fullInstructions:
                usedRegisters = set()
                for register in [
                    self.instructions[index + 1].rs1, self.instructions[index + 1].rs2,
                ]:
                    if register != None:
                        usedRegisters.add(register)
                newInstructionIndex = index - 1
                while(newInstructionIndex >= 0 and self.instructions[newInstructionIndex].type not in ['B', "J"] and
                    self.instructions[newInstructionIndex].fullInstructions != nopInstruction.fullInstructions):
                    currentInstruction = self.instructions[newInstructionIndex]
                    if (str(currentInstruction.rd) not in usedRegisters):
                        self.instructions[index] = currentInstruction
                        currentInstruction.movedInstruction = True
                        self.instructions.pop(newInstructionIndex)
                        break
                    else:
                        if currentInstruction.rs1 not in [None, '00000']:
                            usedRegisters.add(currentInstruction.rs1)  
                        if currentInstruction.rs2 not in [None, '00000']:
                            usedRegisters.add(currentInstruction.rs2)  
                    newInstructionIndex -= 1
                    
    def delayBranches(self):
        for index, instruction in enumerate(self.instructions):
            if(instruction.type in ["B","J"] and index < len(self.instructions) - 2):
                usedRegisters = set()
                if instruction.type == "B":
                    usedRegisters.add(instruction.rs1)
                    usedRegisters.add(instruction.rs2)
                currentIndex = index - 1
                currentInstruction = self.instructions[currentIndex]
                while (currentIndex >= 0 and not(currentInstruction.movedInstruction) ):
                    pass
    
    def nopInsertion(self, newInstruction : riscVInstruction):
        lastInstructions = self.instructions[-2::]
        for index, instruction in enumerate(lastInstructions):
            if ((instruction.rd == newInstruction.rs1 or instruction.rd == newInstruction.rs2) and instruction.rd != None):
                if (not(self.haveForward)):
                    for _ in range(index + 1):
                        self.instructions.append(nopInstruction)
                elif instruction.opcode == "0000011" and index == 1:
                    self.instructions.append(nopInstruction)
    
    def getFullProgram(self):
        fullProgram = ""
        for instruction in self.instructions:
            fullProgram += instruction.getHexInstruction() + "\n"
        return fullProgram
    
            