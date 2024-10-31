from functions.instructionsTypes import instructionsTypes
from functions.common import binStrToInt
from typing import Literal


class riscVInstruction:
    def __init__(self, binario, movedInstruction = False):
        self.movedInstruction = movedInstruction
        self.fullInstructions = binario
        self.opcode = binario[31-6::]
        self.type : Literal["U", "J", "B", "I", "S", "R"] = instructionsTypes.get(self.opcode)
        rd = binario[31-11:31-6]
        funct3 = binario[31-14: 31-11]
        rs1 = binario[31-19:31-14]
        rs2 = binario[31-24:31-19]
        funct7 = binario[31-31:31-24]
        
        haveRD = ("R","I","U","J")
        haveFunct3 = ("R","I","S","B")
        haveRS1= ("R","I","S","B")
        haveRS2=("R","S","B")
        self.rd = rd if self.type in haveRD else None
        self.funct3 = funct3 if self.type in haveFunct3 else None
        self.rs1 = rs1 if self.type in haveRS1 else None
        self.rs2 = rs2 if self.type in haveRS2 else None
        self.funct7 = funct7 if self.type == "R" else None 
        imediates = {
            "I" : funct7+rs2 ,
            "S" : funct7+rd,
            "B" : (binario[0]+binario[31-7]+binario[1:32-25]+binario[31-11:31-7]+ "0"),
            "U" : funct7 + rs2 + rs1 + funct3 + "000000000000",
            "J" : binario[0] + binario[31-19:31-11] + binario[11] + binario[1:11]    
        }
        self.imediate = imediates.get(self.type, "")
        
    def getAllInfo(self):
        return [self.type, binStrToInt(self.opcode), binStrToInt(self.rd), binStrToInt(self.funct3), 
            binStrToInt(self.rs1), binStrToInt(self.rs2), 
            binStrToInt(self.imediate), binStrToInt(self.funct7)]
        
    def getHexInstruction(self):
        return hex(int(self.fullInstructions, 2))

nopInstruction = riscVInstruction(str(10011).rjust(32,"0"))
def newNopInstruction():
    return riscVInstruction(str(10011).rjust(32,"0"))