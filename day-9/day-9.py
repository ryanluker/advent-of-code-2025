# Day 9: Movie Theater
#
# Calculate areas based on the rectangles drawn from
# red tile placements (see example below).
#
# 0 1 2 3 4
# 1 . . . .
# 2 . # 0 0
# 3 . 0 0 0
# 4 . 0 0 #
#
# The above example would have two red tiles ([2,2] and [4,4])
# which would result in an area of 3x3 (9).

red_tiles = []
with open('input.txt', 'r') as f:
    for line in f.readlines():
        strip_line = line.strip()
        x, y = (int(tile) for tile in strip_line.split(','))
        red_tiles.append((x,y))

# Iterate over each red tile and construct a paired list of rectangles
tile_pairings = []
for corner_tile_one in red_tiles:
    # Store tuples of tile pairing with their area amount
    for corner_tile_two in red_tiles:
        # Skip the same tiles from the pairing list
        if corner_tile_one == corner_tile_two:
            continue
        # Calculate the area by finding the abs length and abs width via the tile points
        area_rect = (abs(corner_tile_one[0] - corner_tile_two[0]) + 1) * (abs(corner_tile_one[1] - corner_tile_two[1]) + 1)
        tile_rect = (corner_tile_one, corner_tile_two, area_rect)
        tile_pairings.append(tile_rect)

# Sort the tile pairings based on area and print the largest
tile_pairings.sort(key=lambda tile_pair: tile_pair[2])
biggest_tile = tile_pairings[-1]
print(f"biggest tile:{biggest_tile[0], biggest_tile[1]} | area:{biggest_tile[2]}")
