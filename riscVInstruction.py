class riscVInstruction:
    def __init__(self, binario):
        self.opcode = binario[31-6::]
        self.rd = binario[31-11:31-6]
        self.funct3 = binario[31-14: 31-11]
        self.rs1 = binario[31-19:31-14]
        self.rs2 = binario[31-24:31-19]
        self.funct7 = binario[31-31:31-24]
        self.ITypeImd = self.funct7+self.rs2
        self.StypeImd = self.funct7+self.rd
        self.BTypeImd = (binario[0]+binario[31-7]+binario[1:32-25]+binario[31-11:31-7]+ "0")
        self.UTypeImd = self.funct7 + self.rs2 + self.rs1 + self.funct3 + "00000000000"
        self.JTypeImd = binario[0] + binario[31-19:31-11] + binario[11] + binario[1:11]
    
    def get_instruction_type(self):
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