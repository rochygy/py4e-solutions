#7.2 Írj egy programot, amely kéri a fájl nevét, majd megnyitja azt, végigolvassa a fájlt, és olyan sorokat keres, amelyek a következő formátumúak:
# X-DSPAM-Confidence:    0.8475
# Számold meg ezeket a sorokat, vonj ki minden sorból a lebegőpontos értékeket, számítsd ki ezek átlagát, és állítsd elő az alábbiakban látható kimenetet. A megoldásodban ne használd a sum() függvényt, illetve a „sum” nevű változót.
# A mintaadatokat letöltheti a http://www.py4e.com/code3/mbox-short.txt weboldalról; a tesztelés során írja be az mbox-short.txt fájlnevet.
# Feladat https://www.py4e.com/tools/pythonauto/?inherit=pythonauto_07_02&_LTI_TSUGI=8d4fa522578c35475bae4fd8b4df676c
fname = input("Enter file name: ")
fh = open(fname)
total = 0
count = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    word = line.split()
    total = total + float(word[1])
    count += 1
print("Average spam confidence:", total/count)