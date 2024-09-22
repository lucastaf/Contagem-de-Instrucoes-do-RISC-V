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

def binStrToInt(str):
    return int(str,2) if str.isdigit() else ""

def objectToString(object): 
    returnValue = ""
    for key, value in object.items():
        returnValue += key + ": " + value + ","
    returnValue = returnValue[:-1]
    return returnValue
