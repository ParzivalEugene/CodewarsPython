def encrypt_this(text):
    def encrypt(word):
        if len(word) == 1:
            return str(ord(word[0]))
        elif len(word) == 2:
            return str(ord(word[0])) + word[-1]
        return str(ord(word[0])) + word[-1] + word[2:-1] + word[1]

    return " ".join([encrypt(i) for i in text.split()])


print(encrypt_this("A wise old owl lived in an oak"))
