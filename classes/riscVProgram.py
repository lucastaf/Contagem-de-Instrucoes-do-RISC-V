from classes.riscVInstruction import riscVInstruction

class riscVProgram:
    def __init__(self) -> None:
        self.intructions : list[riscVInstruction] = []
        self.lastInstructions : list[riscVInstruction] = []
        self.usedRegisters = []
    
    def addInstruction(self, intruction : riscVInstruction):
        self.intructions.append(intruction)
        self.lastInstructions = self.intructions[-5::]
        
        
        
    def getUsedRegisters(self):
        self.usedRegisters = []
        for instruction in self.lastInstructions:
            if instruction.rd not in self.usedRegisters:
                self.usedRegisters.append(instruction.rd)
            if instruction.rs1 not in self.usedRegisters:
                self.usedRegisters.append(instruction.rs1)
            if instruction.rs2 not in self.usedRegisters:
                self.usedRegisters.append(instruction.rs2)
            
            