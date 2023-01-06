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

def populate_bomb(table):

    size_table = len(table) - 1

    for bomb in range(len(table)):

        colunm = randint(0, size_table)
        line = randint(0, size_table)

        table[line][colunm] = 'B'

        if 0 in [colunm, line] and size_table in [colunm, line]:

            pass

        else:

            match line:

                case 0:

                    table[line + 1][colunm + 1] = 1 if table[line + 1][colunm + 1] == 'X' else table[line + 1][colunm + 1] + 1
                    table[line + 1][colunm - 1] = 1 if table[line + 1][colunm - 1] == 'X' else table[line + 1][colunm - 1] + 1
                    table[line + 1][colunm] = 1 if table[line + 1][colunm] == 'X' else table[line + 1][colunm] + 1
                    table[line][colunm + 1] = 1 if table[line][colunm + 1] == 'X' else table[line][colunm + 1] + 1
                    table[line][colunm - 1] = 1 if table[line][colunm - 1] == 'X' else table[line][colunm - 1] + 1


                case size_table:

                    table[line - 1][colunm + 1] = 1 if table[line + 1][colunm + 1] == 'X' else table[line + 1][colunm + 1] + 1
                    table[line - 1][colunm - 1] = 1 if table[line + 1][colunm - 1] == 'X' else table[line + 1][colunm - 1] + 1
                    table[line - 1][colunm] = 1 if table[line + 1][colunm] == 'X' else table[line + 1][colunm] + 1
                    table[line][colunm + 1] = 1 if table[line][colunm + 1] == 'X' else table[line][colunm + 1] + 1
                    table[line][colunm - 1] = 1 if table[line][colunm - 1] == 'X' else table[line][colunm - 1] + 1

            match colunm:

                case 0:

                    table[line + 1][colunm + 1] = 1 if table[line][colunm] == 'X' else table[line][colunm] + 1
                    table[line - 1][colunm + 1] = 1 if table[line][colunm] == 'X' else table[line][colunm] + 1
                    table[line][colunm + 1] = 1 if table[line][colunm] == 'X' else table[line][colunm] + 1
                    table[line + 1][colunm] = 1 if table[line][colunm] == 'X' else table[line][colunm] + 1
                    table[line - 1][colunm] = 1 if table[line][colunm] == 'X' else table[line][colunm] + 1

    return table

show_table(populate_bomb(create_table(10, 'X')))