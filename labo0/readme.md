 # Лабороторная работа №0
 
 ## Задание
+ **Требовалось:**
    1. Создать репозиторий на Github.
    2. Склонировать его себе на ПК.
    3. Написать свою первую программу.
    4. Скомпилировать и запустить ее.
    5. Получить по отдельности результаты кажого этапа компиляции.
    6. Написать отсчет в "readme.md" содержащий:
        + Задание
        + Описание проделанной работы
        + Консольные команды
        + Скриншоты результатов
        + Ссылки на используемые материалы
    7. Сделать коммит и пуш.
    8. Добавить отчет в шпараглку по работе с ``git``.
 
 
 ## Шпаргалка git'а
 + Что нужно сделать перед началом работы:
 1. Создать репозиторий на git hub'е.
 2. Создать файл на компьютере, ВАЖНО: имя файла должно совпадать с названием репозитория.
 3. Создать внутренний репозиторий. Для этого нужно:
    + Нажать правой кнопкой мышки в файле
    + Открыть терминал в этой папке
    + Написать в терминале команду ``git init``
4. Создать тектовый файл "readme.md"
5. Открыть файл "readme.md" с помощью "VSCodium"
6. Добавить в отслеживание созданный файл с помощью команды ``git add (имя файла)`` или ``git add .`` (добавляет все файлы к отслеживнаию)
7. Зафиксировать изменения с помощью команды ``git commit (также можно написать -m "name commit")``
8. Создать ветку с помощью команды ``git branch -M (имя ветки, обычно main или master)``
9. Подключить наш репозиторий к репозиторию на сайте github с помощью команды ``git remote add origin (сылка на репозиторий с github'a)``
    + Можно проверить подключилось или нет с помощью команды ``git remote -v``
10. Отправляем нашу ветку на github с помощью команды ``git push -u origin main``

+ Последющие сохарнение изменений на github:
1. После внесения изменений пишем команду ``git add (имя файла)`` или ``git add .`` (для сохранения сразу всех файлов) 
2. Фиксируем изменения с помощью команды ``git commit -m`` (в "" можно написать название фиксации)
3. Отправляем изменения на gitgub с помощью команды ``git push``

+ Работа со своим репозиторием с другого устройства:
1. На новом устрйостве используем команду ``git clone (сылка на репозиторий)``



## Описание проделанной работы
1. В начале мы создали репозиторий на Github.
2. Создали папку лабортаорной работы на компьютере (название свопадает с названием репозитория на Github)
+ **Описанные далее дейсвтия просходили в папке лабортароной работы**
3. Создали из папки репозиторий с помощью команды в терминале ``git init``
4. Создали текстовый файл отсчета **reafme.md**
5. Создали файл **hello.c** и написали первую программу
6. В терминале **"VSCodium"** написали команду ``git add .`` и тем самым добавили к отслеживанию все файлы внутреннего репозитория.
7. Зафиксировали изменения с помощью команды ``git commit -m "имя коммита"``
8. Создали ветку командой ``git branch -M main``
9. Подключили наш репозиторий к Github, командой ``git remote add origin (ссылка на репозиторий)``
10. Отправили нашу ветку на Github, командой ``git push -u origin main``
11. Напсиали отсчет и отправили его на Github командами: ``git add .`` => ``git commit "имя комита"`` => ``git push``


## Консольные команды
Во время лабороторной работы мы посмотрели некоторые консольные команды, такие как:
1. ``pwd`` - ваше местонохаждение (папка в котром вы находитесь)
2. ``ls`` - ваше местонохождение без пути (файл в котром вы находитесь)
3. ``ls -l`` - количество файлов в папке в котрой вы находитесь 
4. ``man ls`` - инстуркция команды ``ls``
5. ``ls -a`` - все файлы (считая скрытые)
6. ``cd (аргумент)`` - перемещние по папкам в терминале (без аргумента переносит в самое начало)
7. ``mkdir (имя папки)`` - создает папку в той папке в которой вы находитесь
8. ``rm -r (имя папки)`` - удаляет папку



## Инстуркция по использованию 
1. В терминалие **VSC** напсиать команду ``./hellow``
2. В случае если не работает написать команды ``gcc hello.c`` => ``./a.out``



## Используемые материалы
1. https://doka.guide/tools/markdown/