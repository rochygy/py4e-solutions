##8.5 Open the file mbox-short.txt and read it line by line. When you find a line that starts with 'From ' like the following line:
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# You will parse the From line using split() and print out the second word in the line (i.e. the entire address of the person who sent the message). Then print out a count at the end.
# Hint: make sure not to include the lines that start with 'From:'. Also look at the last line of the sample output to see how to print the count.

# 8.5 Nyisd meg az mbox-short.txt fájlt, és olvasd be sorról sorra! Amikor olyan sort találsz, amely a „From ” karaktersorozattal kezdődik – mint például ez: From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008 –, a split() metódus segítségével dolgozd fel a sort, és írasd ki a második szót (vagyis az üzenetküldő teljes e-mail-címét)! Végül írasd ki a darabszámot is! Tipp: ügyelj arra, hogy a „From:” (kettősponttal végződő) kezdetű sorokat ne vedd figyelembe! A minta kimenet utolsó sorából pedig megtudhatod, hogyan kell a darabszámot megjeleníteni.
fname = r"R:\Saját meghajtó\Learn\py4e\chapter_7\mbox-short.txt"
# fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

count = 0
fh = open(fname)

for line in fh:
    wds = line.split()
    if len(wds) < 1 or wds[0] != "From":
        continue
    print(wds[1])
    count = count + 1

print("There were", count, "lines in the file with From as the first word")
