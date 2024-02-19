def ReverseWord(w):
    str2 = w.split()
    str2 = str2[::-1]
    str2 = " ".join(str2)
    return str2
# return " ".join(w.split()[::-1])
w = input("Give Long String: ")
print(ReverseWord(w))
