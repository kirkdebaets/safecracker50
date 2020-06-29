#   Modified from 
#   --Solution for the SafeCracker 50 Puzzle from Creative Crafthouse
#   --By: Eric Pollinger
#   --9/11/2016
#   on 29-June-2020

#   Function to handle the addition of a given slice
def add(slice):
    if row1Outer[(index1 + slice) % 16] != -1:
        valRow1 = row1Outer[(index1 + slice) % 16]
    else:
        valRow1 = row0Inner[slice]

    if row2Outer[(index2 + slice) % 16] != -1:
        valRow2 = row2Outer[(index2 + slice) % 16]
    else:
        valRow2 = row1Inner[(index1 + slice) % 16]

    if row3Outer[(index3 + slice) % 16] != -1:
        valRow3 = row3Outer[(index3 + slice) % 16]
    else:
        valRow3 = row2Inner[(index2 + slice) % 16]

    if row4[(index4 + slice) % 16] != -1:
        valRow4 = row4[(index4 + slice) % 16]
    else:
        valRow4 = row3Inner[(index3 + slice) % 16]
    return row0Outer[slice] + valRow1 + valRow2 + valRow3 + valRow4

if __name__ == "__main__":
    # Raw data (Row0 = base of puzzle)
    row0Outer = [10,1,10,4,5,3,15,16,4,7,0,16,8,4,15,7]
    row0Inner = [10,10,10,15,7,19,18,2,9,27,13,11,13,10,18,10]
    row1Outer = [-1,10,-1,8,-1,10,-1,9,-1,8,-1,8,-1,9,-1,6]
    row1Inner = [1,24,8,10,20,7,20,12,1,10,12,22,0,5,8,5]
    row2Outer = [0,-1,11,-1,8,-1,8,-1,8,-1,10,-1,11,-1,10,-1]
    row2Inner = [20,8,19,10,15,20,12,20,13,13,0,22,19,10,0,5]
    row3Outer = [10,-1,14,-1,11,-1,8,-1,12,-1,11,-1,3,-1,8,-1]
    row3Inner = [6,18,8,17,4,20,4,14,4,5,1,14,10,17,10,5]
    row4 = [8,-1,8,-1,16,-1,19,-1,8,-1,17,-1,6,-1,6,-1]

    count = 0
    for index1 in range(0,16):
        for index2 in range(0,16):
            for index3 in range(0,16):
                for index4 in range(0,16):
                    if add(0) == 50:
                        solution = True
                        for sl in range(1,16):
                            if add(sl) != 50:
                                solution = False
                        if solution == True:
                            count = count + 1
                            # Print Solution
                            print('Solution with index values: ' + str(index1) + ' ' + str(index2) + ' ' + str(index3)
                                  + ' ' + str(index4) + ' for a total number of solutions: ' + str(count))
                            for i in range(0, 16):
                                print('Solution with Slice ' + str(i) + ' values:\t ' + str(row0Outer[i]) + '\t\t'+ str(row1Outer[(index1 + i) % 16]) + '\t\t' + str(
                                row2Outer[(index2 + i) % 16]) + '\t\t' + str(row3Outer[(index3 + i) % 16]) + '\t\t' + str(row4[(index4 + i) % 16]))
    if count == 0:
        print("No Solution Found")
