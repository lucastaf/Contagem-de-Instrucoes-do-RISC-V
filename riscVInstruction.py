class riscVInstruction:
    def __init__(self, binario):
        self.fullInstructions = binario
        self.opcode = binario[31-6::]
        self.type = self.getInstructionType()
        rd = binario[31-11:31-6]
        funct3 = binario[31-14: 31-11]
        rs1 = binario[31-19:31-14]
        rs2 = binario[31-24:31-19]
        funct7 = binario[31-31:31-24]
        
        haveRD = ["R","I","U","J"]
        haveFunct3 = ["R","I","S","B"]
        haveRS1= ["R","I","S","B"]
        haveRS2=["R","S","B"]
        self.rd = rd if self.type in haveRD else ""
        self.funct3 = funct3 if self.type in haveFunct3 else ""
        self.rs1 = rs1 if self.type in haveRS1 else ""
        self.rs2 = rs2 if self.type in haveRS2 else ""
        self.funct7 = funct7 if self.type == "R" else "" 
        
        imediates = {
            "I" : funct7+rs2 ,
            "S" : funct7+rd,
            "B" : (binario[0]+binario[31-7]+binario[1:32-25]+binario[31-11:31-7]+ "0"),
            "U" : funct7 + rs2 + rs1 + funct3 + "000000000000",
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
        defaultValues = objectToString({
                "type" : self.type,
                "opcode" : self.opcode,
        })
        details = {
            "R": objectToString({
                "rd" : self.rd,
                "funct3" : self.funct3,
                "rs1": self.rs1,
                "rs2" : self.rs2,
                "funct7" : self.funct7
            }),
            "I": objectToString({
                "rd" : self.rd,
                "funct3" : self.funct3,
                "rs1": self.rs1,
                "imd" : self.imediate
            }),
            "S": objectToString({
                "funct3" : self.funct3,
                "rs1": self.rs1,
                "rs2" : self.rs2,
                "imd" : self.imediate
            }),
            "B": objectToString({
                "funct3" : self.funct3,
                "rs1": self.rs1,
                "rs2" : self.rs2,
                "imd" : self.imediate
            }),
            "U": objectToString({
                "rd" : self.rd,
                "imd" : self.imediate
            }),
            "J": objectToString({
                "rd" : self.rd,
                "imd" : self.imediate
            })
        }
        
        return defaultValues +  ", " + details.get(self.type)
    
    def getAllInfo(self):
        return [self.type, binStrToInt(self.opcode), binStrToInt(self.rd), binStrToInt(self.funct3), 
            binStrToInt(self.rs1), binStrToInt(self.rs2), 
            binStrToInt(self.imediate), binStrToInt(self.funct7)]

    
def binStrToInt(str):
    return int(str,2) if str.isdigit() else ""

def objectToString(object): 
    returnValue = ""
    for key, value in object.items():
        returnValue += key + ": " + value + ","
    returnValue = returnValue[:-1]
    return returnValue