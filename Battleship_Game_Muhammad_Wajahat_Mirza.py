#BattleShip Game
# There is randomly oriented ship in the grid either horizontal or vertical.
# Ask user to target and sink it for game to over
# Provide the user with the accuracy of sinking the ship

#Process
    # 1. Define and initialize grid
    # 2. Display Grid with col, row names
    # 3. Randomly assign 4 block ship and display
    # 4. Make user interface to interact with grid. Validate Input
    # 5. Place user input on grid
    # 6. Check if ship is sank and calculate accuracy 

import random
import string
import os
import re

num_row = 10
num_col = 10

grid = []
ship_coordinates = []

#Initialize the grid 
def grid_initialize():
    for row in range(num_row):
        h_list = []
        for col in range(num_col):
            h_list.append(" ")
        grid.append(h_list)
        
#Display the grid 
def grid_display():

    #Display Alphabets for the columns of the grid
    alphabet = [" ", " A ", " B  " ," C  "," D  ", " E  ", " F  ", " G  ", " H  ", " I  ", " J  " ]
    for col in range(num_col + 1):
        print(alphabet[col], end=" ")
    print()

    #Display Row number for the columns of the grid
    for row in range(num_row):
        if (row + 1 < 10):
            print(row + 1, end="  ")
        else:
            print(row + 1, end=" ")
        for col in range(num_col):
            print(grid[row][col] + " | ", end=" ")
        print("\n " + " ---+" * num_col)
        print()
        
#Randomly assign ship coordinates and orientation    
def random_ship():
    row_ship_coordinate = random.randint(0,9)
    col_ship_coordinate = random.randint(0,9)
    ship_orientation = random.randint(0,1)
    
    #if ship_orientation is 0, then horizontol
    if (ship_orientation == 0):
        if (col_ship_coordinate <= 6):
            ship_coordinates.append([row_ship_coordinate,col_ship_coordinate])
            ship_coordinates.append([row_ship_coordinate,col_ship_coordinate + 1])
            ship_coordinates.append([row_ship_coordinate,col_ship_coordinate + 2])
            ship_coordinates.append([row_ship_coordinate,col_ship_coordinate + 3])
        else:
            ship_coordinates.append([row_ship_coordinate,col_ship_coordinate])
            ship_coordinates.append([row_ship_coordinate,col_ship_coordinate - 1])
            ship_coordinates.append([row_ship_coordinate,col_ship_coordinate - 2])
            ship_coordinates.append([row_ship_coordinate,col_ship_coordinate - 3])

    #if ship_orientation is 1, then vertical
    else:
        if (row_ship_coordinate <= 6):
            ship_coordinates.append([row_ship_coordinate,col_ship_coordinate])
            ship_coordinates.append([row_ship_coordinate + 1,col_ship_coordinate])
            ship_coordinates.append([row_ship_coordinate + 2,col_ship_coordinate])
            ship_coordinates.append([row_ship_coordinate + 3,col_ship_coordinate])
        else:
            ship_coordinates.append([row_ship_coordinate,col_ship_coordinate])
            ship_coordinates.append([row_ship_coordinate - 1,col_ship_coordinate])
            ship_coordinates.append([row_ship_coordinate - 2,col_ship_coordinate])
            ship_coordinates.append([row_ship_coordinate - 3,col_ship_coordinate])

def user_input():
    coordinate_given = input("Please enter coordinates where you want to hit as 'A1', 'Z3': ").upper()
    # Check if the input does not creat any special characters
    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    # check if input is in wrong format such as '5G'
    while (coordinate_given[0].isdigit() == True) or (coordinate_given[1: ].isalpha() == True) or (regex.search(coordinate_given[:]) != None):
           coordinate_given = input("Please enter coordinates where you want to hit (as 'A1', 'Z3': ").upper()
        

    # Convert string values of col using 'ord' and conver string value of row using 'int'
    coordinate_col = ord(coordinate_given[0])
    coordinate_row = int(coordinate_given[1: ])

    # Range check: check if input for col is in between A-J and for row 1-10
    while ((coordinate_row < 1 or coordinate_row > 10) or (coordinate_col < 65 or coordinate_col > 74)):
        coordinate_given = input("Coordinates are out of range. Please enter valid coordinates: ").upper()
        coordinate_col = ord(coordinate_given[0])
        coordinate_row = int(coordinate_given[1: ])
    # Assign given coordinates a cell on the grid
    grid_row = coordinate_row - 1
    grid_col = coordinate_col - 65
    
    return grid_row, grid_col

def place_target():
    ship_hit_count = 0
    ship_miss_count = 0
    #Run game until all four cells of ship are sank
    while (ship_hit_count < 4):
        target_row, target_col = user_input()

        # To avoid re-entering the same coordinate, use if loop.
        if (grid[target_row][target_col] == " "):
            os.system("cls" if os.name=="nt" else "clear")
            if [target_row,target_col] in ship_coordinates:
                grid[target_row][target_col] = "X"
                ship_hit_count += 1
                print("Ship has been hit!!! Congrats, almost there!")
                
            else:
                grid[target_row][target_col] = "O"
                ship_miss_count += 1
                print("You missed the hit :( Keep trying, don't give up!")

            
            grid_display()

        else:
            print("You have already entered these coordinates previously. Try again!")
        
        accuracy_rate(ship_hit_count, ship_miss_count)

    print("Game over! You have successful sunk the ship. You are pro now.")

def accuracy_rate(ship_hit_count, ship_miss_count):
    accuracy = ( ship_hit_count / (ship_hit_count + ship_miss_count))
    print("Your accuracy of sinking the ship is: ", accuracy)
    

def main():
    grid_initialize()      
    random_ship()
    grid_display()
    place_target()

main()

# End Code 



