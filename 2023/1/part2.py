import re
s = 0
for line in open("input.txt", "r").readlines():
    line_orig = line
    for y in range(len(line)):
        for i, w in enumerate(("one", "two", "three", "four", "five", "six", "seven", "eight", "nine")):
            line = line[:y].replace(w, str(i+1)) + line[y:]
    s += int(re.search("([0-9])", line)[1]) * 10
    
    line = line_orig
    for y in reversed(range(len(line))):
        for i, w in enumerate(("one", "two", "three", "four", "five", "six", "seven", "eight", "nine")):
            line = line[:y] + line[y:].replace(w, str(i+1))
    
    s += int(re.search("([0-9])[^0-9]*$", line)[1])

print(s)

