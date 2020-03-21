Jawaban Nomer 1
def biodataku():
    import json
    
    x={
        "name":"Novani Indra Kustanti",
        "age":24,
        "adress":"JL. Pemuda Gang I/16",
        "hobbies":("Sports","Singing","design"),
        "is_married":False,
        "list_school":("Institut Teknologi Sepuluh Nopember","2014","2018","Mathematics"),
        "skill":("HTML","CSS","QGIS","ARCMAP","Beginner"),
        "interest_in_coding":True
    }
    y=json.dumps(x)
    return y
biodataku()
