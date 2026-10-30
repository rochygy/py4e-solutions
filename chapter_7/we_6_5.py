# 6.5 Írj kódot a find() függvénnyel és karakterlánc-szeleteléssel (lásd 6.10. szakasz), hogy kinyerd az alábbi sor végén található számot. Alakítsd át a kinyert értéket lebegőpontos számmá, és nyomtasd ki.
#Feladat: https://www.py4e.com/tools/pythonauto/?inherit=pythonauto_06_05&_LTI_TSUGI=018aef08d218023dcddf065299701142
text = "X-DSPAM-Confidence:    0.8475"
atpos = text.find(':')
bpos = text.find('5')
gypos = text.find('0')
finalstring = text[gypos : bpos+1]
finalfloat = float(finalstring)
print(finalfloat)