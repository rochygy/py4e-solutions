# 8.4 Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split() method. The program should build a list of words. For each word on each line check to see if the word is already in the list and if not append it to the list. When the program completes, sort and print the resulting words in python sort() order as shown in the desired output.

# Nyisd meg a romeo.txt fájlt és olvasd be soronként. Minden sorban a split() metódussal bontsd a sort szavak listájára. A programnak szavak listáját kell létrehoznia. Minden egyes szónál ellenőrizd, hogy a szó már szerepel-e a listában, és ha nem, fűzd hozzá a listához. Amikor a program befejeződött, rendezd és nyomtasd ki a kapott szavakat python sort() sorrendben, a kívánt kimenetben látható módon.
fname = input("Enter file name: ")
fname = open(r'R:\Saját meghajtó\Learn\py4e\chapter_8\romeo.txt')

lst = list()
for line in fname:
    line = line.rstrip()
    wds = line.split()

    for word in wds:
        if word in lst:
            continue
        lst.append(word)

lst.sort()
print(lst)