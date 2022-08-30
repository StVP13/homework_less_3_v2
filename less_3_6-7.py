def int_func():
    for word in input('введите слово малыми латинскими буквами:\n').split():
        chars = 0
        for char in word:
            if 97 <= ord(char) <= 122:
                chars += 1
    print(word.title() if chars == len(word) else f'{word} - только прописные английские буквы!')

int_func()
