# Day 1

I would like to go back to counting calories :(

## Part 1

Part 1 felt relatively appropriate for a part 1 of a Day 1. Very straightfoward. Not much to say.

## Part 2
Part 2 is undeniable, unequivocal, undisputable proof that numbers > words. I think most people were thrown off with the sudden difficulty, since historically Day 1 is quite free. 

Unfortunately, I didn't read the question before starting my solution for part 2. This is not a great idea. I started making a program that finds the first and last number, rather than just the first and last digit like in part 1. No clue why I did this. After submitting the answer and realising that I had not done the question, I started on a solution to the actual question, now losing a couple minutes.

I did the replace method, which obviously lead to the infamous overlap problem. Luckily I had this idea quite quicky: 
```python
s = s.replace("one", "one1one")
```
- I did forget how `.replace()` works and just did `s.replace("one", "one1one1)` and wondered why my code returned the same answer

I personally didn't do `s = s.replace("one", "o1e")` as it wouldn't be effective against multiple overlapping letters. Although, for part 2 it would have worked (too much thinking needed to verify - we don't do that).

## Thoughts
Strangely difficult problem for day 1. 

**Difficulty: 4/10**

Overall I did quite well, completing part 1 in a bit over 2 minutes, and both in a bit over 7 minutes (unfortunately missing global by about 20 seconds each), but definitely could've done much better.

**Tip of the day**: Read the question

**(Python) tip of the day**: Make sure you know which methods return something, and which ones that acts directly on it. Also strings are immutable.
