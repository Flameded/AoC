with open("input.txt", "r") as f:
    inp = [l.split() for l in f.readlines()]


def move_tail(front, back):
    if abs(front[0] - back[0]) <= 1 and abs(front[1] - back[1]) <= 1:
        return back

    for i in [0, 1]:
        back[i] += (1 if front[i] > back[i] else -1 if front[i] < back[i] else 0)
    return back


part = 2
snake = [[0, 0] for _ in range(part**3 + part)]
visited = set()

for direction, amount in inp:
    for _ in range(int(amount)):
        # Move head part
        if direction == "R":
            snake[0][0] += 1
        if direction == "L":
            snake[0][0] -= 1
        if direction == "U":
            snake[0][1] += 1
        if direction == "D":
            snake[0][1] -= 1

        # Move tail parts if necessary
        for i in range(1, len(snake)):
            snake[i] = move_tail(snake[i - 1], snake[i])

        visited.add(tuple(snake[-1]))

print(len(visited))
