python_10_8
"""
https://www.youtube.com/watch?v=dnCooWIYbTg
https://github.com/qa-guru/qa_guru_python_7_8
https://github.com/qa-guru/knowledge-base

~~~~~~~~~~
Тестируем классы интернет-магазина
Вам нужно реализовать и протестировать классы интернет-магазина. Все места, которые нужно дописать как в тестах, так и классах, отмечены # TODO.
При реализации обращайте внимание на типизацию аргументов методов и возвращаемых значений. Так же обратите внимание на организацию тестов в файле с тестами:
– Тесты сгруппированы по классу, который они тестируют.
– Каждый тест называется именем соответствующего ему метода.
Вы можете начать как с реализации классов, так и с тестов.
Дополнительные вопросы:
– С чего проще начать выполнение домашнего задания: с тестов или с реализации классов?
– Почему для хранения товаров в корзине используется словарь, а не список?
– Зачем нужен hash в классе Product? Изучите этот метод и объясните, почему он нужен.
"""

python_10_9
"""
https://www.youtube.com/watch?v=wzwMwGd3weU
https://github.com/qa-guru/qa_guru_python_1_7

ИНСТРУКЦИЯ ПО УСТАНОВКЕ ALLURE


Устанавливаем Аллюр с помощью инсталлятора как в лекции.

Если по каким-то причинам аллюр не удаётся установить с помощью инсталлятора, тогда действуем так:



Как приготовить Аллюр по быстрому:

1. Если не установлена Java - установить

2. Отсюда https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/

забираем последнюю версию (или какая тебе нужна)

допустим это 2.20.1:

здесь https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/2.20.1/

качаем архив allure-commandline-2.20.1.zip

3. Разархивируем в корень проекта, получаем папку allure-2.20.1

4. Переименовываем для удобства папку allure-2.20.1 в allure

Аллюр по быстрому готов, теперь запускать отчет можно из корня проекта командой (если папка с результатами в allure-result и она в корне проекта):

Mac: allure/bin/allure serve

Win: allure/bin/allure.bat serve


Вариант чуть сложнее, но один раз сделал, и будет работать всегда (начиная с п.3 примерно так делают установщики аллюра):


1. как п.1 в аллюр по быстрому

2. как п.2 в аллюр по быстрому

3. разархивируем куда тебе удобно

4. прописываем в переменную окружения PATH полный путь до папки allure/bin/ в которой лежат исполняемые файлы allure для Mac и allure.bat для Win

Например путь для Mac: /Users/User_name/PythonProject/tests_demoqa/allure/bin

Теперь запускать отчет можно из корня проекта командой (если папка с результатами в allure-result и она в корне проекта):

Mac: allure serve

Win: allure.bat serve


Аттеншн:

1. Если ты креативен, и папка с результатами называется не allure-results, то после serve надо указать имя этой папки

2. В случае, если папка с результатами формируется не в корне проекта, то в конфгурации запуска надо поправить working directory - указать корневую папку проекта, это исправит ситуацию

3. Параметры запуска:

--alluredir=allure-results - указывает аллюру имя папки куда записывать результаты

--clean-alluredir - указывает аллюру, что при запуске надо удалить содержимое папки alluredir (удалить результаты предыдущего запуска, обычно полезно при разработке и отладке, чтобы не было мусора)

4. В корне проекта можно создать файл pytest.ini следующего содержания:

[pytest]

addopts =

    --clean-alluredir

    --alluredir=allure-results

в таком случае, параметры запуска будут браться из этого файла, и указывать отдельно в команде запуска эти параметры будет не нужно 

5. Папку  с аллюром allure (если она лежит в проекте) и папку с результатами allure-results (или твое имя папки, если ты задавал другое) надо добавить в .gitignore, эти папки не должны попасть в репозиторий

дока https://docs.qameta.io/allure-report/#_installing_a_commandline

п 2.1.4. Manual installation

~~~~~~~~~

Написать тест на проверку названия Issue в репозитории через Web-интерфейс.
Этот тест представить в трех вариантах:

1. Чистый Selene (без шагов)

2. Лямбда шаги через with allure.step

3. Шаги с декоратором @allure.step

4. Разметку тестов всеми аннотациями

В качестве ответа на задание приложите ссылку на свой репозиторий GitHub в поле ответа
"""

python_10_10

"""
Урок // https://www.youtube.com/watch?v=8iWqsZmihKk
Репо // https://github.com/yashaka/demoqa-tests/tree/py-04-lesson-po-practice-form-task-final

О синтаксисе классов в Python: «Инструментарий для работы с классами в Python» // https://www.youtube.com/watch?v=tfaFMfulY1M

Мартин Фаулер о PageObject // https://martinfowler.com/bliki/PageObject.html

Рекомендации и общепринятые договоренности в подборе имен (Python) // https://autotest.how/sdet-start-ru

Примеры тестов разного стиля с и без применения PageObject // https://github.com/yashaka/python-web-test/blob/master/tests/test_search_engines_should_search.py

Примеры более сложных PageObject-ов для контролов и тестов с ними // https://github.com/automician/snippets/tree/master/python/python-selene-for-odoo-crm-examples/framework/model/controls
https://github.com/automician/snippets/blob/master/python/python-selene-for-odoo-crm-examples/tests/test_examples.py

~~~~~~~~~~~~~~~~
ровести рефакторинг своего теста на регистрацию студента по форме https://demoqa.com/automation-practice-form, используя инструменты объектно-ориентированной парадигмы для инкапсуляции деталей реализации бизнес-шагов пользователя, таким образом реализовав идеи шаблона PageObject.

Задание состоит из нескольких частей, каждую из которых следует сдавать в виде отдельной ссылки на соответствующую бренчу в репозитории с тестами на приложение demoqa (все ссылки в одном сообщении в комментариях ниже).



ЧАСТЬ I (реализовать в бренче mid-level-step-objects)

В этой части мы рассматриваем как ценный c точки зрения бизнеса шаг пользователя – «заполнение отдельных данных о пользователе» или «подтверждение результата проделанной работы» (как например, подтверждение что регистрация прошла успешно).

Финальный тест должен иметь структуру вида:

registration_page.open()
registration_page.fill_first_name('Yasha')
registration_page.fill_last_name('Kramarenko')
...
registration_page.submit()
registration_page.should_have_registered(yasha)
... или использовав идеи шаблона Fluent PageObject:
registration_page.open()
registration_page \
    .fill_first_name('Yasha') \
    .fill_last_name('Kramarenko') \
    .fill_email('yashaka@gmail.com') \
    ... \
    .submit()
registration_page.should_have_registered('Yasha Kramarenko', 'yashaka@gmail.com', ...)
... или использовав форматирование через круглые скобки вместо \


registration_page.open()
(  
    registration_page
    .fill_first_name('Yasha')
    .fill_last_name('Kramarenko')
    .fill_email('yashaka@gmail.com')
    ...
    .submit()
)
registration_page.should_have_registered('Yasha Kramarenko', 'yashaka@gmail.com', ...)
Другие варианты реализации проверки:

registration_page.should_have_registered(
    student_name='Yasha Kramarenko', 
    student_email='yashaka@gmail.com',
    ...
)
registration_page.should_have_registered(
    ('Student Name', 'Yasha Kramarenko'), 
    ('Student Email', 'yashaka@gmail.com'), 
    ...
)


Дополнительные условия и подсказки:

* Все элементы выносить в отдельные поля объекта класса не обязательно, но стоит это сделать с теми элементами, которые будут повторяться.

* Класс для PageObject должен лежать в выделенном модуле в выделенном пакете внутри проекта, как было показано на уроке 😉



ЧАСТЬ II (реализовать в бренче high-level-step-objects)

В этой части мы рассматриваем как ценный c точки зрения бизнеса шаг пользователя – «отправить форму с данными» или другими словами «провести регистрацию через форму». Также шагом считаем подтверждение результата проделанной работы (как например, подтверждение, что регистрация прошла успешно).



Также в этой части следует провести рефакторинг работы с данными пользователя, представив их в виде объекта датакласса, используя уже имеющиеся знания из предыдущих уроков.



Финальный тест должен выглядеть примерно так:

yasha = User(first_name='yasha', last_name='kramarenko', email='yashaka@gmail.com', ...)
registration_page.open()
registration_page.register(yasha)
registration_page.should_have_registered(yasha)
Допустимо реализовать шаг вида:


registration_page.fill(yasha).submit()
Допустимо предопределить пользователя для тестов в отдельном модуле users.py и в тесте либо использовать напрямую:
registration_page.open()
registration_page.register(users.student)
registration_page.should_have_registered(users.student)
... либо через переменную:

student = users.student
registration_page.open()
registration_page.register(student)
registration_page.should_have_registered(student)


Дополнительные условия и подсказки:

* Не обязательно на уровне с высокоуровневыми шагами типа .register(user) добавлять в PageObject средне-уровневые шаги типа .fill_email(user.email), но можно

  * если их добавлять – это будет сделать не сложно, просто скопировав из предыдущей версии решения из Часть I, – то возможно их стоит сделать "приватными" (добавив перед именем подчеркивание), чтобы не дать возможность в тесте – миксовать подход, а использовать только высокоуровневые шаги, но можно и не вводить такое ограничение.

  * вероятно, проще вместо добавления таких средне-уровневых шагов из Часть I – добавить в init поля объекта для всех элементов и переиспользовать их внутри реализации .register(user). Таким образом реализация будет более лаконичная и все еще достаточно гибкая, чтобы в будущем иметь доступ к элементам в контексте других "бизнес задач" на этой странице.

* Классы для PageObject и модели данных должны лежать в выделенных модулях в выделенных пакетах внутри проекта, как было показано на уроке 😉

* При реализации модели данных для реализации тех или иных полей будет неплохо использовать специальные типы данных, например, для даты использовать datetime.date, а для хобби использовать Enum 😉 





Часть III – ДОПОЛНИТЕЛЬНО/НЕ-ОБЯЗАТЕЛЬНО (реализовать в бренче application-manager)

* добавить в проект тест на упрощенную регистрацию через форму https://demoqa.com/text-box  и соответствующий PageObject. 

  * Реализовать шаблон ApplicationManager для предсоздания всех объектов для пейдж-обджектов.

  * в тесте загрузить форму не через simple_registration_form.open(), а через app.left_panel.open_simple_registration_form(), который должен быть шорткатом (методом, вызывающим под капотом другой метод этого же объекта) на app.left_panel.open('Elements', 'Text Box')

    * cоответственно добавить пейджобджект для LeftPanel и создать его объект в виде поля обьекта апликейшен-менеджера
 
"""

python_10_11

"""
Урок // https://www.youtube.com/watch?v=mjlrTdwQ_pY
Репо // https://github.com/yashaka/selene-in-action/tree/py05-lesson-configuration-management-with-pydantic

Вводный урок к этому: «Базовое управление конфигурацией через переменные среды». // https://www.loom.com/share/a3657e6a84b94fcda1a1b94e5c0a97d4
Стоит посмотреть перед началом просмотра этого урока

Кодекс Python // https://peps.python.org/pep-0020/
О консистентности в именах // https://tonsky.livejournal.com/304954.html?
Менее универсальная альтернатива для Pydantic - Pytest options (не рекомендуется к использованию для конфигурации проекта, но знать стоит) // https://docs.pytest.org/en/6.2.x/example/simple.html?highlight=pytest%20option#pass-different-values...
Пример проекта с более приближенной к реальности конфигурацией // https://github.com/yashaka/python-web-test
Примеры разных конфигураций драйвера для Selene, в том числе используемые pydantic или dotenv, или и то и то вместе // https://github.com/yashaka/selene/tree/master/examples


Пример рефакторинга с целью создания своей собственной версии Pydantic: 


Теория: 

 – Python Descriptors: An Introduction // https://realpython.com/python-descriptors/

 – Python Dataclasses from Scratch // https://xavd.id/blog/post/python-dataclasses-from-scratch/

Практика:

– шаг 1  // https://github.com/yashaka/selene/blob/master/examples/run_remote_in_web_chrome_with_options_for_selenoid/test_todomvc.py

– шаг 2 // https://github.com/yashaka/selene/blob/master/examples/run_remote_in_android_chrome_with_options_for_browserstack/test_todomvc.py

– шаг 3 // https://github.com/yashaka/selene/blob/master/examples/run_remote_in_ios_safari_with_options_for_browserstack/test_todomvc.py

– шаг 4 // https://github.com/yashaka/selene/blob/master/examples/run_remote_in_android_app_with_options_for_browserstack/version_1__original_selene_browser_style/test_wikipedia.py

– шаг 5 // https://github.com/yashaka/selene/blob/master/examples/run_remote_in_android_app_with_options_for_browserstack/version_4__app_fixture_style/test_wikipedia.py

Библиотека для явных ожиданий (не только для веба, а например для конекшена к базе данных) // https://github.com/rockem/busypie

~~~~
"""
Разбор дз // https://www.youtube.com/watch?v=sGVRpOTHKtA

python_10_12

"""
Урок https://www.youtube.com/watch?v=jmHvqLD0FHA

Ссылка на Jenkins  // https://jenkins.autotests.cloud/login?from=%2F

Ссылка на репозиторий // https://github.com/qa-guru/qa_guru_python_9_jenkins/tree/demoqa
Ссылка на Jenkins simple // https://jenkins.autotests.cloud/login?from=%2Fjob%2Fteacher-iTerkin-qa_guru_python_9_jenkins_simple%2F
Ссылка на Jenkins demoqa // https://jenkins.autotests.cloud/login?from=%2Fjob%2Fteacher-iTerkin-qa_guru_python_9_jenkins_demoqa

Конспект лекций // https://github.com/qa-guru/knowledge-base

______

ДЗ
1. Взять свой код для http://demoqa.com/automation-practice-form
2. Добавить аттачи для Allure – скриншот, page source, console.log и видео
3. Cделать сборку в Jenkins

В качестве ответа нужно приложить ссылку на Allure-отчет в Jenkins (с видео)
"""

РАЗБОР Дз по pageobject // https://www.youtube.com/watch?v=2QGnf_WlVbE

Рекомендации и общепринятые договоренности в подборе имен (Python) // https://autotest.how/sdet-start-ru
Stop Writing Classes // https://www.youtube.com/watch?v=o9pEzgHorH0

python_10_13

"""
Lesson // https://www.youtube.com/watch?v=syPeao2M8TQ

Ссылка на репозиторий // https://jenkins.autotests.cloud/login?from=%2Fjob%2Fteacher-iTerkin-qa_guru_python_1_9_jenkins%2F
Ссылка на jenkins // https://github.com/qa-guru/qa_guru_python_1_9_jenkins/

___________

Home task
1. Доработать свой код на регистрационную форму с аллюровскими степами

2. Доработать код, чтобы он запускался не локально, а браузер в selenoid.autotests.cloud

3. Добавить аттачменты - скриншот, логи консоли, page source, видео

4. Сделать сборку в jenkins.autotests.cloud (регистрация открыта) с кодом

5. Передать из дженкинса адрес удаленного браузера

6. Спрятать логин/пароль к удаленному браузеру в .env файл
"""

Q&A сессия к занятиям PageObjects и Configuration Management // https://www.youtube.com/watch?v=c2yaYmFlu3E

"""
– The Practical Test Pyramid // https://martinfowler.com/articles/practical-test-pyramid.html

– Раздел «Classical Inheritance is Obsolete» из книги Эрика Элиотта  https://www.oreilly.com/library/view/programming-javascript-applications/9781491950289/ch03.html
– Доклад Эрика Элиотта  // https://vimeo.com/69255635

Цитаты: «Inheritance hierarchies are trouble: inflexible, tightly coupled (child HAS TO KNOW IMPL of parent class), non-natural», «e.g. you have Tools and Weapons that you designed for war context. Maybe you can reuse them for "tactical training" but you probably can't build a "Clue board game" with them ;)»

– Статья о Why you should not use SetUp and TearDown // https://jamesnewkirk.typepad.com/posts/2007/09/why-you-should-.html

– SDET Engineer Skills Upgrade Programm // https://docs.google.com/document/d/1yf6-uhTIM2jpHa9NfoFHAJgKucuqwkH_XhSzuwjwcQQ/edit

"""

python_10_14

"""
Lesson // https://www.youtube.com/watch?v=ZbpwaZJrQt8

– Репозиторий с кодом // https://github.com/qa-guru/qa_guru_python_9_jenkins
– https://jenkins.autotests.cloud/job/teacher-iTerkin-qa_guru_python_9_jenkins_notifications/2/allure/
– https://jenkins.autotests.cloud/job/teacher-iTerkin-qa_guru_python_9_jenkins_notifications_positive

Бот с уведомлениями // https://github.com/qa-guru/allure-notifications
Wiki // https://github.com/qa-guru/allure-notifications/wiki
Конспект лекций // https://github.com/qa-guru/knowledge-base
____________

Задание
1. Создайте проект с любыми автотестами, либо возьмите уже созданный.
2. Создайте задачу в Jenkins.
3. Зарегистрируйте бота в Telegram, создайте чат и добавьте бота в него. 
4. Добавьте бота к вашему проекту.
Для выполнения домашнего задания нужно приложить скриншот из телеграм-чата с нотификацией о прохождении автотестов в поле ответа.
"""

Дополнительное занятие. Логирование шагов и Декораторы. Яков Крамаренко // https://www.youtube.com/watch?v=DeJYgj86Nd4
Репо // https://gist.github.com/yashaka/0cb814a5de49f4dc91a3a8528bf0d6e7

python_10_15

"""
15. Учимся быстро разрабатывать готовые проекты для тестовых заданий. Васенков Станислав
Набиваем руку небольшими проектами.
1. Находим интересную нам вакансию (hh.ru / linkedin / @qa_jobs)
2. Делаем небольшой проект:
– разрабатываем 5-10 простых автотестов на сайт из вакансии,
  – создаем задачу в Jenkins,
– прячем секретные данные (должны быть вынесены в отдельный файл / конфиг сборки в Jenkis)
– настраиваем Allure-отчет, добавляем вложения:
– снимки экрана,
– логи браузера,
– видеозапись теста,
– тест-план Allure TestOps - с ручными и автоматизированными тестами
– интеграцию с Jira
– настраиваем нотификацию в Telegram / Slack.

По мере прохождения курса добавим сюда:
– автотесты на API
3. Отправляем наш проект HR c сопроводительным письмом

Lesson // https://www.youtube.com/watch?v=tF0K813nH6I

Ссылка на репозиторий // https://jenkins.autotests.cloud/login?from=%2Fjob%2Fteacher-iTerkin-qa_guru_python_8_full_project%2F

Конспект лекций // https://github.com/qa-guru/knowledge-base

Доступы к сервисам

https://jira.autotests.cloud/
jira8 jira8
https://allure.autotests.cloud
allure8 allure8




Полезные ссылки: 

– https://jenkins.autotests.cloud/job/teacher-iTerkin-qa_guru_python_10_jenkins_full_project/
– https://allure.autotests.cloud/launch/36279
– https://jira.autotests.cloud/browse/HOMEWORK-1139


Оформляем README.md
Необходимо посмотреть дополнительное занятие - Дополнительное занятие. Станислав Васенков. «GitHub. Readme / Markdown»


Обязательно должны быть:
- Команды запуска тестов из терминала с пояснением ключей
- История со скриншотами - где что происходит, запускается
- Гифка с тестом (из видео в selenoid)
- Иконки используемого стека для красоты

Дополнительное занятие. Даниил Шатухин. «Оформляем README профиля на GitHub» // https://www.youtube.com/watch?v=r52XllO_3TQ

Дополнительное занятие. Даниил Шатухин. «Рисуем диаграммы с помощью Mermaid.js и Markdown» // https://www.youtube.com/watch?v=uJuskThFWW8

__________

Задание
1. Выберите вакансию 

2. Напишите на неё автотестов:

- 5-10 простых. Главное – не тратьте на это много времени!

- Тесты должны проверять основную логику приложения (регистрация, аутентификация, поиск, добавление/удаление товара из корзины, оформление заказа и др.)

- Использование параметризованных тестов не запрещается, но вся работа НЕ должна состоять из одного большого теста с параметрами (в случае, если тесты могут быть объединены в один параметризованный тест, то все подходящие тесты будут засчитываться как один).

3. Сделайте джобу в Jenkins, добавьте Allure отчёт, уведомления в чат Telegram, Selenoid.

4. Оформите всё со скриншотами в readme.md



В поле ответа на задание приложите: ссылку на джобу в Jenkins, репозиторий с тестами на github, скриншот письма рекрутёру.

Если вы не находитесь в поиске работы, просто сбросьте всё вышеуказанное на ревью. 
"""

python_10_16

"""
16. Pytest. Сергей Хомутинин. Занятие в записи
1. Аргументы запуска. Собираем фикстуры, марки и другую полезную информацию для отладки
2. Марки. Пропускаем тесты правильно
3. Параметризация. На тесте, на фикстуре. Переопределение параметров

Lesson // https://www.youtube.com/watch?v=g9y0nh2IpeM

Ссылка на репозиторий // https://github.com/qa-guru/qa_guru_python_5_15

How to parametrize fixtures and test functions // https://docs.pytest.org/en/7.1.x/how-to/parametrize.html

Запись с занятия. Часть II // https://www.youtube.com/watch?v=RHO9FGOxWOg

Ссылка на репозиторий // https://github.com/qa-guru/qa_guru_python_5_15_p2

Полезные ссылки
https://github.com/pytest-dev/pytest/issues/3261#issuecomment-369740536
https://pytest-xdist.readthedocs.io/en/latest/how-to.html

Решение проблемы с session-scope фикстурами при параллельном тестировании // https://pytest-xdist.readthedocs.io/en/latest/how-to.html#making-session-scoped-fixtures-execute-only-once

Хуки в документации  // https://docs.pytest.org/en/7.2.x/reference/reference.html#hooks

Конспект лекций // https://github.com/qa-guru/knowledge-base

________
Задание
- Реализовать автотест для github.com, который заходит на страницу, ищет кнопку Sign In, и нажимает на нее (авторизоваться не нужно);

- Параметризовать тест различным размером окна браузера;

- Обратите внимание, что для мобильной версии сайта потребуется другой автотест из-за изменения структуры локаторов;

- Сделайте два варианта пропуска неподходящих параметров и тестов.

1. Пропустите мобильный тест, если соотношение сторон десктопное (и наоборот);

2. Переопределите параметр с помощью indirect;

3. Сделайте разные фикстуры для каждого теста.

В чем преимущества и недостатки каждого из подходов?

"""
