import collections
def traverse(graph, start):
    edges, nodes, frontier = collections.Counter(), {start: 0}, [(start, 0)]
    while len(frontier) > 0:
        src, i = frontier.pop(0)
        for dest in sorted(graph[src]):
            if dest not in nodes:
                nodes[dest] = i
                # Count the number of shortest paths though that edge
                edges[(min(dest, src),max(dest, src))] += len(graph)-i
                frontier.append((dest, i+1))
    return nodes, edges
graph = {k: set(v.split()) for k, v in (line.split(": ") for line in open("input.txt"))}
for k, s in tuple(graph.items()):
    for v in s:
        graph.setdefault(v, set())
        graph[v].add(k)
for _ in range(3):
    edgesum = collections.Counter()
    for start in graph.keys():
        _, edges = traverse(graph, start)
        for k, v in edges.items():
            edgesum[k] += v
    a, b = edgesum.most_common(1)[0][0]
    graph[a].discard(b)
    graph[b].discard(a)
nodes, _ = traverse(graph, a)
print(len(nodes)*(len(graph)-len(nodes)))