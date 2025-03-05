def reverseVowels(s: str) -> str:
    vowels = ["a", "e", "i", "o", "u"]
    dummy = []
    s_list = list(s)

    for i, n in enumerate(s):
        if n.lower() in vowels:
            dummy.append(i)

    for j, m in enumerate(dummy):
        if j == len(dummy) // 2:
            break

        temp = s_list[int(m)] 
        # print(s[dummy[len(dummy)-j-1]])
        s_list[int(m)] = s[dummy[len(dummy)-j-1]]
        s_list[dummy[len(dummy)-j-1]] = temp

    return "".join(s_list)


str1 = "IceCreAm"
str2 = "leetcode"


print(reverseVowels(str1))
print(reverseVowels(str2))

# strtest = "abc"
# strtest_list = list(strtest)  # Convert to list
# temp = strtest_list[0]
# strtest_list[0] = strtest_list[2]  # Modify the first character
# strtest_list[2] = temp  # Modify the first character
# strtest = "".join(strtest_list)  # Convert back to string
# print(strtest)  # Output: "cbc"
