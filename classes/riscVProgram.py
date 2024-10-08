from classes.riscVInstruction import riscVInstruction
from functions.common import haveSharedItems

class riscVProgram:
    def __init__(self, haveForward : bool):
        self.haveForward : bool = haveForward
        self.instructions : list[riscVInstruction] = []
    
    def addInstruction(self, newInstruction : riscVInstruction):
        lastInstructions = self.instructions[-2::]
        for index, instruction in enumerate(lastInstructions):
            if ((instruction.rd == newInstruction.rs1 or instruction.rd == newInstruction.rs2) and instruction.rd != None):
                if (not(self.haveForward)):
                    for _ in range(index + 1):
                        self.instructions.append(riscVInstruction(str(10011).rjust(32,"0")))
                elif instruction.opcode == "0000011" and index == 1:
                    self.instructions.append(riscVInstruction(str(10011).rjust(32,"0")))
                    
        self.instructions.append(newInstruction)
        
    def getFullProgram(self):
        fullProgram = ""
        for instruction in self.instructions:
            fullProgram += instruction.getHexInstruction() + "\n"
        return fullProgram
    
    
            
            