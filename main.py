from collections import defaultdict

def grouped(strings):
    # create an empty dictionary where keys will be a group of letters
    # and values will be words that are an anagram of that group of letters.
    # defaultdict is purely a convenience to avoid needing to handle adding
    # the first word for a key and any other words for that key differently.
    anagrams_dict = defaultdict(list)

    # loop through words in strings
    for word in strings:
        # create a list of characters making up word
        word_as_list = [char for char in word]
        # sort the list of characters
        word_as_list.sort()
        # create the key by casting the list of characters to a tuple
        key = tuple(word_as_list)

        # add the word to list of words that are an anagram of the key
        anagrams_dict[key].append(word)

    # create an empty set to store result
    answer = set()

    # loop through key-value pairs in dictionary
    for key, value in anagrams_dict.items():
        # sort the group of anagrams
        sorted_val = sorted(value)
        # convert group of anagrams to a tuple and add to set
        answer.add(tuple(sorted_val))

    # return the set
    return answer


lst = ["eat", "tea", "tan", "ate", "nat", "bat"]
answer_1 = set([("ate", "eat", "tea"), ("bat",), ("nat", "tan")])
assert grouped(lst) == answer_1

lst = ["bored", "players", "sadder", "dreads", "robed", "parsley"]
answer_2 = set([("bored", "robed"), ("parsley", "players"),
                ("dreads", "sadder")])
assert grouped(lst) == answer_2

lst = ["eat", "tae", "tea", "eta", "aet", "ate"]
answer_3 = set([("aet", "ate", "eat", "eta", "tae", "tea")])
assert grouped(lst) == answer_3

lst = ["eat", "ear", "tar", "pop", "pan", "pap"]
answer_4 = set([("eat",), ("ear",), ("tar",), ("pop",), ("pan",),
                ("pap",)])
assert grouped(lst) == answer_4

lst = []
answer_5 = set()
assert grouped(lst) == answer_5

print("All tests passed!")
print("Discuss time & space complexity if time remains.")
