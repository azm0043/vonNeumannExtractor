InFile = open('out.txt', 'r')  # Open labview file
Extracted = open('extracted_output.txt', 'w')  # open new file
# OutFile = open('binary_file.txt', 'rw')  # open new file

x = 4  # initialize index
scaledShift = x
nextInt = 0  # initialize buffer variable

for line in InFile:  # loop through file
    number = int(line, 16)  # reads numbers as hex and converts to decimal int
    HighBits = (number & 12) >> 2  # mask lower bits and shift
    LowBits = number & 3  # mask upper bits

    if HighBits == 1:
        formInt = '{:2}'.format(0)
        Extracted.write(str(formInt) + '\n')
    if HighBits == 2:
        formInt = '{:2}'.format(1)
        Extracted.write(str(formInt) + '\n')
    if LowBits == 1:
        formInt = '{:2}'.format(0)
        Extracted.write(str(formInt) + '\n')
    if LowBits == 2:
        formInt = '{:2}'.format(1)
        Extracted.write(str(formInt) + '\n')
    # if HighBits == 1:
    #     if 1 > x:
    #         formInt = '{0:>10}'.format(nextInt)
    #         Extracted.write(str(formInt) + '\n')
    #         x = 32
    #         nextInt = 0
    #     nextInt += 0 << (1 * (32-x))
    #     x -= 1
    # if HighBits == 2:
    #     if 1 > x:
    #         formInt = '{0:>10}'.format(nextInt)
    #         Extracted.write(str(formInt) + '\n')
    #         x = 32
    #         nextInt = 0
    #     nextInt += 1 << (1 * (32-x))
    #     x -= 1
    # if LowBits == 1:
    #     if 1 > x:
    #         formInt = '{0:>10}'.format(nextInt)
    #         Extracted.write(str(formInt) + '\n')
    #         x = 32
    #         nextInt = 0
    #     nextInt += 0 << (1 * (32-x))
    #     x -= 1
    # if LowBits == 2:
    #     if 1 > x:
    #         formInt = '{0:>10}'.format(nextInt)
    #         Extracted.write(str(formInt) + '\n')
    #         x = 32
    #         nextInt = 1
    #     nextInt += 1 << (1 * (32-x))
    #     x -= 1

    # if (HighBits == 1) or (HighBits == 2) is True:  # or, if 11 || 00, throw out
    #     if 1 > x:  # if all 32 bits have been filled
    #         formInt = '{0:>10}'.format(nextInt)  # format as right justified, 10 digit decimal number
    #         Extracted.write(str(formInt) + '\n')
    #         x = 16
    #         nextInt = 0
    #     nextInt += HighBits << (1 * (32 - x))  # if all 32 bits have not been filled, shift to next empty location
    #     x -= 1  # decrement index
    # if (LowBits == 1) or (LowBits == 2) is True:
    #     if 1 > x:  # if all 32 bits have been filled
    #         formInt = '{0:>10}'.format(nextInt)  # format as right justified, 10 digit decimal number
    #         Extracted.write(str(formInt) + '\n')
    #         x = 16
    #         nextInt = 0
    #     nextInt += LowBits << (2 * (16 - x))  # if all 32 bits have not been filled, shift to next empty location
    #     x -= 1  # decrement index


Extracted.close()
InFile.close()  # close these files


print('Part Two Complete')
