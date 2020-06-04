def no_dups(s):
    # Your code here
    if s == "":
        return ""
    new_str_list = s.split(" ")
    words = dict()
    for word in new_str_list:
        if word not in words:
            words[word] = 1
        else:
            words[word] += 1
    output_array = []
    for word in words:
        if words[word] == 1:
            output_array.append(word)
        output_str = (" ".join(output_array))
    return output_str

    





if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))