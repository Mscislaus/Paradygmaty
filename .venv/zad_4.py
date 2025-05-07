def checkPalindrom(txt):
    txt = txt.lower().replace(" ", "")
    return txt == txt[::-1]

print(checkPalindrom("kajak"))
print(checkPalindrom("A to kawa kawa to a"))
print(checkPalindrom("Python"))
