$("document").ready(function () {
    "use strict"; // Директива ECMAScript 5, ставим в начале сценария или функции
    // --- Начало. Преобразовываем код HTML в спецпоследовательности. --------
    $('#do').click(function() {
        // Создаю объект с парой ключ значение
        let symbols = {
            '<': '&lt;',
            '>': '&gt;',
            '"': '&quot;'
        };
        // получаю весь код, введенный в textarea.
        let str = $('#codeHTML').val();
        // Перебираем объект, получая символ и спецпоследовательность для замены.
        for (let key in symbols) {
            let reg = new RegExp("" + key + "", "g");  // Создаем регкулярное выражение с переменной.
            str = str.replace(reg, symbols[key]);  // Изменияем значения в коде.
        }
        console.log(str); // Получаем новую строку
        $('#code').val(str);
    });// --- Конец. Преобразовываем код HTML в спецпоследовательности.
      //
      // --- Копирование текста кода в хайлайтере в буфер обмена.
      // ВНИМАНИЕ: д.б. выдержана структура хайлайтеара.
      //           метод execCommand('copy') считается устаревшим, но взамен  пока  ничего  нет.
    $('.highlight-code').click(function () {
        let text = $(this).children().next().children();  // Получаем тэг <code>, путь: div-div-pre-code
        let $tmp = $("<textarea>"); // Создаем элемент textarea, который поддерживает переносы.
        $("body").append($tmp);  // Добвляем этот созданный элемент к странице.
        $tmp.val(text.text()).select(); // Записываем в него содержимое элемента и выделяем его.
        document.execCommand("copy");
        $tmp.remove();
    });
}); // -- Конец $("document").ready(function ()