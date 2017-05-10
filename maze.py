#coding: utf-8
from __future__ import division
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
Red = (255,0,0)
Path = []

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
def go_out(screen,r_color,room1,room2,size) :
    px , py = 25 + room1.x*size + size/2 , 25 + room1.y*size + size/2
    tx , ty = 25 + room2.x*size + size/2 , 25 + room2.y*size + size/2
    pygame.draw.line(screen,r_color,(px,py),(tx,ty))

def backtrack_maze(room_list,room,screen) :
    change = [[0,-1],[1,0],[0,1],[-1,0]]
    Path.append(room)
    room.visited = False
    if room.x == 29 and  room.y == 29 :
        for index , item in enumerate(Path) :
            if index == len(Path) - 1 :
                break
            go_out(screen,Red,item,Path[index+1],room_size)
    for index , item in enumerate(change) :
        tx , ty = room.x + item[0] , room.y + item[1]
        if tx in range(0,room_m)  and ty in range(0,room_n) and ( room.walls[index] == 0 )  and (room_list[tx][ty].visited == True ):
            backtrack_maze(room_list,room_list[tx][ty],screen)
    Path.pop()
    room.visited = True

if __name__ == '__main__' :
    pygame.init()
    screen=pygame.display.set_mode([screen_size,screen_size])
    screen.fill(White)
    room = create_map(room_m,room_n)
    start_point = [0,0]
    create_maze(room,room[0][0])
    for i in range(room_m) :
        for j in range(room_n) :
            start_point[0] = 25 + i * room_size
            start_point[1] = 25 + j * room_size
            draw_line(screen,start_point,room[i][j].walls,room_size,Black)
    backtrack_maze(room,room[0][0],screen)
    pygame.draw.circle(screen,Red,[25+12,25+12],5,5)
    pygame.draw.circle(screen,Red,[775-12,775-12],5,5)
    while True :
        for event in pygame.event.get():
            if event.type==QUIT:
                break
        pygame.display.flip()
    pygame.quit()
