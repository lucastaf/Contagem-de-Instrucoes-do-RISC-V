from ast import List
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
    
    def reordenateInstructions(self):
        for index, instruction in enumerate(self.instructions):
            if instruction.fullInstructions == nopInstruction.fullInstructions:
                usedRegisters : list[str]  = []
                if (self.instructions[index - 1].rd not in [None, '00000']):
                    usedRegisters.append(self.instructions[index -1].rd)
                if(index >= 2 and self.instructions[index - 2].rd not in [None, '00000']):
                    usedRegisters.append(self.instructions[index -2].rd)
                    
                newInstructionIndex = index + 1
                while(newInstructionIndex < len(self.instructions) and self.instructions[newInstructionIndex].type != 'B'):
                    currentInstruction = self.instructions[newInstructionIndex]
                    if (currentInstruction.fullInstructions != nopInstruction.fullInstructions and 
                        str(currentInstruction.rs1) not in usedRegisters and str(currentInstruction.rs2) not in usedRegisters):
                        
                        self.instructions[index] = currentInstruction
                        self.instructions.pop(newInstructionIndex)
                        break
                    elif currentInstruction.rd not in [None, '00000']:
                        usedRegisters.append(currentInstruction.rd)  
                    newInstructionIndex += 1
                    
        
    
    def nopInsertion(self, newInstruction : riscVInstruction):
        lastInstructions = self.instructions[-2::]
        for index, instruction in enumerate(lastInstructions):
            if ((instruction.rd == newInstruction.rs1 or instruction.rd == newInstruction.rs2) and instruction.rd != None):
                if (not(self.haveForward)):
                    for _ in range(index + 1):
                        self.instructions.append(riscVInstruction(str(10011).rjust(32,"0")))
                elif instruction.opcode == "0000011" and index == 1:
                    self.instructions.append(nopInstruction)
    
    def getFullProgram(self):
        fullProgram = ""
        for instruction in self.instructions:
            fullProgram += instruction.getHexInstruction() + "\n"
        return fullProgram
    
            