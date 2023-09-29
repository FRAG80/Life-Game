
import pygame, time, csv

seed_filename = "seed2.csv"

# seed_array = \ ## example 'glider' array
# [[0, 0, 0, 0, 0, 0],
# [0, 0, 1, 0, 0, 0],
# [0, 0, 0, 1, 0, 0],
# [0, 1, 1, 1, 0, 0],
# [0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 0]]

block_size = 10

def main():
    with open(seed_filename) as f:
        reader = csv.reader(f)
        string_array = list(reader) ## feed this as input to arr_conv1
        seed_array = arr_conv1(string_array) ## list of lists of ints

    Nx, Ny = len(seed_array), len(seed_array[0])
    X, Y = Nx * block_size, Ny * block_size

    array = [row[:] for row in seed_array]
    next_array = [row[:] for row in array]
    iteration = 0

    print("Nx= ", Nx, " Ny= ", Ny)
    print("Seed array when iteration = 0")

    pygame.init()
    display = pygame.display.set_mode((X, Y))
    pygame.display.set_caption('Life game by Fra')
    drawGrid(Nx, Ny, display)

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        display.fill([0,0,0])

        print(f"Array #{iteration}")
        for row in array:
            print(row)
        print()

        for x in range(Nx):
            for y in range(Ny):
                if array[x][y] == 1:
                    cell_on(x, y, block_size, display)
                elif array[x][y] == 0: #se:
                    cell_off(x, y, block_size, display)

        next_array = decide_next_whole(array, next_array)

        print()
        print(f"next_array #{iteration}")

        for row in next_array:
            print(row)
        print()

        array = [row[:] for row in next_array]
        iteration += 1
        # time.sleep(0.3)


def decide_next_whole(array, next_array):
    #selection rule: B3/S23, cell born if 3 neighbours, survives if 2 or 3, dies otherwise
    Nx, Ny = len(array), len(array[0])

    for x in range(Nx):
        for y in range(Ny):

            a, b, c, d, e, f, g, h = 0, 0, 0, 0, 0, 0, 0, 0
            next_state, sum = 0, 0

            a, b, c = array[(x-1)%Nx][(y-1)%Ny], array[(x-1)%Nx][y], array[(x-1)%Nx][(y+1)%Ny]
            d, e = array[x][(y-1)%Ny], array[x][(y+1)%Ny]
            f, g, h = array[(x+1)%Nx][(y-1)%Ny], array[(x+1)%Nx][y], array[(x+1)%Nx][(y+1)%Ny]
            print()
            print(a, b, c)
            print(d, " ", e)
            print(f, g, h)

            sum = a + b + c + d + e + f + g + h
            print(f"x= {x}, y= {y}, sum= ", end="")
            if sum == 3:
                print(sum, " ", "be born", end="    next_state = ")
                next_state = 1
            elif sum == 2:
                print(sum, " ", "survive", end="    next_state = ")
                next_state = array[x][y]
            else:
                print(sum, " ", "die", end="    next_state = ")
                next_state = 0

            print(next_state)
            next_array[x][y] = next_state

    return next_array


def drawGrid(Nx, Ny, display):
    for x in range(Nx):
        for y in range(Ny):
            cell_off(x, y, block_size, display)
            # time.sleep(0.025)
    time.sleep(0.7)


def cell_on(x, y, block_size, display):
    filled_rect = pygame.Rect(x*block_size, y*block_size, block_size, block_size)
    pygame.draw.rect(display, (255, 255, 255), filled_rect, width=0)
    pygame.display.flip()
    # time.sleep(0.02)


def cell_off(x, y, block_size, display):
    filled_rect = pygame.Rect(x*block_size, y*block_size, block_size, block_size)
    pygame.draw.rect(display, (255, 255, 255), filled_rect, width=1)
    pygame.display.flip()
    # time.sleep(0.02)


def arr_conv1(top_list):
    int_top_list = [] ### new integer list of lists
    for row in top_list:
        int_list = [] ### new integer sub list
        for item in row:
            int_item = int(item)
            int_list.append(int_item)
        int_top_list.append(int_list)
    # for row in int_top_list:
    #     print(row)
    return int_top_list


if __name__ == "__main__":
    main()



