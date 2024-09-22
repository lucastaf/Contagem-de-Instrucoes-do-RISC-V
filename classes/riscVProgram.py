from classes.riscVInstruction import riscVInstruction
from functions.common import haveSharedItems

class riscVProgram:
    def __init__(self):
        self.intructions : list[riscVInstruction] = []
        self.lastInstructions : list[riscVInstruction] = []
        self.usedRegisters = []
    
    def addInstruction(self, newInstruction : riscVInstruction):
        self.intructions.append(newInstruction)
        self.lastInstructions = self.intructions[-5::]
        for index, instruction in enumerate(self.lastInstructions):
            if haveSharedItems(newInstruction.getUsedRegisters(), instruction.getUsedRegisters()):
                print(index)
                pass
    
            
            