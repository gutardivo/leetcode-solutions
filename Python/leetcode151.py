def reverseWords(s: str) -> str:
    str_list = list(s.split(" "))
    res = []

    for i in range(len(str_list)-1,-1,-1):
        if str_list[i].replace(" ","") != "":
            res.append(str_list[i])

    return " ".join(res)

str1 = "the sky is blue"
str2 = "  hello world  "
str3 = "a good   example"


print(reverseWords(str1))
print(reverseWords(str2))
print(reverseWords(str3))