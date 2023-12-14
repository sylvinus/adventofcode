def test(grid):
    for i in range(1, len(grid)):
        if grid[i-min(i, len(grid)-i):i]==list(reversed(grid[i:i+min(i, len(grid)-i)])):
            return i
print(sum(
    (test(block.split()) or 0)*100 + (test(list(zip(*block.split()))) or 0)
    for block in open("input.txt").read().split("\n\n")
))