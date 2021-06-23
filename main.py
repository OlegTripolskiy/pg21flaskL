from flask import Flask, render_template, url_for   # Из пакета flask импортируем класс Flask
import psycopg2

app = Flask(__name__)	# Создаем новое web-приложение
# app – имя переменной, в которой хранится ссылка на ЭКЗЕМПЛЯР класса Flask
# __name__ -  атрибут создаваемого экземпляра класса. Передает создаваемому экземпляру класса 
# имя модуля (пакета) в котором расположен   этот класс.
 	    # Иначе Flask не знает где искать шаблоны, статистические файлы и т.д.
@app.route("/")
def index():  #  эта функция получает статьи из БД и через переменную включает в шаблон сайта layout.html. 
#    return "Hello, world!"
    # Соединяемся с БД.
    con = psycopg2.connect(
        database="postgres", 
        user="postgres", 
        password="postgres", 
        host="127.0.0.1", 
        port="5432"
    )
    # Получаем запись из таблицы
    cur = con.cursor()
    cur.execute("SELECT article FROM articles;")
    rows = cur.fetchall()
    for row in rows:
        article = row[0]
        return render_template("layout.html", article=article)
#        return article
        
    con.close()
    
@app.route("/layout.html")
def layout(): #  эта функция вызывает шаблон сайта 
    return render_template("layout.html")

@app.route("/integrity.html")
def integrity():		#  эта функция вызывает статью "Целостность БД." и которая наследует шаблон layout.
    return render_template("integrity.html")

@app.route("/terms.html")
def terms():		#  эта функция вызывает статью "Термины при моделировании БД." и которая наследует шаблон layout.
    return render_template("terms.html")

@app.route("/highlight.html")
def highlight():
    return render_template("highlight.html")

#	return "Hello, world! "
#@app.route("/index")
# @ - декоратор - вызываем функцию (метод) route() расположенную в экземпляре app класса Flask. 
# Эта функция route()  анализирует строку браузера и, если она заканчивается на / (слэш),  
# то вызывается функция расположенная сразу под декоратором.
# Можно разместить  несколько декораторов подряд, тогда одно действие для нескольких путей.

#  Вариант запуска  flask 
if __name__ == "__main__":  #  Если вызвать этот файл из командной:  python hello.py
    app.run(debug=True)			#  То запустится  web приложение
