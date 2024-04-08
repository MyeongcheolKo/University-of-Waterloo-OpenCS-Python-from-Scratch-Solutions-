def box_sides(length, width, height): 
   big_side = length * height
   small_side = width * height
   return 2 * (big_side + small_side)
