from collections import defaultdict

# def grouped(words):
#     word_dict_list = list()
#     for word in words:
#         word_dict = defaultdict(int)

#         for char in word:
#             word_dict[char] += 1

#         word_dict_list.append(word_dict)

#     seen = set()
#     result = set()

#     for i in range(len(words)):
#         if i in seen:
#             continue

#         group = [words[i]]
#         seen.add(i)

#         for j in range(i+1, len(words)):
#             if word_dict_list[i] == word_dict_list[j]:
#                 group.append(words[j])
#                 seen.add(j)
        
#         result.add(tuple(sorted(group)))

#     return result

# ************** refactored ******************
# For Grouping use a dictionary with defaultdict(list)

def grouped(words):
    groups = defaultdict(list)

    for word in words:
        key = tuple(sorted(word))  # anagram key (Learn how to use tuple as key)
        groups[key].append(word) 

    # print(groups)

    # Convert to set of sorted tuples for uniqueness and hashability
    result = set()
    for group in groups.values():
        result.add(tuple(sorted(group)))
        
    # result = {tuple(sorted(group)) for group in groups.values()}

    return result


lst = ["eat", "tea", "tan", "ate", "nat", "bat"]
answer_1 = set([("ate", "eat", "tea"), ("bat",), ("nat", "tan")])
print(grouped(lst))
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
