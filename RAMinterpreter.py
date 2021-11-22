# add = 1; tail = 2; clr = 3; assign = 4; gotoa = 5; gotob = 6; jmpa = 7; jpmb = 8; continue = 9
RAMconcat = [[-1, 3, 4, 0, 1],
             [-1, 4, 4, 0, 2],
             [0,  4,  8, 1, 1],
             [-1, 4,  8, 2, 2],
             [-1, 0,  6, 0, 3],
             [1,  0,  1, 1, 3],
             [-1, 0,  2, 0, 4],
             [-1, 0,  5, 0, 0],
             [2,  0,  1, 2, 3],
             [-1, 0,  2, 0, 4],
             [-1, 0,  5, 0, 0],
             [3,  1,  4, 0, 3],
             [-1, 0,  9, 0, 0]]


def findNext(instructions, pc, nextline, order):
    # find above
    if order == -1:
        for i in range(pc-1, -1, -1):
            if instructions[i][0] != -1 and instructions[i][0] == nextline:
                return i
    # find below
    else:
        for i in range(pc+1, len(instructions)):
            if instructions[i][0] != -1 and instructions[i][0] == nextline:
                return i

def RAMinterp(instructions, n, p, k, input):
    # n is te number of input registers
    # p is the total number of registers
    # k is the alphabet size
    # input is the input string
    # input2 is the optional string for concatenation

    # initializing registers
    registers = [""] * p

    # initializing input registers
    for i in range(0, n):
        registers[i] = input[i]

    lines = []
    alphabets = []
    for i in range(k):
        i += 1
        alphabets.append(str(i))

    # print('initialized registers are ' + ' '.join(str(ele) for ele in registers))
    pc = 0
    stop = False

    while not stop:
        # print('each round registers are ' + ' '.join(str(ele) for ele in registers))
        instruction = instructions[pc]
        # print('instruction for this round is ' + ' '.join(str(ele) for ele in instruction))
        # print('pc is ' + str(pc))
        line, register, operation, alphabet, last = instruction
        if operation == 1:
            # add
            registers[last-1] += str(alphabets[alphabet-1])
            pc += 1
        elif operation == 2:
            # tail
            if len(registers[last-1]) > 1:
              registers[last-1] = registers[last-1][1:]
            else:
              registers[last-1] = ""
            pc += 1
        elif operation == 3:
            # clr
            registers[last-1] = ""
            pc += 1
        elif operation == 4:
            # assign
            registers[register-1] = registers[last-1]
            pc += 1
        elif operation == 5:
            # goto above
            pc = findNext(instructions, pc, last, -1)
        elif operation == 6:
            # goto below
            pc = findNext(instructions, pc, last, 1)
        elif operation == 7:
            # jmp a
            if len(registers[register-1]) > 0 and registers[register-1][0] == alphabets[alphabet-1]:
                    pc = findNext(instructions, pc, last, -1)
            else:
                pc += 1
        elif operation == 8:
            # jmp b
            if len(registers[register-1]) > 0 and registers[register-1][0] == alphabets[alphabet-1]:
                pc = findNext(instructions, pc, last, 1)
            else:
                pc += 1
        elif operation == 9:
            # continue
            if pc == len(instructions)-1:
              stop = True
            else:
              pc += 1

    print('The inputs are: ')
    print(input)
    print('Result is ' + registers[0])
    return registers[0]

theinput = ["1212", "2121"]
RAMinterp(RAMconcat, 2, 4, 2, theinput)
