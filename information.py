# P.S Файл предназначен для изменения данных, которые заполняются при запуске автотестов, для каждого могут различаться

#  -------------------------------------------------МЕНЕДЖЕР ПРОИСШЕСТВИЙ--------------------------------
# для авторизации
serenity = "192.168.10.237:8888"
login = "admin"
password = "admin"
firefly = "192.168.10.237:8243"

# данные для заполнения полей в создании новой задачи (Заявка на ТО)

task_fio = "Иванов Иван Иванович автотест"
task_phone = "1111111111"
task_address= "Самарская область, Самара, Ул. Стара-Загора 96а"
task_language = "Русский"

# текст в новом регламенте в таблице "вопросы"
question_text = "У меня текстовый вопрос"

# текст для названия нового регламента
name_of_new_reglament ="autotest"

# текст у измененного регламента (вводится при редактировании
edited_name_reglament = "edited_autotest"

# текст в редактируемом регламенте в таблице "вопросы"
new_name_question = "У меня отредактированный текстовый вопрос"

# название новой задачи
name_of_new_task = "autotest_new_task"
# текст у отредактированной задачи
edited_name_task = "edited_autotest_task"

# координаты и возможно что-то ещё для добавления нового регламента
coordinates = "53.228425 50.199929"



# -------------------------------------------------ЦЕНТР АВТОРИЗАЦИИ--------------------------------

# логин+пароль для центра авторизации
# P. S используются одинаковые фф+серенити, как и для менеджера проишествий, если надо будут другие - вынесу в отдельные переменнные
center_login = "dimatest"
center_pass = "dimatest"

# информация для нового юзера в ЦА
new_user_login = "ilya_autotest"
new_user_pass = "ilya_autotest"
new_user_lastname = "Autotest"
new_user_name = "Autotest"
new_user_patronymic = "Autotestovich"


# информация для редактирования информации о юзере
edited_user_login = "edited_ilya_autotest"
edited_user_pass = "edited_ilya_autotest"
edited_user_lastname = "Autotest_edited"
edited_user_name = "Autotest_edited"
edited_user_patronymic = "Autotestovich_edited"

# информация для логина под фф
center_ff_login = "firefly"
center_ff_pass = "firefly"