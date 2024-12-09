import os

#Translate instructions into binary
opcodes = {"ADD": 0b00, "SUB": 0b01, "LDR": 0b10, "STR": 0b11}
registers = {"X0": 0b00, "X1": 0b01, "X2": 0b10, "X3": 0b11}

#Analyzes input and translates into machine code and then hex
#EX: ADD X0, X1, X2 -> [ADD, X0, X1, X2] -> [00,00,01,10] -> 0000111100000110 -> 0x0f06
#EX: ADD X0, X1, 5 -> [ADD, X0, X1, 5] -> [00, 00, 01, 0000000101] -> 0000000001010101 -> 0055

def assemble(line):
    '''Translates a line of assembly into binary.'''
    parts = line.replace(",", "").split()
    opcode = parts[0]
    dstreg = registers[parts[1]]

    if opcode == "ADD" or opcode == "SUB":
        try:
            imm = int(parts[3])
            if imm < -512 or imm > 511:
                raise ValueError("Integer value must be at most 10 bits long.")
            reg1 = registers[parts[2]]
            binary = (opcodes[opcode] << 14) | (imm << 4) | (reg1 << 2) | dstreg
        except ValueError:
            reg1 = registers[parts[2]]
            reg2 = registers[parts[3]]
            binary = (opcodes[opcode] << 14) | (reg2 << 12) | (0b11110000 << 4) | (reg1 << 2) | dstreg

    elif opcode == "LDR" or opcode == "STR":
            imm = int(parts[3][:-1])
            if imm < 0 or imm > 1023:
                raise ValueError("Integer value must be at most 10 bits long.")
            reg1 = registers[parts[2][1:]]
            binary = (opcodes[opcode] << 14) | (imm << 4) | (reg1 << 2) | dstreg
    else:
        raise ValueError(f"Unknown opcode: {opcode}")
    
    return binary

def create_image(assembly, output):
    '''Writes into output.txt file with properly formatted hex data from the assembly instructions.'''
    with open(output, "w") as file:
        file.write("v3.0 hex words addressed\n")

        address = 0
        line = []

        for lines in assembly:
            machine_code = assemble(lines)
            hex_code = f"{machine_code:04x}"
            line.append(hex_code)

            if (len(line) == 4):
                    file.write(f"{address:02x}: {' '.join(line)}\n")
                    line = []
                    address += 4
        if line != []:
            file.write(f"{address:02x}: {' '.join(line)}\n")

assembly_code = []

print("Welcome to PacMo! This CPU Project was created by Matthew Mohamed & Jake Paccione. \n")
#Prompts user input to add assembly instruction into a list that translates it into binary and hex data.
while True:
    if (assembly_code != []):
        print("\n")
        print("Current Assembly Code: \n")
        for i in range(0, len(assembly_code)):
            print(assembly_code[i])
        print("\n")
    user_input = input("Entire your line of ARM64 Assembly or type 'done' to quit.\n")
    if user_input == 'done':
        break
    assembly_code.append(user_input)

# Generate the output file
create_image(assembly_code, "output.txt")
print(f"Logisim-compatible text file created: output.txt in {os.path.abspath('output.txt')}.")



