from ast import List, Raise, Set
from dis import Instruction
from classes.riscVInstruction import riscVInstruction, nopInstruction, newNopInstruction
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
            self.instructions.append(newNopInstruction())
            self.instructions.append(newNopInstruction())
    
    def reordenateInstructions(self):
        for index, instruction in enumerate(self.instructions):
            #se o index for igual ao começo da array, nao tem como substruir possiveis nops
            if index == 0: continue
                
            if instruction.fullInstructions == nopInstruction.fullInstructions and not(instruction.movedInstruction):
                self.reordenateNop(index, isDelayedBranch=False)
                pass
            if instruction.type in ["B", "J"]:
                newInstructionIndex = index + 1
                while newInstructionIndex < len(self.instructions) and self.instructions[newInstructionIndex].fullInstructions == nopInstruction.fullInstructions:
                    isNopMoved = self.reordenateNop(newInstructionIndex, isDelayedBranch=True)
                    if not(isNopMoved): newInstructionIndex += 1

    def reordenateNop(self, index : int, isDelayedBranch = False):
        #se o index for igual ao ultimo item, nao precisa remover a NOP se tiver
        if index == len(self.instructions) - 1: return False
        instruction = self.instructions[index]
        if instruction.fullInstructions != nopInstruction.fullInstructions:
            raise Exception("Instruction is not a nop")
        
        usedRegisters = set()
        #Cria um set com todos os registorios usados diferentes de none e zero
        for register in [
            self.instructions[index + 1].rs1, self.instructions[index + 1].rs2,
        ]:
            if register not in [None, '00000']:
                usedRegisters.add(register)
                
        currentInstructionIndex = index - 1
        currentInstruction = self.instructions[currentInstructionIndex]                        
        #se a reordenação for de um delayedBranch, a busca por instruçõo começa uma instrução assima do primeiro branch
        if isDelayedBranch:
            while (currentInstruction.type not in ["B", "J"]):
                currentInstructionIndex = currentInstructionIndex - 1
                currentInstruction = self.instructions[currentInstructionIndex]
                
            #adiciona os registorios usados no branch para a lista de usedRegisters
            for register in [currentInstruction.rs1, currentInstruction.rs2]:
                if register not in [None, '00000']:
                    usedRegisters.add(register)
            #subtrai novamente o index para começar a contagem uma instrução antes
            currentInstructionIndex = currentInstructionIndex - 1
            currentInstruction = self.instructions[currentInstructionIndex]
                
        while(currentInstructionIndex >= 0 and currentInstruction.type not in ['B', "J"] and
            not(currentInstruction.movedInstruction)):
            #se a instrução não foi usada, substui com a NOP
            if (str(currentInstruction.rd) not in usedRegisters):
                self.instructions[index] = currentInstruction
                currentInstruction.movedInstruction = True
                self.instructions.pop(currentInstructionIndex)
                return True
            else:
                #senao, inclua seus regisers para a lista de registorios usados
                if currentInstruction.rs1 not in [None, '00000']:
                    usedRegisters.add(currentInstruction.rs1)  
                if currentInstruction.rs2 not in [None, '00000']:
                    usedRegisters.add(currentInstruction.rs2)  
            currentInstructionIndex -= 1
            currentInstruction = self.instructions[currentInstructionIndex]
        #Fim do While ----
        self.instructions[index].movedInstruction = True
        return False
    
    def nopInsertion(self, newInstruction : riscVInstruction):
        lastInstructions = self.instructions[-2::]
        for index, instruction in enumerate(lastInstructions):
            if ((instruction.rd == newInstruction.rs1 or instruction.rd == newInstruction.rs2) and instruction.rd != None):
                if (not(self.haveForward)):
                    for _ in range(index + 1):
                        self.instructions.append(newNopInstruction())
                elif instruction.opcode == "0000011" and index == 1:
                    self.instructions.append(newNopInstruction())
    
    def getFullProgram(self):
        fullProgram = ""
        for instruction in self.instructions:
            fullProgram += instruction.getHexInstruction() + "\n"
        return fullProgram
    
            