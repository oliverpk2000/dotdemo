import pygame, random, sys

def add_point():
    x_cord = random.randint(0, screen_width)
    y_cord = random.randint(0, screen_height)
    width = random.randint(0, 50)
    height = random.randint(0,50)
    point = pygame.Rect(x_cord,y_cord,width,height)
    point_color = pygame.Color(random.randint(0,255),random.randint(0,255),random.randint(0,255))
    points.append(point)
    colors.append(point_color)

def draw_points():
    start = 0
    if(len(points) > 50):
        start = len(points) - 50
        points.remove(points[start -1])
        colors.remove(colors[start -1])
    for i in range(0, len(points)):
            pygame.draw.rect(screen, colors[i], points[i])

screen_width = 1280
screen_height = 960
go = False
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("dotdemo")
pygame.init()
points = []
colors = []

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print(len(points))
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                go = not go
    
    if go:    
        add_point()
        draw_points()
        pygame.display.flip()
