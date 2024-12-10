**PacMo CPU User Manual**  
Matthew Mohamed & Jake Paccione

PacMo is a 16-bit CPU with four general-purpose registers (X0-X3), two read ports, and one write port. PacMo can perform addition and subtraction of two 16-bit numbers, one number coming from a register and the second either coming from a register or an immediate number. PacMo can also store data in memory using an immediate number for the offset and load data from memory using an immediate number as the offset.

**Usage:**

- Download the ‘PacMo CPU Package’ and ensure the following files are in your saved directory:  
  - PacMo.circ  
  - assembler.py  
- Create and name your ARM64 assembly file to **demo.s** and place it in the same directory as the pre-existing program files.  
- Open *assembler.py* in VS Code (or any suitable IDE) and run it inside of a terminal window. This should create an output file called **output.txt** in the same directory as the program files.  
- Open *PacMo.circ* and locate the instruction memory in the Logisim circuit on the left side.  
  - Right Click and use 'Load Image' to upload the **output.txt** for usage.  
- After the instruction data is loaded, find the ‘Simulate’ tab in the top left of Logisim, and either manually tick through the program or enable ‘Auto-Tick’ to automatically run through the program. You should see the registers and/or the memory update according to the instructions.  
- To reset the circuit/simulation, find the ‘Simulate’ tab once again and use ‘Reset Simulation’ (CTRL R).

**Instruction Syntax:**  
Our instruction set mirrors the syntax of ARM64 Assembly. Here is a quick rundown of our basic instructions.

- ADD Xd, Xn, Xm : *Xd \= Xn \+ Xm*  
- ADD Xd, Xn, simm10 : *Xd \= Xn \+ simm10*  
- SUB Xd, Xn, Xm : *Xd \= Xn \- Xm*  
- SUB Xd, Xn, simm10 : *Xd \= Xn \- simm10*  
- LDR Xt, \[base, uimm10\] : loads a halfword from memory addressed by base+uimm10 to Xt.  
- STR Xt, \[base, uimm10\] : stores a halfword from Xt to memory addressed by base+uimm10;

***Binary Encodings:***  
ADD / SUB:  
	*for register addition:*  
| Opcode (00/01) | Reg2 (2 bit) | 11110000 | Reg1 (2 bit) | DstReg (2 bit) |  
*for imm:*  
| Opcode (00/01) | simm10 | Reg1 (2 bit) | DstReg (2 bit) |  
LDR / STR:  
	| Opcode (10/11) | uimm10 | Reg1 (2 bit) | DstReg (2 bit) |

Here are some quick notes on the limitations of the 16-bit CPU:

- There are 4 general purpose registers, ranging from X0-X3. Instructions such as:   
  **ADD X5, X0, X1** will not perform correctly.  
- You may not directly add a negative immediate integer to a register. The only way to have a negative number is to subtract two registers.  
- The maximum positive integer available in the arithmetic instructions is 511\.  
- The maximum offset in the data transfer instructions is 1023\.

**Job Descriptions:**  
Matthew Mohamed and Jake Paccione collaborated effectively throughout this project while also splitting up parts to make tasks more efficient. While already collaborating together on Labs 8 and 9 in class, Matt and Jake took their already existing register file and RAM and placed it in a new Logisim file. From there, Matt began handling the majority of the wiring and design in the circuit while Jake moved on to plan out the design of the machine code and the assembler python file. They decided to mirror ARM64 assembly using 16-bit machine code for ease of use and familiarity. While each having their own tasks, Matt and Jake still collaborated and helped each other to solve common bugs in the project, and would often switch roles to broaden perspectives and potential solutions for issues.  
