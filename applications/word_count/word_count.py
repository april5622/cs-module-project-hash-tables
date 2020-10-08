def word_count(s):
    wordCount = {}

    bannedCharacters = {":": None, ";": None, ",": None, ".": None, "-": None, "+": None,  "=": None, "/": None, "\\": None,  "\"": None,  "|": None, "[": None, "]": None, "{": None, "}": None,  "(": None, ")": None, "*": None, "^": None, "&": None}
    
    s = s.lower().strip()

    for letter in s:
        if letter in bannedCharacters:
            s = s.replace(letter, '')
    s = s.split()

    for word in s:
        if word not in wordCount:
            wordCount[word] = 1
        else:
            wordCount[word] += 1
    return wordCount



if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))