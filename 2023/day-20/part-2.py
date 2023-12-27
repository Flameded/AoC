from collections import deque
from math import lcm

with open("input.txt", "r") as f:
    inp = f.readlines()

inp = [l.strip("\n") for l in inp]

adj_list, types = {}, {}
for fr, to in [signal.split(" -> ") for signal in inp]:
    typ = fr[0]
    module = fr if typ == "b" else fr[1:]
    adj_list[module] = to.split(", ")
    types[module] = typ

memory = {}
for fr, to in adj_list.items():
    if "rx" in to:
        final_module = fr

    for adj in to:
        if adj not in types:
            continue

        if types[adj] == "&":
            if adj not in memory:
                memory[adj] = {}
            memory[adj][fr] = 0
        elif types[adj] == "%":
            memory[adj] = 0

done = {}
i = 0
while True:
    i += 1

    q = deque([("button", "broadcaster", 0)])
    while q:
        coming_from, module, pulse = q.popleft()

        # &pm, &mk, &pk, &vf  --> &vf --> rx
        if module == final_module:
            for input_module, input_pulse in memory[module].items():
                if input_pulse == 1 and input_module not in done:
                    done[input_module] = i
            if len(done.values()) == len(memory[module]):
                print(lcm(*done.values()))
                exit()

        if module not in types:
            continue
        typ = types[module]

        next_pulse = 0
        if typ == "b":
            next_pulse = pulse
        elif typ == "%" and pulse == 0:
            memory[module] = 1 - memory[module]
            next_pulse = memory[module]
        elif typ == "&":
            memory[module][coming_from] = pulse
            next_pulse = 1 - all(memory[module].values())
        else:
            continue

        q += [(module, adj, next_pulse) for adj in adj_list[module]]
