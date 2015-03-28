task1_result = {"stylus":[], "mouse":[]}
task2_part1_result = {"stylus":{"time":[], "error":[]}, "mouse":{"time":[], "error":[]}}
task2_part2_result = {"stylus":{"time":[], "error":[]}, "mouse":{"time":[], "error":[]}}
task2_part3_result = {"stylus":{"time":[], "error":[]}, "mouse":{"time":[], "error":[]}}
task2_part4_result = {"stylus":{"time":[], "error":[]}, "mouse":{"time":[], "error":[]}}
task2_part5_result = {"stylus":{"time":[], "error":[]}, "mouse":{"time":[], "error":[]}}

task4_result = {"stylus":[], "mouse":[]}

    

def analyze(file):
    line = file.readline()
    while line:
        if "Start tracking" in line:
            if "task1a" in line:
                file = task1(file, "stylus")
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
            elif "task1b" in line:
                file = task1(file, "mouse")
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
        line = file.readline()
            
         
def task2(file, result, input, start, end):
    equation = line_solver(start[0], start[1], end[0], end[1]) 
    line = file.readline()
    start_time = int(line.split(" ")[2][:-1])
    total_error = 0

    while not "Stop tracking" in line:
        split_line = line.split(" ")
        x = int(split_line[3][2:-1])
        y = int(split_line[4][2:])
        
        y_actual = equation["m"]*x + equation["b"]
        y_error = abs(y_actual - y)
        total_error += y_error
        end_time = int(line.split(" ")[2][:-1])
        line = file.readline()
        
    total_time = end_time - start_time
    result[input]["time"] = total_time
    result[input]["error"] = int(total_error)
    
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
    count = 2
    
    while count < 5:
        line = file.readline()
        split_line = line.split(" ")
        end_time = int(split_line[2][:-1])
        line = file.readline()
        count += 1
    task1_result[input].append(end_time - start_time)
    return file
    
    
if __name__ == "__main__":
    f = open('ex3.txt', 'r')
    analyze(f)
    
    print "task1:", task1_result,'\n'
    print "task2.1:", task2_part1_result,'\n'
    print "task2.2:", task2_part2_result,'\n'
    print "task2.3:", task2_part3_result,'\n'
    print "task2.4:", task2_part4_result,'\n'
    print "task2.5:", task2_part5_result,'\n'
    