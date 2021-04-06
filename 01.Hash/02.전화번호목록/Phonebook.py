def solution(phone_book):
    hash_table = {}
    for number in phone_book:
       hash_table[number] = 1

    for number in phone_book:
        temp = ""
        for n in number:
            temp += n
            if temp in hash_table and temp != number:
                return False
    return True
    


print(solution(["119","245","11922"]))
print(solution(["4732","245","11922"]))



