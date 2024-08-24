class riscVInstruction:
    def __init__(self, binario):
        self.opcode = binario[31-6::]
        self.type = self.getInstructionType()
        
        haveRD = ["R","I","U","J"]
        haveFunct3 = ["R","I","S","B"]
        haveRS1= ["R","I","S","B"]
        haveRS2=["R","S","B"]
        self.rd = binario[31-11:31-6] if type in haveRD else ""
        self.funct3 = binario[31-14: 31-11] if type in haveFunct3 else ""
        self.rs1 = binario[31-19:31-14] if type in haveRS1 else ""
        self.rs2 = binario[31-24:31-19] if type in haveRS2 else ""
        self.funct7 = binario[31-31:31-24] if type == "R" else "" 
        
        imediates = {
            "I" : self.funct7+self.rs2,
            "S" : self.funct7+self.rd,
            "B" : (binario[0]+binario[31-7]+binario[1:32-25]+binario[31-11:31-7]+ "0"),
            "U" : self.funct7 + self.rs2 + self.rs1 + self.funct3 + "000000000000",
            "J" : binario[0] + binario[31-19:31-11] + binario[11] + binario[1:11]    
        }
        self.imediate = imediates.get(self.type, "")
        
        
    
    def getInstructionType(self) -> str:
        opcode = int(self.opcode,2)
        instruction_types = {
            "R": range(0x00, 0x20),
            "I": range(0x20, 0x40),
            "S": range(0x40, 0x60),
            "B": range(0x60, 0x80),
            "U": range(0x80, 0xA0),
            "J": range(0xA0, 0xC0)
        }
        for instruction_type, opcode_range in instruction_types.items():
            if opcode in opcode_range:
                return instruction_type
            
    def getInstructionDetails(self) -> str:
        details = {
            "R": objectToString({
                "type" : self.type,
                "opcode" : self.opcode,
                "rd" : self.rd,
                "funct3" : self.funct3,
                "rs1": self.rs1,
                "rs2" : self.rs2,
                "funct7" : self.funct7
            }),
            "I": objectToString({
                "type" : self.type,
                "opcode" : self.opcode,
                "rd" : self.rd,
                "funct3" : self.funct3,
                "rs1": self.rs1,
                "imd" : self.imediate
            }),
            "S": objectToString({
                "type" : self.type,
                "opcode" : self.opcode,
                "funct3" : self.funct3,
                "rs1": self.rs1,
                "rs2" : self.rs2,
                "imd" : self.imediate
            }),
            "B": objectToString({
                "type" : self.type,
                "opcode" : self.opcode,
                "funct3" : self.funct3,
                "rs1": self.rs1,
                "rs2" : self.rs2,
                "imd" : self.imediate
            }),
            "U": objectToString({
                "type" : self.type,
                "opcode" : self.opcode,
                "rd" : self.rd,
                "imd" : self.imediate
            }),
            "J": objectToString({
                "type" : self.type,
                "opcode" : self.opcode,
                "rd" : self.rd,
                "imd" : self.imediate
            })
        }
        
        return details.get(self.type)
    
def objectToString(object): 
    returnValue = ""
    for key, value in object.items():
        returnValue += key + ": " + value + ","
    returnValue = returnValue[:-1]
    return returnValue