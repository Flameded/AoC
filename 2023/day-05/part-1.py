with open("input.txt", "r") as f:
    inp = [x.split("\n") for x in f.read().split("\n\n")]

seeds = [int(x) for x in inp[0][0][6:].split()]

for mapping_info in inp[1:]:

    finished_seeds = []
    for line in mapping_info[1:]:
        destination_start, source_start, amount = [int(x) for x in line.split()]
        source_end = source_start + amount
        to_add = destination_start - source_start

        new_seeds = []
        for seed in seeds:
            if source_start <= seed < source_end:
                # Mapped seeds no longer need to be checked
                finished_seeds += [seed + to_add]
            else:
                new_seeds += [seed]
        seeds = list(new_seeds)

    seeds += finished_seeds

print(f"Part 1: {min(seeds)}")
