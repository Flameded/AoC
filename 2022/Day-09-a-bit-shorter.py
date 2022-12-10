with open("input.txt", "r") as f:
    inp = [l.split() for l in f.readlines()]

part = 2
snake, visited = [[0, 0] for _ in range(part**3 + part)], set()
for direction, amount in inp:
    for _ in range(int(amount)): 
        snake[0][0] += 1 if direction == "R" else -1 if direction == "L" else 0
        snake[0][1] += 1 if direction == "U" else -1 if direction == "D" else 0

        for i in range(1, len(snake)):
            h, t = snake[i - 1], snake[i] 
            if not (abs(h[0] - t[0]) <= 1 and abs(h[1] - t[1]) <= 1):
                snake[i] = [t[i] + (0 if h[i] == t[i] else 1 if h[i] > t[i] else -1) for i in [0, 1]]
                
        visited.add(tuple(snake[-1]))

print(len(visited))
