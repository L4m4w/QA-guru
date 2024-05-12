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
"""
