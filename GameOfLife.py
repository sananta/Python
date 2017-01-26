## Srivarshini Ananta
## GameOfLife.py
## March 6, 2016

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
                 
