#Jake Paccione & Matthew Mohamed
#I pledge my honor that I have abided by the Stevens Honor System.

import os

#Ensure the working directory is in the same folder as 'translator.py'
dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(dir)

#Translate instructions into binary
opcodes = {"ADD": 0b00, "SUB": 0b01, "LDR": 0b10, "STR": 0b11}
registers = {"X0": 0b00, "X1": 0b01, "X2": 0b10, "X3": 0b11}

#Analyzes input and translates into machine code and then hex
#EX: ADD X0, X1, X2 -> [ADD, X0, X1, X2] -> [00,00,01,10] -> 0b0000111100000110 -> 0x0f06
#EX: ADD X0, X1, 5 -> [ADD, X0, X1, 5] -> [00, 00, 01, 0000000101] -> 0b0000000001010101 -> 0x0055

def assemble(line):
    '''Translates a line of assembly into binary.'''
    code = line.replace(",", "").split()
    opcode = code[0]
    dstreg = registers[code[1]]

    if opcode == "ADD" or opcode == "SUB":
        try:
            imm = int(code[3])
            if imm < 0 or imm > 511:
                raise ValueError("Integer input must be non-negative no greater than 511.")
            reg1 = registers[code[2]]
            binary = (opcodes[opcode] << 14) | (imm << 4) | (reg1 << 2) | dstreg
        except ValueError:
            reg1 = registers[code[2]]
            reg2 = registers[code[3]]
            binary = (opcodes[opcode] << 14) | (reg2 << 12) | (0b11110000 << 4) | (reg1 << 2) | dstreg

    elif opcode == "LDR" or opcode == "STR":
            try:
                imm = int(code[3][:-1])
            except ValueError:
                print("Immediate offset must be an integer value.")
            if imm < 0 or imm > 1023:
                raise ValueError("Immediate offset must be non-negative no greater than 1023.")
            reg1 = registers[code[2][1:]]
            binary = (opcodes[opcode] << 14) | (imm << 4) | (reg1 << 2) | dstreg
            print(binary)
    else:
        raise ValueError(f"Unknown opcode: {opcode}")
    
    return binary

def create_image(assembly, output):
    '''Writes into output.txt file with properly formatted hex data from the assembly instructions.'''
    with open(output, "w") as file:
        file.write("v3.0 hex words addressed\n")

        pc = 0
        line = []

        for lines in assembly:
            machine_code = assemble(lines)
            hex_code = f"{machine_code:04x}"
            line.append(hex_code)

            if (len(line) == 4):
                    file.write(f"{pc:02x}: {' '.join(line)}\n")
                    line = []
                    pc += 4
        if line != []:
            file.write(f"{pc:02x}: {' '.join(line)}\n")

assembly_code = []

print("Welcome to PacMo! This CPU Project was created by Matthew Mohamed & Jake Paccione. \n")
try:
    with open("assembly.s", "r") as file:
        for line in file:
            if line.split():  
                assembly_code.append(line)
        # Generate the output file
    create_image(assembly_code, "output.txt")
    print("An image file named 'output.txt' has been created in the same directory as your program.")
except FileNotFoundError:
    print("File not found. Make sure your ARM64 assembly code is named ")
    print("'assembly.s' and is in the same directory as your program. \n")





