def get_input():
   # Ask the player to type a letter
   # We will read that letter
   # We will print that letter back to them
   x = 0
   y = 0
   letter_input = input("Enter a letter: ")
   print("Letter: " + letter_input)
   if (letter_input == "w"):
      y += 1
   elif (letter_input == "s"):
      y += -1  
   elif (letter_input == "a"):
      x += -1 
   elif (letter_input == "d"):
      x += 1      
      
   return (x,y)

def do_logic(x, y):
   if (y > 3 or y < 0):
      quit()
   elif (x > 3 or x < 0):
      quit()  

def add_to_render(map_grid,symbol, pos_x, pos_y):
   temp_grid = map_grid
   temp_grid[pos_x][pos_y] = symbol

   return temp_grid

def render (mapI):

   temp_map = [[" "," "," "],[" "," "," "],[" "," "," "]]



   ix = 0
   iy = 0
   for i in mapI:
      for j in i:
         temp_map[iy][ix] = mapI[ix][iy]
         iy += 1
      ix += 1
      iy = 0

   for i in temp_map:
      for j in i:
         print("|" + str(j) + "|", end='')
      print("\n")

def main():
   player_position_x = 1
   player_position_y = 1
   player_symbol     = "&"

   while(1):
      
      map_grid = [[" "," "," "],[" "," "," "],[" "," "," "]]
      # Do the game
      # Check Changes in Game
      (x,y) = get_input()
      player_position_x += x
      player_position_y += y
      # Do Logic
      ret = do_logic(player_position_x, player_position_y)
      print ("Player Position is currently: [" + str(player_position_x) + "," + str(player_position_y) + "]")

      # Render Output
      map_grid = add_to_render (map_grid,player_symbol, player_position_x, player_position_y)
      render(map_grid)

main()