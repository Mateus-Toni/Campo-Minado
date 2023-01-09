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

    if caracter in 'XF':

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


def get_free_area(table, index_free_area, len_before=None):

    size_table = len(table) - 1

    size_index = len(index_free_area)

    if len_before:

        new_positions = [*index_free_area[len_before:]]

    else:

        new_positions = index_free_area[:]

    free_area = False

    for value in new_positions:

        line = value[0]
        colunm = value[1]

        if line == 0 and colunm == 0:

            if table[line + 1][colunm + 1] in 'XF' and (line + 1, colunm + 1) not in index_free_area:

                free_area = True
                
                index_free_area.append((line + 1, colunm + 1))

            if table[line][colunm + 1] in 'XF' and (line, colunm + 1) not in index_free_area:

                free_area = True

                index_free_area.append((line, colunm + 1))

            if table[line + 1][colunm] in 'XF' and (line + 1, colunm) not in index_free_area:

                free_area = True

                index_free_area.append((line + 1, colunm))
        
        elif line == size_table and colunm == 0:

            if table[line - 1][colunm + 1] in 'XF' and (line - 1, colunm + 1) not in index_free_area:

                free_area = True

                index_free_area.append((line - 1, colunm + 1))

            if table[line - 1][colunm] in 'XF' and (line - 1, colunm) not in index_free_area:

                free_area = True

                index_free_area.append((line - 1, colunm))

            if table[line][colunm + 1] in 'XF' and (line, colunm + 1) not in index_free_area:

                free_area = True

                index_free_area.append((line, colunm + 1))

        elif line == 0 and colunm == size_table:

            if table[line + 1][colunm - 1] in 'XF' and (line + 1, colunm - 1) not in index_free_area:

                free_area = True

                index_free_area.append((line + 1, colunm - 1))

            if table[line + 1][colunm] in 'XF' and (line + 1, colunm) not in index_free_area:

                free_area = True

                index_free_area.append((line + 1, colunm))

            if table[line][colunm - 1] in 'XF' and (line, colunm - 1) not in index_free_area:

                free_area = True

                index_free_area.append((line, colunm - 1))

        elif line == size_table and colunm == size_table:

            if table[line - 1][colunm - 1] in 'XF' and (line - 1, colunm - 1) not in index_free_area:

                free_area = True
                
                index_free_area.append((line - 1, colunm - 1))

            if table[line][colunm - 1] in 'XF' and (line, colunm - 1) not in index_free_area:

                free_area = True
                
                index_free_area.append((line, colunm - 1))

            if table[line - 1][colunm] in 'XF' and (line - 1, colunm) not in index_free_area:

                free_area = True
                
                index_free_area.append((line - 1, colunm))

        elif 0 == colunm and 0 < line < size_table:

            if table[line + 1][colunm + 1] in 'XF' and (line + 1, colunm + 1) not in index_free_area:

                free_area = True

                index_free_area.append((line + 1, colunm + 1))


            if table[line - 1][colunm + 1] in 'XF' and (line - 1, colunm + 1) not in index_free_area:

                free_area = True

                index_free_area.append((line - 1, colunm + 1))


            if table[line][colunm + 1] in 'XF' and (line, colunm + 1) not in index_free_area:

                free_area = True

                index_free_area.append((line, colunm + 1))


            if table[line + 1][colunm] in 'XF' and (line + 1, colunm) not in index_free_area:

                free_area = True

                index_free_area.append((line + 1, colunm))


            if table[line - 1][colunm] in 'XF' and (line - 1, colunm) not in index_free_area:

                free_area = True

                index_free_area.append((line - 1, colunm))


        elif size_table == colunm and 0 < line < size_table:

            if table[line - 1][colunm - 1] in 'XF' and (line - 1, colunm - 1) not in index_free_area:

                free_area = True

                index_free_area.append((line - 1, colunm - 1))


            if table[line + 1][colunm - 1] in 'XF' and (line + 1, colunm - 1) not in index_free_area:

                free_area = True

                index_free_area.append((line + 1, colunm - 1))


            if table[line][colunm - 1] in 'XF' and (line, colunm - 1) not in index_free_area:

                free_area = True

                index_free_area.append((line, colunm - 1))


            if table[line + 1][colunm] in 'XF' and (line + 1, colunm) not in index_free_area:

                free_area = True

                index_free_area.append((line + 1, colunm))


            if table[line - 1][colunm] in 'XF' and (line - 1, colunm) not in index_free_area:

                free_area = True

                index_free_area.append((line - 1, colunm))


        elif 0  == line and 0 < colunm < size_table:

            if table[line + 1][colunm + 1] in 'XF' and (line + 1, colunm + 1) not in index_free_area:

                free_area = True

                index_free_area.append((line + 1, colunm + 1))


            if table[line + 1][colunm - 1] in 'XF' and (line + 1, colunm - 1) not in index_free_area:

                free_area = True

                index_free_area.append((line + 1, colunm - 1))


            if table[line][colunm + 1] in 'XF' and (line, colunm + 1) not in index_free_area:

                free_area = True

                index_free_area.append((line, colunm + 1))


            if table[line][colunm - 1] in 'XF' and (line, colunm - 1) not in index_free_area:

                free_area = True

                index_free_area.append((line, colunm - 1))


            if table[line + 1][colunm] in 'XF' and (line + 1, colunm) not in index_free_area:

                free_area = True

                index_free_area.append((line + 1, colunm))


        elif size_table == line and 0 < colunm < size_table:

            if table[line - 1][colunm - 1] in 'XF' and (line - 1, colunm - 1) not in index_free_area:

                free_area = True

                index_free_area.append((line - 1, colunm - 1))


            if table[line - 1][colunm + 1] in 'XF' and (line - 1, colunm + 1) not in index_free_area:

                free_area = True

                index_free_area.append((line - 1, colunm + 1))


            if table[line][colunm + 1] in 'XF' and (line, colunm + 1) not in index_free_area:

                free_area = True

                index_free_area.append((line, colunm + 1))


            if table[line][colunm - 1] in 'XF' and (line, colunm - 1) not in index_free_area:

                free_area = True

                index_free_area.append((line, colunm - 1))


            if table[line - 1][colunm] in 'XF' and (line - 1, colunm) not in index_free_area:

                free_area = True

                index_free_area.append((line - 1, colunm))

        else:

            if table[line + 1][colunm + 1] in 'XF' and (line + 1, colunm + 1) not in index_free_area:

                free_area = True

                index_free_area.append((line + 1, colunm + 1))


            if table[line - 1][colunm - 1] in 'XF' and (line - 1, colunm - 1) not in index_free_area:
            
                free_area = True

                index_free_area.append((line - 1, colunm - 1))


            if table[line - 1][colunm + 1] in 'XF' and(line - 1, colunm + 1) not in index_free_area:

                free_area = True

                index_free_area.append((line - 1, colunm + 1))


            if table[line + 1][colunm - 1] in 'XF' and (line + 1, colunm - 1) not in index_free_area:
        
                free_area = True

                index_free_area.append((line + 1, colunm - 1))


            if table[line][colunm + 1] in 'XF' and (line, colunm + 1) not in index_free_area:

                free_area = True

                index_free_area.append((line, colunm + 1))


            if table[line][colunm - 1] in 'XF' and (line, colunm - 1) not in index_free_area:

                free_area = True

                index_free_area.append((line, colunm - 1))

            
            if table[line + 1][colunm] in 'XF' and (line + 1, colunm) not in index_free_area:

                free_area = True

                index_free_area.append((line + 1, colunm))

            
            if table[line - 1][colunm] in 'XF' and (line - 1, colunm) not in index_free_area:

                free_area = True

                index_free_area.append((line - 1, colunm))

    if free_area:

        return get_free_area(table, index_free_area, len_before=size_index)

    else: 
        
        return index_free_area


