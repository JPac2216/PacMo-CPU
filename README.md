# PacMo-CPU
Innovative CPU

Machine Code: 16 bits
- Opcode: ADD (00), SUB (01), LDR (10), STR (11) -> 2 bits
- readreg1, readreg2, dstreg -> 2 bits each
- imm -> 10 bits
- filler -> 8 bits

for ADD & SUB:  
EX: ADD X0, X1, X2  
EX: ADD X0, X1, 5

filler: 11110000

| Opcode (2 bit) | Reg2 (2 bit) | filler (8 bit) | Reg1 (2 bit) | DstReg (2 bit) |
for imm:
| Opcode (2 bit) | imm (10 bit) | Reg1 (2 bit) | DstReg (2 bit) |

for LDR & STR:  
EX: LDR X0, [X1, 5]  

| Opcode (2 bit) | imm (10 bit) | Reg1 (2 bit) | DstReg (2 bit) |
