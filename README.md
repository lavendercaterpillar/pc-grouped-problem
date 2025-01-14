# Grouped Problem

Problem belonging to the post-classroom Mock Interview Question Repository.

## Problem Statement

We are interested in writing a function that takes a given list of words and groups anagrams together.

Our function should accept one argument, a list of strings.

We will store our groups of anagrams as a set of sorted tuples.

For example:
Input:

```py
["eat", "tea", "tan", "ate", "nat", "bat"]
```

Output:

```py
{
    ("ate", "eat", "tea"),
    ("nat", "tan"),
    ("bat",)
}
```

Because `"eat"`, `"tea"`, and `"ate"` are anagrams of each other, they should be grouped in alphabetic order as the tuple `("ate", "eat", "tea")`.

Similarly, the words `"tan"` and `"nat"` should be grouped together as `("nat", "tan")`.

Finally `"bat"` is not an anagram of any other word in the list, so it should remain by itself as `("bat",)`.

Note that each word in the list will be unique.

## Examples

### Example 1

```py
lst = ["eat", "tea", "tan", "ate", "nat", "bat"]
grouped(lst)
```

Produces

```py
{
    ("ate", "eat", "tea"),
    ("bat",),
    ("nat", "tan")
}
```

### Example 2

```py
lst = ["bored", "players", "sadder", "dreads", "robed", "parsley"]
grouped(lst)
```

Produces

```py
{
    ("bored", "robed"),
    ("parsley", "players"),
    ("dreads", "sadder")
}
```

### Example 3

```py
lst = ["eat", "tae", "tea", "eta", "aet", "ate"]
grouped(lst)
```

Produces

```py
{
    ("aet", "ate", "eat", "eta", "tae", "tea")
}
```

### Example 4

```py
lst = ["eat", "ear", "tar", "pop", "pan", "pap"]
grouped(lst)
```

Produces

```py
{
    ("eat",),
    ("ear",),
    ("tar",),
    ("pop",),
    ("pan",),
    ("pap",)
}
```

### Example 5

```py
lst = []
grouped(lst)
```

Produces

```py
set()  # recall that {} would be an empty dict, not a set
```
