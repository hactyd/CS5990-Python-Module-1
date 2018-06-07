def board_draw(height, width):
    i = 1
    for j in range(height):
        print(" ___ " * width)
        if i <= height:
            for k in range(height):
                print( " |  " * (width + 1))
    print(" ___ " * width)



if __name__ == "__main__":
    heightinp= int(input("Enter the height of the board: "))
    widthinp= int(input("Enter the width of the board: "))
    board_draw(heightinp,widthinp)
