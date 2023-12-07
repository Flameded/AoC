# Day 2



## Part 1

For some reason, I had quite a bit of trouble parsing the input. I think I just forgot how to parse things. Once again, I didn't read the question properly. I tried to find the total amount of games (?) that had exactly 12 red, 13 green, and 14 blue cubes. Not sure what I was doing but it cost me a lot of time. Anyway, A relatively standard Day 2 problem - not very difficult.

Looking back at what I did, I realise that there's a couple things I could've done differently that would've greatly improved my speed (besides read the question properly). Firstly, there was no need to split the games into each group (seperated by a ;), just by games and cubes. Secondly, I could've used a dictionary to store the maximum number of cubes of each colour for each game. 
```python
cubes = {"red": 0, "green": 0, "blue": 0}
```
Since the input uses the word "red", "green", and "blue", you can just access the dictionary with that part of the input. Something like:
```python
# cube_information is like   "4 green"
cube_number, colour = cube_information.split()
cubes[colour] = max(cubes[colour], int(cube_number))
```
You then check whether each colour is in the bounds at the end of the game. 
This would've made the parsing a bit easier, and meant that I wouldn't need to have a seperate variable and if statement for each colour. Quite a lot shorter.


## Part 2

Part 1 nicely leads into part 2, basically just being a quick extension to part 1. The method above leads even nicer into the part 2, as it finds the maximum of each game.

The solution below is an implementation of the described method:
```python
with open("input.txt", "r") as f:
    inp = f.readlines()

inp = [l.split(":")[1].replace(";", ",").split(",") for l in inp]

t1 = 0
t2 = 0
for game_id, game in enumerate(inp, 1):

    cubes = {"red": 0, "green": 0, "blue": 0}
    for cube in game:
        n, colour = cube.split()
        cubes[colour] = max(cubes[colour], int(n))

    if cubes["red"] <= 12 and cubes["green"] <= 13 and cubes["blue"] <= 14:
        t1 += game_id

    t2 += cubes["red"] * cubes["green"] * cubes["blue"]

print(t1)
print(t2)
```


## Thoughts
Quite a standard Day 2 problem. 

**Difficulty: 2/10**

Overall Day 2 part 1 did not go great for me, taking 17 minutes, but I did part 2 relatively quickly and finished both parts in under 20 minutes. Definitely not my greatest performance. Sacrificing a few seconds to read the problem is probably a good idea.

**Tip of the day**: Read the question (again)

**Python tip of the day**: You can start enumerating from a specified index! `enumerate(iterable, 3)` starts enumerating at 3 instead of 0.
