#coding: utf-8
import pygame
from pygame.locals import *
from random  import randint
global room_n , room_m , room_szie , screen_size
room_n = 30
room_m = 30
room_size = 25
screen_size = 800
White = (255,255,255)
Black  = (0,0,0)

class Room() :
    def __init__(self,x,y) :
        self.x , self.y = x , y
        self.walls , self.visited = [1,1,1,1] , False

def draw_line(screen,begin,walls,size,r_color) :
    x = begin[0]
    y = begin[1]
    change = [[0,0,1,0],[1,0,1,1],[1,1,0,1],[0,1,0,0]]
    for index , wall in enumerate(walls) :
        temp = change[index]
        if wall :
            pygame.draw.line(screen,r_color,(x+temp[0]*size,y+temp[1]*size),(x+temp[2]*size,y+temp[3]*size))

def create_map(m,n) :
    room = [[ 0 for col in range(n)] for row in range(m) ]
    for i in range(m) :
        for j in range(n) :
            room[i][j] = Room(i,j)
    return room

def go_to_next(room,now) :
    temp = [None,None,None,None]
    have = False
    change = [[0,-1],[1,0],[0,1],[-1,0]]
    next_list = [2,3,0,1]
    for index , item in enumerate(change) :
        tx ,ty = now.x + item[0] ,  now.y + item[1]
        if tx in range(0,room_m)  and ty in range(0,room_n) and (room[tx][ty].visited == False) :
            temp[index] = room[tx][ty]
            have = True
    while have :
        s = randint(0,3)
        if temp[s] != None :
            next_room = temp[s]
            now.walls[s] = 0
            next_room.walls[next_list[s]] = 0
            return next_room
    return None

def create_maze(room,next_room) :
    stack = []
    while True :
        if next_room != None :
            if next_room.visited == False :
                next_room.visited = True
                stack.append(next_room)
            next_room = go_to_next(room,next_room)
        else :
            next_room = stack.pop()
            if len(stack) == 0 :
                break

if __name__ == '__main__' :
    pygame.init()
    screen=pygame.display.set_mode([screen_size,screen_size])
    screen.fill(White)
    clock=pygame.time.Clock()
    room = create_map(room_m,room_n)
    start_point = [0,0]
    start_room = room[0][0]
    create_maze(room,start_room)
    for i in range(room_m) :
        for j in range(room_n) :
            start_point[0] = 25 + i * room_size
            start_point[1] = 25 + j * room_size
            draw_line(screen,start_point,room[i][j].walls,room_size,Black)
    while True :
        for event in pygame.event.get():
            if event.type==QUIT:
                break
        pygame.display.flip()
    pygame.quit()
