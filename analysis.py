#!/bin/env python3.0
import math
task1_result = {"stylus":[], "mouse":[]}
task2_part1_result = {"stylus":{"time":[], "error":[]}, "mouse":{"time":[], "error":[]}}
task2_part2_result = {"stylus":{"time":[], "error":[]}, "mouse":{"time":[], "error":[]}}
task2_part3_result = {"stylus":{"time":[], "error":[]}, "mouse":{"time":[], "error":[]}}
task2_part4_result = {"stylus":{"time":[], "error":[]}, "mouse":{"time":[], "error":[]}}
task2_part5_result = {"stylus":{"time":[], "error":[]}, "mouse":{"time":[], "error":[]}}

task4_part1_result = {"stylus":{"time":[], "error":[]}, "mouse":{"time":[], "error":[]}}
task4_part2_result = {"stylus":{"time":[], "error":[]}, "mouse":{"time":[], "error":[]}}
task4_part3_result = {"stylus":{"time":[], "error":[]}, "mouse":{"time":[], "error":[]}}

    

def analyze(file):
    line = file.readline()
    while line:
        if "Start tracking" in line:
            if "task1a" in line:
                file = task1(file, "stylus")
            elif "task1b" in line:
                file = task1(file, "mouse")
            elif "task2a" in line:
                if "Part 1" in line:
                    file = task2_part1(file, "stylus")
                elif "Part 2" in line:
                    file = task2_part2(file, "stylus")
                elif "Part 3" in line:
                    file = task2_part3(file, "stylus")
                elif "Part 4" in line:
                    file = task2_part4(file, "stylus")
                elif "Part 5" in line:
                    file = task2_part5(file, "stylus")
            elif "task2b" in line:
                if "Part 1" in line:
                    file = task2_part1(file, "mouse")
                elif "Part 2" in line:
                    file = task2_part2(file, "mouse")
                elif "Part 3" in line:
                    file = task2_part3(file, "mouse")
                elif "Part 4" in line:
                    file = task2_part4(file, "mouse")
                elif "Part 5" in line:
                    file = task2_part5(file, "mouse")
            elif "task4a" in line:
                if "Part 1" in line:
                    file = task4_part1(file, "stylus")
                elif "Part 2" in line:
                    file = task4_part2(file, "stylus")
                elif "Part 3" in line:
                    file = task4_part3(file, "stylus") 
            elif "task4b" in line:
                if "Part 1" in line:
                    file = task4_part1(file, "mouse")
                elif "Part 2" in line:
                    file = task4_part2(file, "mouse")
                elif "Part 3" in line:
                    file = task4_part3(file, "mouse")
                
        line = file.readline()
    
def distance_from_origin(x, y):
    return math.sqrt((x**2 + y**2))
    
def task4(file, result, input, radius):
    
    line = file.readline()
    while not "Timestamp" in line:
        line = file.readline()
        
    init_x = int(line.split(" ")[3][2:-1])
    init_y = int(line.split(" ")[4][2:])
    start_time = int(line.split(" ")[2][:-1])
    origin = (init_x + radius, init_y)
    total_error = 0
    
    while (not "Stop tracking" in line) and ("task4" in line):
        if "Timestamp" in line:
            x = int(line.split(" ")[3][2:-1])
            y = int(line.split(" ")[4][2:])
    
            drawn_radius = int(distance_from_origin(origin[0] - x, y - origin[1]))
    
            total_error += abs(drawn_radius - radius)
                
            end_time = int(line.split(" ")[2][:-1])
        line = file.readline()
        
    total_time = end_time - start_time
    result[input]["time"].append(total_time)
    result[input]["error"].append(int(total_error))
    
    return file
    


def task4_part1(file, input):
    return task4(file, task4_part1_result, input, 120)
    
def task4_part2(file, input):
    return task4(file, task4_part2_result, input, 50)
    
def task4_part3(file, input):
    return task4(file, task4_part3_result, input, 120)

def task2(file, result, input, start, end):
    equation = line_solver(start[0], start[1], end[0], end[1]) 
    line = file.readline()
    start_time = int(line.split(" ")[2][:-1])
    total_error = 0

    while (not "Stop tracking" in line) and ("task2" in line):
        if "Timestamp" in line:
            split_line = line.split(" ")
            x = int(split_line[3][2:-1])
            y = int(split_line[4][2:])
            
            y_actual = equation["m"]*x + equation["b"]
            total_error += abs(y_actual - y)
            end_time = int(line.split(" ")[2][:-1])
        line = file.readline()
        
    total_time = end_time - start_time
    result[input]["time"].append(total_time)
    result[input]["error"].append(int(total_error))
    
    return file
   
def line_solver(x1, y1, x2, y2):
    m = float(y2 - y1)/(x2 - x1)
    b = y1 - (m*x1)
    return {"m": m, "b": b}
    

def task2_part1(file, input):
    return task2(file, task2_part1_result, input, (350, 250), (500, 250))
    
def task2_part2(file, input):
    return task2(file, task2_part2_result, input, (250, 250), (600, 250))
    
def task2_part3(file, input):
    return task2(file, task2_part3_result, input, (100, 140), (300, 250))

def task2_part4(file, input):
    return task2(file, task2_part4_result, input, (400, 440), (600, 150))

def task2_part5(file, input):
    return task2(file, task2_part5_result, input, (100, 140), (600, 250))
    
def task1(file, input):
    line = file.readline()
    split_line = line.split(" ")
    start_time = int(split_line[2][:-1])
    line = file.readline()
    
    while (not "Stop tracking" in line) and ("task1" in line):
        if "Timestamp" in line:
            end_time = int(line.split(" ")[2][:-1])
        line = file.readline()
    task1_result[input].append(end_time - start_time)
    return file
    
    
if __name__ == "__main__":
    files = ['ex1.txt','ex2.txt','ex3.txt','ex4.txt','ex5.txt','ex6.txt','ex7.txt','ex8.txt','ex9.txt']
    for f_name in files:
        f = open(f_name, 'r')
        analyze(f)
    
    
    print ("task1:", task1_result,'\n')
    print ("task2.1:", task2_part1_result,'\n')
    print ("task2.2:", task2_part2_result,'\n')
    print ("task2.3:", task2_part3_result,'\n')
    print ("task2.4:", task2_part4_result,'\n')
    print ("task2.5:", task2_part5_result,'\n')
    print ("task4.1:", task4_part1_result,'\n')
    print ("task4.2:", task4_part2_result,'\n')
    print ("task4.3:", task4_part3_result,'\n')
    