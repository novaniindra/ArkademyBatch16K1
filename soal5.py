JAWABAN NOMER 5
==================================================
def groupNumber():
    import numpy as np
    symbols = " -"
    sentence = "993141 -1 1323 14-232"
    for i in symbols:
        #print(sentence)
        sentence = np.char.replace(sentence, i, '')
    print(sentence)
    angka=[0]
    while angka>=50:
        if (angka%3)==0:
            angka=sentence
        print(sentence)
groupNumber()
===================================================
