with open("input.txt", "r") as f:
    trees = [[int(t) for t in list(l.strip())] for l in f.readlines()]


def check_visibility(trees, row, col):
    tree, visible_up, visible_down, visible_left, visible_right = trees[row][col], True, True, True, True

    # Check up
    for i in range(row):
        if trees[i][col] >= tree:
            visible_up = False
            break

    # Check down
    for i in range(row + 1, len(trees)):
        if trees[i][col] >= tree:
            visible_down = False
            break

    # Check left
    for i in range(col):
        if trees[row][i] >= tree:
            visible_left = False
            break

    # Check right
    for i in range(col + 1, len(trees[0])):
        if trees[row][i] >= tree:
            visible_right = False
            break

    return visible_up or visible_down or visible_left or visible_right


def get_scenic_score(trees, row, col):
    tree, total_up, total_down, total_left, total_right = trees[row][col], 0, 0, 0, 0

    # Check up
    for i in range(row - 1, -1, -1):
        total_up += 1
        if trees[i][col] >= tree:
            break

    # Check down
    for i in range(row + 1, len(trees)):
        total_down += 1
        if trees[i][col] >= tree:
            break

    # Check left
    for i in range(col - 1, -1, -1):
        total_left += 1
        if trees[row][i] >= tree:
            break

    # Check right
    for i in range(col + 1, len(trees[0])):
        total_right += 1
        if trees[row][i] >= tree:
            break

    return total_left * total_right * total_up * total_down


visible_trees = 0
scenic_scores = []
for row in range(len(trees)):
    for col in range(len(trees[0])):
        visible_trees += check_visibility(trees, row, col)
        scenic_scores.append(get_scenic_score(trees, row, col))

print(visible_trees)
print(max(scenic_scores))
