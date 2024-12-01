# 🎄❄️ Advent of Code 2024 - Day 1 🎄❄️

Below are my atempts for the first day of the advent of code [2024 Day 1](https://adventofcode.com/2024/day/1)

## Part one

To get the result, run the following:

```terminal
python part_one.py

Result: 1258579
```

For the first part, I developed two approaches:

### Solution 1 - Tree sort

This approach uses a [tree sort](https://en.wikipedia.org/wiki/Tree_sort), by using two trees to store both lists of values:
    - Create two Binary Search Trees and insert the values
    - Traverse in order both trees, `zip` the values and compute the difference

### Solution 2 - List sort

This approach uses a naive approach of loading both lists of values in separate `list`, sorts them separately and `zip` the values.

  1) Load all the left values into a `list`
  2) Load all the right values into a `list`
  3) Sort both lists (`list.sort()`)
  4) `zip` both lists and compute the difference

## Part two

To get the results, run the following:

```terminal
python part_two.py

Result: 23981443
```

For this part, I developed one approach only.

It loads the data and stores the left values in a `list`, and right values in a `dict` that contains the frequency of that value on the right list.

  1) Yield the data from the file and store both values in different structures:
        - Left: Load all the left values into a `list`
        - Right: Load all the right values into a frequency `dict`
  2) Iterate over the left values and multiply by the known frequency in the right dictionary
  3) Return the sum of the multiplications
  
## Performance

Time the solutions by executing `times.py`:

```terminal
$ python times.py

---- Part 1 ----

List sort approach took 0.0007233750075101852 seconds
Tree sort approach took 0.003182541986461729 seconds

---- Part 2 ----

Similarity score approach took 0.0005920830299146473 seconds
```