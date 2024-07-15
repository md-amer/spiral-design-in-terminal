#Spiral design in terminal
#By Amer

from time import sleep
import os
import copy

grid = []

for i in range(10):
	grid.append([' ',' ',' ',' ',' ',' ',' ',' ',' ',' '])

def print_grid():
	for i in range(len(grid)):
		for j in range(len(grid[0])):
			if j == len(grid[0])-1:
				print(grid[i][j])
			else:
				print(grid[i][j],end=' ')
			
def clear_screen():
	os.system('cls' if os.name == 'nt' else 'clear')
	
t=0.1
def spiral(a,m,n,o):
	if len(a)!= 0:

		for j in range(n):
			grid[o][j] = '*'
			sleep(t)
			clear_screen()
			print_grid()
			
		for i in range(1,m):
			grid[i][n-1] = '*'
			sleep(t)
			clear_screen()
			print_grid()
			
		for j in reversed(range(n)):
			grid[i][j] = '*'
			sleep(t)
			clear_screen()
			print_grid()
			
		for i in reversed(range(1,m)):
			grid[i-1][o] = '*'
			sleep(t)
			clear_screen()
			print_grid()
			
		o += 1
		spiral(a, m-1, n-1, o)
		
spiral(grid, len(grid), len(grid[0]), 0)
