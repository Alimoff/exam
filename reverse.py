def reversed_sentence(text):
    a = text.split(" ")
    a.reverse()

    string = ""

    for i in a:
        string += i + " "

    return string
