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

## Notes for the Interviewer

### Clarifying Questions

#### Q: Can words in the input list contain non-alphabetic characters?

A: You can assume all words in the input list contain only alphabetic characters.

#### Q: What should I do if invalid input is passed in?

A: You can assume that the input will be valid.

#### Q: Can a word in the input list be an empty string?

A: Yes, the input list can contain an empty string.

#### Q: Can a word in the input list be repeated?

A: No, you can assume all words in the input list will be unique.

#### Q: Should the output be ordered in any way?

A: Yes, each tuple should be ordered alphabetically. The set of tuples does not need to be ordered. Since you are returning a set, the data is expected to be unordered and will be valid as long as the correct items are in the set.

#### Q: What is an anagram?

A: Two words are anagrams of each other if the first word can be formed by reordering the letters of the second word and vice versa.

### Hints

- If your candidate struggles with an initial algorithm, encourage them to walk through an example and describe how they would do it using only pen and paper.

- If the candidate struggles to come up with an overarching algorithm, encourage them to first solve how we can determine if two words are anagrams of each other.

- If the candidate struggles with grouping anagrams together, encourage them to consider what data types might lend themselves to grouping pieces of data together. It may help them to know that they don't have to transform the input list into a set of alphabetically sorted tuples as they find the groups of anagrams. They may use some other data structure to help them sort the words into their correct groups.

## Optional Bonus At-Home Challenges

To be attempted after completing the interview.

- What is the time/space complexity of sample solution?

- If the candidate did not use a dictionary to implement their solution, encourage them to refactor their solution to use a dictionary.
