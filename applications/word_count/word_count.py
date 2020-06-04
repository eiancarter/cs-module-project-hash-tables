def word_count(s):
    # Your code here
    # s.split(' ')
    new_str_list = s.split(' ')
    print(new_str_list)
    counts = dict()
    for str in new_str_list:
        if str not in counts:
            counts[str] = 1
        else:
            counts[str] += 1
    return counts




if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))