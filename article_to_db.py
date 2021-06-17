import psycopg2

with open("/home/student/pg21flaskL/templates/terms1.html") as file:
    text_file = file.read()
    print(text_file)
    
    # Соединяемся с БД.
    con = psycopg2.connect(
        database="postgres", 
        user="postgres", 
        password="postgres", 
        host="127.0.0.1", 
        port="5432"
    )
    # Записываем содержимое файла в таблицу.
    cur = con.cursor()
#    cur.execute("INSERT INTO articles VALUES ({}, {}});")
    cur.execute('''INSERT INTO articles (id, article) VALUES(%s,%s)''', (1, text_file))
    
    con.commit()
    con.close()