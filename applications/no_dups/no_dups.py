def no_dups(s):
    nodupsList = []
    seen = set()
    for word in s.split():
        if word not in seen:
            nodupsList.append(word)
            seen.add(word)
    return ' '.join(nodupsList)   




if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))