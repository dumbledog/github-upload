"""
For this week's exercise I want you to write a function that accepts a
sequence (a list for example) and returns a new iterable (anything you can
loop over) with adjacent duplicate values removed.

For example:

>>> compact([1, 1, 1])
[1]
>>> compact([1, 1, 2, 2, 3, 2])
[1, 2, 3, 2]
>>> compact([])
[]
"""



def compact(l):
    if not l:
        return []
    iterable = iter(l)
    out = [next(iterable)]
    for item in iterable:
        if item != out[-1]:
            out.append(item)
    return out


if __name__ == '__main__':
    print(compact([1,1,2,3,4]))