        
def life():
    while True:
        namefile = input("Enter input file name: ")
        try:
            inFile = open(namefile, "r")
            break
        except:
            print("No such file. Try again.")
    while True:
        numgenerations = input("How many new generations would you like to print?")
        if numgenerations.isdigit() is not True:
            print("Not a valid number.")
        else:
            break

    lst = inFile.readlines()
    count = 0
    while (count <= len(numgenerations)):
        print("Generation:", count)
        for i in range(0, len(lst)):
            for j in range(0, len(lst[0])-1):
                if lst[i][j] == "0":
                    print(".", end = " ")
                else:
                    print("*", end = " ")
            print()
        lst = nextGen(lst)
        count = count + 1
    tinyglider = []
    for i in range(1, lst-1):
        newrow = []
        for j in range(1, lst-1):
            newrow.append(lst[i][j])
            tinyglider.append(newrow) 
    count = 0
    while (count <= int(numgenerations)):
        print("Generation: ", count)
        length = readlines(inFile) 
        for i in range(1, lst-1):
            for j in range(1, lst[0]-1):
                if lst[i][j] == 0:
                    print(".", end = " ") 
    
         
     
        
    
    
        
        

    

    
def nextGen(glider):
    " " " Function computes a new grid given the initial grid called glider based on the rules of the Game of Life which determine whether a particular position in a specific row and column will contain a 0 or 1 based on whether its neighboring positions contain a 0 or 1 as well " " "
    gen_new = [[0 for col in glider [0]]for row in glider]
    p = len(glider)
    for l in range(1, p-1):
        q = len(glider[l])
        for m in range(1, q-1):
            initial = []
            initial.append(glider[l][m+1])
            initial.append(glider[l+1][m])
            initial.append(glider[l-1][m+1])
            initial.append(glider[l+1][m-1])
            initial.append(glider[l+1][m+1])
            initial.append(glider[l-1][m-1])
            initial.append(glider[l][m-1])
            initial.append(glider[l-1][m])
            total_value = sum(initial)
            if glider[l][m] == 0:
                if total_value == 3:
                    gen_new[l][m] = 1
                elif total_value <= 1:
                    gen_new[l][m] = 0
                elif total_value >= 4:
                    gen_new[l][m] = 0
                elif total_value <= 2:
                    gen_new[l][m] = 0

            if glider[l][m] == 1:
                if total_value == 3:
                    gen_new[l][m] = 1
                elif total_value >= 4:
                    gen_new[l][m] = 0
                elif total_value <= 1:
                    gen_new[l][m] = 0
                elif total_value == 2:
                    gen_new[l][m] = 1
    return gen_new   

