from random import randint

def create_table(size, caracter):

    table = [[caracter]*size for count in range(size)]

    return table


def show_table(table):

    print("-\t"*len(table))

    for lines in table:

        for colunms in lines:

            print(colunms, end='\t')

        print()
        print()

    print("-\t"*len(table))


def change_caracter(caracter):

    if caracter == 'X':

        return '1'

    elif caracter.isnumeric():

        return str(int(caracter) + 1)

    else: 

        return caracter


def populate_bomb(table):

    size_table = len(table) - 1

    for bomb in range(len(table)):

        while True:

            colunm = randint(0, size_table)
            line = randint(0, size_table)

            if table[line][colunm] != 'B':

                table[line][colunm] = 'B'
                break

        if line == 0 and colunm == 0: 

            table[line + 1][colunm + 1] = change_caracter(table[line + 1][colunm + 1])
            table[line][colunm + 1] = change_caracter(table[line][colunm + 1])
            table[line + 1][colunm] = change_caracter(table[line + 1][colunm])

        elif line == size_table and colunm == 0:

            table[line - 1][colunm + 1] = change_caracter(table[line - 1][colunm + 1])
            table[line - 1][colunm] = change_caracter(table[line - 1][colunm])
            table[line][colunm + 1] = change_caracter(table[line][colunm + 1])

        elif line == 0 and colunm == size_table:

            table[line + 1][colunm - 1] = change_caracter(table[line + 1][colunm - 1])
            table[line + 1][colunm] = change_caracter(table[line + 1][colunm])
            table[line][colunm - 1] = change_caracter(table[line][colunm - 1])

        elif line == size_table and colunm == size_table:

            table[line - 1][colunm - 1] = change_caracter(table[line - 1][colunm - 1])
            table[line][colunm - 1] = change_caracter(table[line][colunm - 1])
            table[line - 1][colunm] = change_caracter(table[line - 1][colunm])

        elif 0 == colunm and 0 < line < size_table:

            table[line + 1][colunm + 1] = change_caracter(table[line + 1][colunm + 1])
            table[line - 1][colunm + 1] = change_caracter(table[line - 1][colunm + 1])
            table[line][colunm + 1] = change_caracter(table[line][colunm + 1])
            table[line + 1][colunm] = change_caracter(table[line + 1][colunm])
            table[line - 1][colunm] = change_caracter(table[line - 1][colunm])

        elif size_table == colunm and 0 < line < size_table:

            table[line - 1][colunm - 1] = change_caracter(table[line - 1][colunm - 1])
            table[line + 1][colunm - 1] = change_caracter(table[line + 1][colunm - 1])
            table[line][colunm - 1] = change_caracter(table[line][colunm - 1])
            table[line + 1][colunm] = change_caracter(table[line + 1][colunm])
            table[line - 1][colunm] = change_caracter(table[line - 1][colunm])

        elif 0  == line and 0 < colunm < size_table:

            table[line + 1][colunm + 1] = change_caracter(table[line + 1][colunm + 1])
            table[line + 1][colunm - 1] = change_caracter(table[line + 1][colunm - 1])
            table[line][colunm + 1] = change_caracter(table[line][colunm + 1])
            table[line][colunm - 1] = change_caracter(table[line][colunm - 1])
            table[line + 1][colunm] = change_caracter(table[line + 1][colunm])

        elif size_table == line and 0 < colunm < size_table:

            table[line - 1][colunm - 1] = change_caracter(table[line - 1][colunm - 1])
            table[line - 1][colunm + 1] = change_caracter(table[line - 1][colunm + 1])
            table[line][colunm + 1] = change_caracter(table[line][colunm + 1])
            table[line][colunm - 1] = change_caracter(table[line][colunm - 1])
            table[line - 1][colunm] = change_caracter(table[line - 1][colunm])

        else:

            table[line + 1][colunm + 1] = change_caracter(table[line + 1][colunm + 1])
            table[line - 1][colunm - 1] = change_caracter(table[line - 1][colunm - 1])
            table[line - 1][colunm + 1] = change_caracter(table[line - 1][colunm + 1])
            table[line + 1][colunm - 1] = change_caracter(table[line + 1][colunm - 1])
            table[line][colunm + 1] = change_caracter(table[line][colunm + 1])
            table[line][colunm - 1] = change_caracter(table[line][colunm - 1])
            table[line + 1][colunm] = change_caracter(table[line + 1][colunm])
            table[line - 1][colunm] = change_caracter(table[line - 1][colunm])

    return table


def get_free_area(table, line_p, colunm_p):

    size_table = len(table) - 1

    table[line_p][colunm_p] = 'F'

    for count in range(len(table)):

        if colunm_p == 0: 

            for item in range(len(table[line_p])):

                if table[line_p][item] in 'XF':

                  table[line_p][item] = 'F'

                else:

                    break  

        elif colunm_p == size_table:
            
            for item in range(len(table[line_p]), 0):

                if table[line_p][item] in 'XF':

                  table[line_p][item] = 'F'

                else:

                    break 
            
        elif 0 < colunm_p < size_table:

            ...

        


    
    
table = create_table(size=10, caracter='X')

table = populate_bomb(table)

get_free_area(table, 5, 5)
