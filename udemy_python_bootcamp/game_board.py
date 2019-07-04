def update_board(pos, sym, d):
    if pos != '0':
        d[pos] = sym
    print(f" {d['7']} | {d['8']} | {d['9']} \n___|___|___\n {d['4']} | {d['5']} | {d['6']} \n___|___|___\n {d['1']} | {d['2']} | {d['3']} \n   |   |   \n")

#update_board(pos='8',sym='X',d="x")
#update_board(pos='9',sym='O',d="x")




def get_position(sym, d):
    pos = input("Enter position for {sym}'s next move: ")
    d[pos] = sym
    return d

