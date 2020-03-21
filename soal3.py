# ArkademyBatch16K1
Repository ini digunakan untuk tes bootcamp arkademy
Jawaban Nomer 3

def triangle(x):
    a=""
    b=1
    while b<=x:
        c=b
        while c>0:
            a=a+"#"
            c=c-1
        a=a+"\n"
        b=b+1
    print(a)
triangle(5)
