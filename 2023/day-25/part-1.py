from collections import defaultdict

with open("input.txt", "r") as f:
    inp = f.readlines()

inp = [l.strip("\n") for l in inp]

# I tried to avoid using networkX, but after a bit I gave up with coming up with a clever solution
# I put it into a random graph visualisation software I could find online (Flourish)
# And the 3 edges became clear: (qqq, mlp), (vsx, zbr), (jxx, qdp) - not my greatest solution
edges_to_remove = [("qqq", "mlp"), ("vsx", "zbr"), ("jxx", "qdp")]

graph = defaultdict(list)
for l in inp:
    fr, *to = l.replace(":", "").split(" ")

    for adj in to:
        if (fr, adj) not in edges_to_remove and (adj, fr) not in edges_to_remove:
            graph[fr].append(adj)
            graph[adj].append(fr)

seen = set()
q = [next(iter(graph))]
while q:
    curr = q.pop()
    if curr not in seen:
        seen.add(curr)
        q += graph[curr]

print(len(seen) * (len(graph) - len(seen)))
