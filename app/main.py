import utils


while True:
    
    print("""
Choose your game size:
1) Eazy - 5 Bombs
2) Medium - 10 Bombs
3) Hard - 20 Bombs
    """)
    
    choose = int(input('your choose: '))

    match choose:
        case 1:

            size = 5
            break

        case 2:

            size = 10
            break

        case 3:

            size = 20
            break

        case default:

            print('wrong input')



template = utils.create_table(size=size, caracter='X')
template = utils.populate_bomb(table=template)
game = utils.create_table(size=size, caracter='X')

while True:

    utils.show_table(game)

    print("""
your attempt:
    """)

    line = int(input('line: '))
    colunm = int(input('colunm: '))

    if template[line][colunm] == 'X':

        index_free_area = [(line, colunm)]

        index_free_area = utils.get_free_area(template, index_free_area)

        index_free_area = utils.get_numbers_free(template, index_free_area)

        for value in index_free_area:

            line = value[0]
            colunm = value[1]

            template[line][colunm] = 'F' if template[line][colunm] in 'X' else template[line][colunm]
            game[line][colunm] = template[line][colunm]

    elif template[line][colunm].isnumeric():

        game[line][colunm] = template[line][colunm]

    elif template[line][colunm] == 'B':

        print('lose')
        break

    else:

        print('this is a free area')



