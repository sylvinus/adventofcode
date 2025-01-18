print(sum(
    all(x not in s for x in ("ab","cd","pq","xy")) * 
    (sum(s.count(v) for v in "aeiou")>2) * 
    any(s[i]==s[i+1] for i in range(len(s)-1))
    for s in open("input.txt")
))