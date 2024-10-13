import pygame
from seaborn import color_palette
from grid import Grid
from sys import version
print(version)

HEIGHT = 800
WIDTH = 800
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
GRIDX = 20
GRIDY = 20

TYPES = {1 : 'GRASS', 2 : 'MOUNTAINS',3 : 'SAND', 4 : 'WATER'}
COLORS = {1 : (38,139,7) , 2 : (100,100,100), 3 : (224,205,169), 4: (153,153,255)}
RULES = {1 : [1,2,3],
         2 : [2,1],
         3 : [3,1,4],
         4 : [4,3]}

grid = Grid(GRIDX,GRIDY, [type for type in TYPES], TYPES, RULES)
#grid.set_values((3,2), [2])
#print(grid)


#grid.collapse((7,3))

def cell_color(grid : Grid, x,y) -> tuple:
    val = grid.get_values((x,y))
    assert type(val) == list
    assert len(val) <= len(TYPES)
    if grid.get_entropy((x,y)) == 1:
        return COLORS[val[0]]
    else:
        palette = color_palette("rocket",len(TYPES))
        return [int(col*255) for col in palette[len(TYPES)-grid.get_entropy((x,y))]]

def render(grid : Grid):
    sizeCell = (WIDTH//GRIDX, HEIGHT//GRIDY)
    for x in range(GRIDX):
        for y in range(GRIDY):
            #raise Exception("bad value in cell")
            pygame.draw.rect(WIN,cell_color(grid, x,y),pygame.Rect(sizeCell[0]*x,sizeCell[1]*y,sizeCell[0],sizeCell[1]))



run = True
clock = pygame.time.Clock()

nxt_cells = []
for x in range(GRIDX):
    for y in range(GRIDY):
        nxt_cells.append((x,y))
    

while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break
    
    #choose cell to collapse
    coords_to_collapse = grid.get_min_entropy(nxt_cells)
    print(coords_to_collapse)

    grid.collapse(coords_to_collapse)
    #nxt_cells.remove(coords_to_collapse)

    WIN.fill(pygame.Color(50,50,255))

    
    render(grid)
    pygame.display.update()
pygame.quit()