def solution(participants, completions):
    hash_table = {}
    for participant in participants:
        hash_table[participant] = 0

    for completion in completions:
        if completion in hash_table:
            del hash_table[completion]
    return list(hash_table.keys())[0]

print(solution(['a','b','c'],['a','b']))
