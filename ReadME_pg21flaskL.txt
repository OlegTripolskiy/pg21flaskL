ПОЛЕЗНОЕ:
Дать команду локальному репозиторию не изменять окончание строки,
      чтобы не появлялось такое сообщение при команде git add .   LF will be replaced by CRLF in js/highlight.pack.js.
        проверка, что установлено, команда: git config --local core.autocrlf ,  ответ: пустая строка.
        установка запрета смены конца строки, команда : git config --local core.autocrlf false
        снова проверка, что установлено, команда : git config --local core.autocrlf,  ответ: false

--- НАЗНАЧЕНИЕ ФАЙЛОВ ПРОЕКТА  ----------
1. Корневой каталог.
  ФАЙЛЫ:
    - main.py (рабочее название) - ОСНОВНОЙ файл проекта, который принимает и обрабатывает ВСЕ запросы.
    - article_to_db.py - переписывает статью сверстанную в HTML в базу данных.
    - Pipfile       - файл виртуального окружения pipenv.
    - Pipfile.lock  - файл виртуального окружения pipenv.
    - .gitignore    - файл, содержащий перечень  папок и файлов не хранимых в архиве.
    - favicon.ico   - фавикон.
    - ReadME_pg21flaskL.txt - кратнкое описаине проекта.
  
  ПАПКИ:
    - static    - папка для хранения статических (редко изменяемых файлов)
        css   - папка с файлами css.
        js    - папка с файлами js.
    - templates - папка для хранения шаблонов
        - layout.html     - файл, в котором хранится ОСНОВНОЙ ШАБЛОН сайта.
        - index.html      - исходный (начальный) файл с которого начинался этот проект.
        СТАТЬИ
        - integrity.html  - статья "Целостность в БД." - вызывает базовый швблон layout.html
        - terms.html      - статья по теме моделирование бд "Термины".
        УЧЕБНЫЕ ФАЙЛЫ
        - base.html     - файл тренировочного базового шаблона.
        - ind.html + incl.html     - файл ind.html вызывает в себя файл incl.html.


--- РАЗВИТИЕ ПРОЕКТА --------
1. Этот проект начал 16.06.2021
2. Проект является РАЗВИТИЕМ проекта в D:\OPENSERVER\OSPanel\domains\postgres2021flask
3. Виртуализация сделана с помощью pipenv
4. 16.06.21 
    - Установил драйвер psycopg2 для работы с БД postgres.
    - Сделал добавление статьи ИЗ БД в шаблон layout.html.
6. 17.06.21  Сделал файл article_to_db.py, который КОПИРУЕТ файл в БД, заполняя строку в таблице для статей.

=== ИЗ ПРЕДЫДУШЕЙ ВЕРСИИ  postgres2021flask  ============================
3. Причина: ПЕРЕВОД разработки на Линукс на виртуальную машину DBA1.
   ИЗМЕНИЛИСЬ ПУТИ к файлам на сайте так как:
      - Статические файлы будут находится в папке static.
      - Индексный  файл будет находиться в папке templates.
   ПРИШЛОСЬ:
   Изменить имя файла шаблона на index.html
   Изменить пути к статическим файлам:
      a) В шапке файла к:
         <!--  Путь к файлам саий из шаблона Flask -->
           <link rel="stylesheet" type="text/css" href="static/css/main.css" /> 
           <link id="link_chcolor" rel="stylesheet" type="text/css" href="static/css/color_grey.css" /> 
           <link rel="icon" href="static/favicon.ico">

           <!--  ПОДКЛЮЧЕНИЕ БИБЛИОТЕКИ Highligt.JS  -->
         <!--  Путь к файлам саий из шаблона Flask -->
           <link rel="stylesheet" href="static/css/higligt_gml.css">
           <link rel="preload" href="static/static/js/highlight.pack.js" as="script">
           <script src="static/js/highlight.pack.js"></script>

      b) В скрипте добавил папку static к пути/ 
         // ==== СМЕНА ЦВЕТОВ САЙТА ===============
          $(".color_scheme tr td").click(function () {
             ...
             let colorFileNname = "static/css/" + idAttr + ".css"; // Создаем путь к файлу стилей цветов.
      c

4. 
5. Начал
