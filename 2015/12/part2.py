import json
def s(e):
    if type(e)==str: return 0
    if type(e)==int: return e
    if type(e)==dict: 
        e=e.values()
        if "red" in e: return 0
    return sum(map(s, e))
print(s(json.load(open("input.txt"))))