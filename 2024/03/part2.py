import re
print(sum(int(a)*int(b) for a,b in re.findall(r"mul\((\d+)\,(\d+)\)",re.sub(r"don't\(\)[\s\S]*?(do\(\)|$)","",open("input.txt").read()))))