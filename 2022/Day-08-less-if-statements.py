with open("input.txt", "r") as f:
    trees = [[int(t) for t in list(l.strip())] for l in f.readlines()]


def check_visibility(trees, r, c):

    visible_up = all([trees[i][c] < trees[r][c] for i in range(r)])
    visible_down = all([trees[i][c] < trees[r][c] for i in range(r + 1, len(trees))])
    visible_left = all([trees[r][i] < trees[r][c] for i in range(c)])
    visible_right = all([trees[r][i] < trees[r][c] for i in range(c + 1, len(trees[0]))])

    return visible_up or visible_down or visible_left or visible_right


def get_s_score(trees, r, c):

    directions, score = [[(0, 1), len(trees[0])-1 - c], [(0, -1), c], [(1, 0), len(trees)-1 - r], [(-1, 0), r]], 1
    for move, distance in directions:
        for i in range(1, distance):
            if trees[r + move[0]*i][c + move[1]*i] >= trees[r][c]:
                score *= i
                break
        else:
            score *= distance

    return score


print(sum([check_visibility(trees, row, col) for row in range(len(trees)) for col in range(len(trees[0]))]))
print(max([get_s_score(trees, row, col) for row in range(len(trees)) for col in range(len(trees[0]))]))
