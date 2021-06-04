word = 'ffkdasnndlfmlngnkjnflvnkfjnvathamvlfmcaulgnfllkfnkjvnfldcaunvfdlvacauthamlvfcaumlbmflnblfdlvnfdkbnathafnlvnflvmldfnbnfdlatha'
word_1 = 'nsdnldsjfnkadnvldflvfdcauvnfnvnfdslmvlncaufdskvnlfdnbnfdlblcauvlfvnfldmvlmfdvnjfdnvlcau vlknflvnfskldmvlfcauvfnkjvnkjdfnkvjf'


def method1(word):
    count = 0
    try:
        for i in range(len(word)):
            if word[i] == 'a':
                if word[i + 1] == 't':
                    if word[i + 2] == 'h':
                        if word[i + 3] == 'a':
                            count += 1

    except IndexError:
        pass
    print(count)


def method2(word, search_word):
    count = 0
    sw_len = len(search_word)
    try:
        for i in range(len(word)):
            if word[i:i + sw_len] == search_word:
                count += 1

    except IndexError:
        pass

    print(count)


method2(word, 'cau')
method2(word_1, 'cau')


def no_dupe(string):
    a = {}
    for char in string:
        if char in a:
            return False
        else:
            a[char] = 1
    return True


print(no_dupe('aaaaaa'))
print(no_dupe('abcdefg'))
print(no_dupe(''))
print(no_dupe('abcdefghijklmnopqrstuvwxyzz'))
print(no_dupe('abcdefghijklmnopqrstuvwxyz'))
