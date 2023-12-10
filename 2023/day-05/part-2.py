with open("input.txt", "r") as f:
    inp = [x.split("\n") for x in f.read().split("\n\n")]


nums = [int(x) for x in inp[0][0][6:].split()]
ranges = []
for i in range(len(nums) // 2):
    x, y = nums[2*i], nums[2*i+1]
    ranges += [(x, x + y)]


for mapping_info in inp[1:]:

    finished_ranges = []
    for line in mapping_info[1:]:
        destination_start, source_start, amount = [int(x) for x in line.split()]
        source_end = source_start + amount
        to_add = destination_start - source_start

        new_ranges = []
        for lo, hi in ranges:

            ordered_nums = sorted([lo, hi, source_start, source_end])

            lo1 = ordered_nums[0]
            hi1 = ordered_nums[1]
            lo2 = ordered_nums[1]
            hi2 = ordered_nums[2]
            lo3 = ordered_nums[2]
            hi3 = ordered_nums[3]

            all_3_ranges = [(lo1, hi1), (lo2, hi2), (lo3, hi3)]

            for xlo, xhi in all_3_ranges:

                # Get rid of the ones we do not care about (anything outside of the original range or not a valid range)
                if xlo < lo or xhi > hi or xlo == xhi:
                    continue

                if source_start <= xlo and xhi <= source_end:
                    # Mapped ranges no longer need to be checked
                    finished_ranges += [(xlo + to_add, xhi + to_add)]
                else:
                    new_ranges += [(xlo, xhi)]
        ranges = list(new_ranges)

    ranges += finished_ranges

print(f"Part 2: {min(min(x1, x2) for x1, x2 in ranges)}")
