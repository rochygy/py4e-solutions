# 5.2 Írj egy programot, amely ismételten egész számokat kér a felhasználótól, amíg a felhasználó be nem írja, hogy „done”. Miután a „done” beírásra került, nyomtassa ki a számok legnagyobb és legkisebb értékét. Ha a felhasználó nem érvényes számot ír be, akkor azt egy try/except paranccsal kapd el, majd egy megfelelő üzenetet jeleníts meg és hagyd figyelmen kívül a számot. Írj be 7-et, 2-t, bob-t, 10-et és 4-et, és párosítsd az alábbi kimenetet.
# Feladat: https://www.py4e.com/tools/pythonauto/?inherit=pythonauto_05_02&_LTI_TSUGI=d5423d97c38105462f5fc906cc7d1f3a
smallest = None
largest = None
while True:
    sval = input('Enter a number:' )
    if sval == 'done':
        break
    try:
        ival = int(sval)
    except: 
        print('Invalid input')
        continue
    if largest is None or ival > largest:
        largest = ival
    if smallest is None or ival < smallest:              
        smallest = ival
#print(tot, num, tot/num)
print('Maximum is', largest)
print('Minimum is', smallest)