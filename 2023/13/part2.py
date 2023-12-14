def folds(grid, factor=1):
    for i in range(1, len(grid)):
        if grid[i-min(i, len(grid)-i):i]==list(reversed(grid[i:i+min(i, len(grid)-i)])):
            yield i*factor
mirrors = lambda block: (set(folds(block.split(), factor=100)), set(folds(list(zip(*block.split())))))
def score(block):
    original = mirrors(block)
    for i in range(len(block)):
        if block[i] != "\n":
            new = mirrors(block[:i] + ("." if block[i]=="#" else "#") + block[i+1:])
            diff = (new[0].difference(original[0]), new[1].difference(original[1]))
            if len(diff[0])+len(diff[1]) == 1:
                return sum(diff[0]) + sum(diff[1])
print(sum(map(score, open("input.txt").read().split("\n\n"))))