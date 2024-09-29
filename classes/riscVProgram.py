from classes.riscVInstruction import riscVInstruction
from functions.common import haveSharedItems

class riscVProgram:
    def __init__(self):
        self.instructions : list[riscVInstruction] = []
        self.lastInstructions : list[riscVInstruction] = []
        self.usedRegisters = []
    
    def addInstruction(self, newInstruction : riscVInstruction):
        self.lastInstructions = self.instructions[-2::]
        for index, instruction in enumerate(self.lastInstructions):
            if instruction.rd == newInstruction.rs1 or instruction.rd == newInstruction.rs2:
                for _ in range(2 - index):
                    self.instructions.append(riscVInstruction(str(10011).rjust(32,"0")))
        self.instructions.append(newInstruction)
        
    def getFullProgram(self):
        fullProgram = ""
        for instruction in self.instructions:
            fullProgram += instruction.fullInstructions + "\n"
        return fullProgram
    
    
            
            