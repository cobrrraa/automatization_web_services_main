import time  # для отладки
from colorama import Fore
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By  # для поиска by
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from information import serenity, login, password, firefly, task_fio, task_phone, task_address, task_language, \
    coordinates, question_text, edited_name_reglament, new_name_question, name_of_new_reglament, name_of_new_task, \
    edited_name_task

#   test number 41 (ipe-41: Открытие приложения)

# добавлен на всякий случай и вставлен в некоторых местах - чисто на всякий случай.
delay = 1
driver = (webdriver.Chrome())
driver.get('http://192.168.10.237:7000/index3D.html')
chrome_options = Options()
chrome_options.add_argument("--disable-extensions")
driver.maximize_window()
action = ActionChains(driver)

# ожидание и открытие формы авторизации
try:
    wait_auth_form = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.ID, "settingsButton")))
    # клик на кнопку настроек
    settings_log_form = driver.find_element(By.ID, 'settingsButton')
    settings_log_form.click()
except TimeoutException:
    print(Fore.RED + "Не смог открыть окно авторизации")
    driver.quit()

# заполнение поля ip адрес
input_ipaddr = driver.find_element(By.ID, 'ip_address')
input_ipaddr.click()
input_ipaddr.send_keys(serenity)

# заполнение поля логин
input_login = driver.find_element(By.ID, 'id_username')
input_login.click()
input_login.send_keys(login)

# заполнение поля пароль
input_password = driver.find_element(By.ID, 'id_password')
input_password.click()
input_password.send_keys(password)

input_password.send_keys(Keys.RETURN)

try:
    input_firefly_wait = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.ID, 'firefly')))
    input_firefly = driver.find_element(By.ID, 'firefly')  # заполнение поля фф + проверка
    input_firefly.click()
    input_firefly.send_keys(firefly)
    input_firefly.send_keys(Keys.RETURN)
except TimeoutException:
    print(Fore.RED + "Авторизация не произошла")
    driver.quit()

try:
    entry_mngr_incident = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.ID, 'loginDiv')))
    entry_mngr_incident.click()
except TimeoutException:
    print(Fore.RED + "Авторизация не произошла")
    driver.quit()

# проверка где я нахожусь, ищу по левой панели
try:
    main_page_waiting = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.XPATH, "//div[@id='main-sidenav']")))
    print(Fore.GREEN + "Планета открылась")

except TimeoutException:
    print(Fore.RED + "Планета не открылась")
    driver.quit()

# поиск и клик на выпадающий список слева на панели НЕ РАБОТАЕТ
try:
    drop_down_wait = WebDriverWait(driver, 60).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@id='sidenav-toggle']")))
    time.sleep(4)  # КАК ОТ ЭТОГО ИЗБАВИТЬСЯ????????????????????????????
except TimeoutException:
    driver.quit()

drop_down_list_click = driver.find_element(By.XPATH, "//div[@id='sidenav-toggle']")
drop_down_list_click.click()

# ожидание на доступность кнопки с планетой
try:
    options_wait = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.ID, "sidenav-menu-planet")))
    print(Fore.GREEN + "Открыл выпадающий список в Интегра-4д")
except TimeoutException:
    print(Fore.RED + "Не открыл выпадающий список в Интегра-4Д")
    driver.quit()

ipe_open_window = driver.find_element(By.XPATH, "//a[@id='sidenav-menu-planet']")
ipe_open_window.click()

# проверка, что окно планеты открылось
try:
    ipe_window_isOpen = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.XPATH, "//div[@id='cesiumContainerDiv']")))
    print(Fore.GREEN + "Окно 'планеты' открылось")
except TimeoutException:
    print(Fore.RED + "Окно 'планеты' не открылось")
    driver.quit()

# открытие менеджера происшествий
mngr_open_window = driver.find_element(By.XPATH, "//a[@id='sidenav-menu-cardevent']")
mngr_open_window.click()

try:
    mngIncident_window_isOpen = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.XPATH, "//div[@id='integra-cardevent']")))
    print(Fore.GREEN + "Окно Менеджер происшествий открылось")
except TimeoutException:
    print(Fore.RED + "Окно Менеджер происшествий не открылось")
    driver.quit()

ipe_script = """
function resizeIframe() {
  var iframe = document.getElementById('cesiumContainerDiv'); 
  iframe.style.width = '23.5417%';
  iframe.style.height = '100%';
  iframe.style.left = '2.65625%';
  iframe.style.top = '0%';
}
resizeIframe();
"""

driver.execute_script(ipe_script)

# поиск и переключение на iframe с менеджером происшествий + изменение размера менеджера происшествий

cardevent_script = """
function resizeIframe() {
  var iframe = document.getElementById('integra-cardevent'); 
  iframe.style.width = '73.6979%'; // Новая ширина iframe
  iframe.style.height = '99.7888%'; // Новая высота iframe
  iframe.style.left = '26.3021%';
  iframe.style.top = '0%';
}
resizeIframe();
"""

driver.execute_script(cardevent_script)

iframe_cardevent = driver.find_element(By.XPATH, "//iframe[@class='nodrag']")
driver.switch_to.frame(iframe_cardevent)

try:
    main_page_wait = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.ID, "drop-editors")))
    # ожидание прогрузки главной страницы 60 секунд, если грузит раньше = выполняется дальше, не выполняется = выводит сообщ
    print(Fore.BLUE + "Test case 'ipe-41: Открытие приложения' -  ПРОЙДЕНО")
except TimeoutException:
    print(Fore.RED + "x")
    driver.quit()

# test number 42 (ipe-42: Добавление регламента инцидента)

# клик на шестеренку
settings_main_form = driver.find_element(By.XPATH,
                                         "//button[@id='drop-editors']//span[@class='mat-button-wrapper']")
settings_main_form.click()

try:
    wait_forclick_editorRegl = WebDriverWait(driver, 60).until(
        EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Редактор регламентов инцидентов')]")))
    editor_reglament = driver.find_element(By.XPATH, "//span[contains(text(),'Редактор регламентов инцидентов')]")
    editor_reglament.click()
except TimeoutException:
    print(Fore.RED + "Не смог нажать на 'Редактор регламентов инцидентов'")
    driver.quit()

#
new_reg_editor_main_page = driver.find_element(By.XPATH, "//span[contains(text(),'Регламенты инцидентов')]")
if new_reg_editor_main_page.text == "Регламенты инцидентов":

    print(Fore.GREEN + "Страница с регламентами инцидентов открыта")
else:
    print(Fore.RED + "Страница со всеми регламентами инцидентов не открыта")
    driver.quit()

# клик на кнопку "Добавить регламент"
add_new_regl = driver.find_element(By.XPATH, "//span[contains(text(),'Добавить регламент')]")
add_new_regl.click()

# проверка на то где нахожусь
new_reg_editor_page = driver.find_element(By.XPATH, "//div[@class='f-r-q-card f-r-q-editor ng-star-inserted']//div[1]")
if new_reg_editor_page.text == "Редактор вопросов":
    print(Fore.GREEN + "Страница с добавлением нового регламента инцидента открыта")
else:
    print(Fore.RED + "Страница с добавлением нового регламента инцидента не открыта")
    driver.quit()

# поиск и клик на категорию регламента
try:
    wait_forclick_type = WebDriverWait(driver, 60).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@mattooltip='Категория регламента']")))
    type_of_incident = driver.find_element(By.XPATH, "//div[@mattooltip='Категория регламента']")
    type_of_incident.click()
    print(Fore.GREEN + "Окно 'Категория регламентов' открылось")
except TimeoutException:
    print(Fore.RED + "Окно 'Категория регламентов' не открылось")
    driver.quit()

# выбор категории, можно заменить riots.png на любую другую
try:
    wait_forclick_icon = WebDriverWait(driver, 60).until(
        EC.element_to_be_clickable((By.XPATH, "//img[@src='assets/img/icons/riots.png']")))
    choose_type_of_incident = driver.find_element(By.XPATH, "//img[@src='assets/img/icons/riots.png']")
    choose_type_of_incident.click()
except TimeoutException:
    driver.quit()

# сохранение категории регламента
try:
    wait_forclick_icon = WebDriverWait(driver, 60).until(EC.element_to_be_clickable(
        (By.XPATH, "//button[@type='button']//span[@class='mat-button-wrapper'][contains(text(),'Сохранить')]")))
    save_type_of_incident = driver.find_element(By.XPATH,
                                                "//button[@type='button']//span[@class='mat-button-wrapper']["
                                                "contains(text(),'Сохранить')]")
    save_type_of_incident.click()
except TimeoutException:
    driver.quit()

add_question = driver.find_element(By.XPATH, "//input[@id='mat-input-3'][1]")  # поиск и клик по инпуту в поле "Вопросы"
add_question.click()
add_question.send_keys(question_text)

# поиск и клик на выпадающий список "Тип вопроса"
type_of_question = driver.find_element(By.XPATH, "//span[contains(text(),'В каком формате должен быть ответ?')]")
type_of_question.click()

try:
    wait_forclick_type = WebDriverWait(driver, 60).until(
        EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Текстовый')]")))
    text_type = driver.find_element(By.XPATH, "//span[contains(text(),'Текстовый')]")
    text_type.click()
except TimeoutException:
    print(Fore.RED + "Не открыл выпадающий список с выбором типа вопроса")
    driver.quit()

# выпадающий список "группы для просмотра
groups_can_see = driver.find_element(By.XPATH, "//span[contains(text(),'Какие Группы необходимо назначить?')]")
groups_can_see.click()
time.sleep(delay)

try:
    wait_forclick_groupsSEE = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, "//mat-option[1]")))
except TimeoutException:
    print(Fore.RED + "Выпадающий список в 'Группы для просмотра' не открылся")
    driver.quit()

# выбор групп которые могут смотреть
choose_group1_see = driver.find_element(By.XPATH, "//span[contains(text(),'Группа 1')]")
choose_group1_see.click()

choose_group2_see = driver.find_element(By.XPATH, "//span[contains(text(),'Группа 2')]")
choose_group2_see.click()

choose_group3_see = driver.find_element(By.XPATH, "//span[contains(text(),'Группа 3')]")
choose_group3_see.click()

choose_group4_see = driver.find_element(By.XPATH, "//span[contains(text(),'Группа 4')]")
choose_group4_see.click()

# клик escape - чтобы выйти из выпадающего списка
webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
# кажется незаменимо))
time.sleep(0.5)

# выпадающий список группы для редактирования
groups_can_edit = driver.find_element(By.XPATH, "//span[contains(text(),'Кто может изменять вопрос?')]")
groups_can_edit.click()

#
try:
    wait_forclick_groupsEDIT = WebDriverWait(driver, 60).until(
        EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Выбрать все')]")))
    choose_group_edit = driver.find_element(By.XPATH, "//span[contains(text(),'Выбрать все')]")
    choose_group_edit.click()
except TimeoutException:
    print(Fore.RED + "Выпадающий список в 'Группы для редактирования' не открылся")
    driver.quit()

# клик escape - чтобы выйти из выпадающего списка
webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
# кажется незаменимо))
time.sleep(0.5)


# заполнение названия регламента
def fill_nameOfReglament():
    try:
        WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Название регламента']")))
        name_of_new_reg = driver.find_element(By.XPATH, "//input[@placeholder='Название регламента']")
        name_of_new_reg.click()
        name_of_new_reg.clear()
        name_of_new_reg.send_keys(name_of_new_reglament)

    except TimeoutException:
        print("Не смог нажать на инпут с названием регламента")
        driver.quit()

    try:
        WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Сохранить регламент')]")))
        save_new_reglament = driver.find_element(By.XPATH, "//span[contains(text(),'Сохранить регламент')]")
        save_new_reglament.click()
        time.sleep(1)  # тоже хз что делать с этим
    except TimeoutException:
        print("Не смог нажать на кнопку сохранения регламента")
        driver.quit()


def check_notifications():
    try:
        notification = driver.find_element(By.XPATH, "//div[@class='noty_message']")
        message = notification.text
        if message == "Данные успешно сохранены":
            return "success"
        elif message == "Регламент с таким названием уже существует!":
            return "exists"
        else:
            return "unknown"
    except NoSuchElementException:
        return "not_found"


counter = 1
max_attempts = 10

while counter <= max_attempts:
    try:
        name_of_new_reglament = f"{name_of_new_reglament}{counter}"
        fill_nameOfReglament()
        result = check_notifications()
        if result == "success":
            print(f"Задача с названием '{name_of_new_reglament}' успешно добавлена.")
            print(Fore.GREEN + "Уведомление 'Данные успешно сохранены' появилось")
            print(Fore.BLUE + "Test case 'ipe-42  Добавление регламента инцидента' - ПРОЙДЕНО")
            try:
                notification = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, "//div[@class='noty_message']")))
                # Ожидание, пока уведомление исчезнет
                while True:
                    try:
                        notification.is_displayed()  # Проверяем, видим ли элемент
                        time.sleep(3)

                    except:
                        break  # Если элемент не видим, выходим из цикла
                    time.sleep(1)  # Если элемент видим, ждем 1 секунду и повторяем проверку
            except:
                pass  # Если элемент не найден, продолжаем выполнение программы
            break

        elif result == "exists":
            print(f"Ошибка: Задача с названием '{name_of_new_reglament}' уже существует.")
            time.sleep(delay)
            close_noty = driver.find_element(By.XPATH, "//div[@class='noty_close']")  # noty_close
            close_noty.click()
            name_of_new_reg = driver.find_element(By.XPATH, "//input[@placeholder='Название регламента']")
            name_of_new_reg.click()
            name_of_new_reg.clear()
            counter += 1
        else:
            # print(Fore.RED + "Уведомление не найдено.")
            driver.quit()
            break
    except TimeoutException:
        print("Ошибка: Время ожидания истекло.")
        driver.quit()
        break
    except Exception as e:
        print(Fore.RED + f"Произошла ошибка: {e}")
        driver.quit()
        break
else:
    print(Fore.RED + "Достигнуто максимальное количество попыток. Тест не может быть завершен.")

try:
    journal_wait = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Регламенты инцидентов')]")))
except TimeoutException:
    print("не вышел из страницы")
    driver.quit()

# test number 44 (ipe-44: Редактирование  регламента инцидента)

edit_new_reg_editor_page = driver.find_element(By.XPATH, "(//h3[normalize-space()='autotest1 [test_sofa]'])[1]")
edit_new_reg_editor_page.click()

try:
    wait_editorRegl = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Регламент инцидента')]")))
    print(Fore.GREEN + "Открыл страницу редактирования регламента")
except TimeoutException:
    print(Fore.RED + "Не открыл страницу редактирования регламента")
    driver.quit()

add_question = driver.find_element(By.XPATH, "//input[@type='text']")  # поиск и клик по инпуту в поле "Вопросы"
add_question.click()
add_question.clear()
add_question.send_keys(new_name_question)

type_of_question = driver.find_element(By.XPATH, "//mat-select[@placeholder='В каком формате должен быть ответ?']")
type_of_question.click()
# ожидание на появление выпадающего списка в "тип вопроса"
try:
    wait_forclick_type = WebDriverWait(driver, 60).until(
        EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Числовой')]")))
    text_type = driver.find_element(By.XPATH, "//span[contains(text(),'Числовой')]")
    text_type.click()
except TimeoutException:
    print(Fore.RED + "Не открыл выпадающий список с выбором типа вопроса")
    driver.quit()

question_block = driver.find_element(By.XPATH, "//mat-select[@placeholder='К какому блоку относится вопрос?']")
question_block.click()
time.sleep(delay)
choose_block1 = driver.find_element(By.XPATH, "//span[@class='mat-option-text'][contains(text(),'Блок 1')]")
choose_block1.click()


def rename_nameOfReglament():
    try:
        WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Название регламента']")))
        edited_name_reg = driver.find_element(By.XPATH, "//input[@placeholder='Название регламента']")
        edited_name_reg.click()
        edited_name_reg.clear()
        edited_name_reg.send_keys(edited_name_reglament)
    except TimeoutException:
        print("Не смог нажать на инпут с названием регламента")
        driver.quit()

    try:
        WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Сохранить регламент')]")))
        save_new_reglament = driver.find_element(By.XPATH, "//span[contains(text(),'Сохранить регламент')]")
        save_new_reglament.click()
        time.sleep(1)  # тоже хз что делать с этим
    except TimeoutException:
        print("Не смог нажать на кнопку сохранения регламента")
        driver.quit()


def check_notifications():
    try:
        notification = driver.find_element(By.XPATH, "//div[@class='noty_message']")
        message = notification.text
        if message == "Данные успешно сохранены":
            return "success"
        elif message == "Регламент с таким названием уже существует!":
            return "exists"
        else:
            return "unknown"
    except NoSuchElementException:
        return "not_found"


counter = 1
max_attempts = 10

while counter <= max_attempts:
    try:
        edited_name_reglament = f"{edited_name_reglament}{counter}"
        rename_nameOfReglament()
        result = check_notifications()
        if result == "success":
            print(f"Задача с названием '{edited_name_reglament}' успешно добавлена.")
            try:
                notification = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, "//div[@class='noty_message']")))
                # Ожидание, пока уведомление исчезнет
                while True:
                    try:
                        notification.is_displayed()  # Проверяем, видим ли элемент
                        time.sleep(3)
                        print(Fore.GREEN + "Уведомление 'Данные успешно сохранены' появилось")
                        print(Fore.BLUE + "Test case 'ipe-44  Редактирование регламента инцидента' - ПРОЙДЕНО")
                    except:
                        break  # Если элемент не видим, выходим из цикла
                    time.sleep(1)  # Если элемент видим, ждем 1 секунду и повторяем проверку
            except:
                pass  # Если элемент не найден, продолжаем выполнение программы
            break
        elif result == "exists":
            print(f"Ошибка: Задача с названием '{edited_name_reglament}' уже существует.")
            close_noty = driver.find_element(By.XPATH, "//div[@class='noty_close']")  # noty_close
            close_noty.click()
            edited_name_reg = driver.find_element(By.XPATH, "//input[@placeholder='Название регламента']")
            edited_name_reg.click()
            edited_name_reg.clear()
            counter += 1
        else:
            # print("Уведомление не найдено.")
            driver.quit()
            break
    except TimeoutException:
        print("Ошибка: Время ожидания истекло.")
        driver.quit()
        break
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        driver.quit()
        break
else:
    print("Достигнуто максимальное количество попыток. Тест не может быть завершен.")

    # test number 43 (ipe-43: Добавление регламента задачи)

# клик на шестеренку
settings_main_form = driver.find_element(By.XPATH, "//button[@id='drop-editors']//span[@class='mat-button-wrapper']")
settings_main_form.click()

try:
    wait_forclick_editorRegl = WebDriverWait(driver, 60).until(
        EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Редактор регламентов задач')]")))
    editor_reglament = driver.find_element(By.XPATH, "//span[contains(text(),'Редактор регламентов задач')]")
    editor_reglament.click()
except TimeoutException:
    print(Fore.RED + "Не смог нажать на 'Редактор регламентов задач'")
    driver.quit()

# проверка на то где нахожусь
new_reg_task_editor_main_page = driver.find_element(By.XPATH, "//span[contains(text(),'Регламенты задач')]")
if new_reg_task_editor_main_page.text == "Регламенты задач":
    print(Fore.GREEN + "Страница с регламентами задач открыта")
else:
    print(Fore.RED + "Страница со всеми регламентами задач не открыта")
    driver.quit()

# клик на добавление нового регламента задач

new_reg_task_page = driver.find_element(By.XPATH, "//span[contains(text(),'Добавить регламент')]")
new_reg_task_page.click()

# проверка на то где нахожусь
new_reg_task_editor_page = driver.find_element(By.XPATH, "//span[contains(text(),'Создание регламента задач')]")
if new_reg_task_editor_page.text == "Создание регламента задач":
    print(Fore.GREEN + "Страница с добавлением нового регламента задачи открыта")
else:
    print(Fore.RED + "Страница с добавлением нового регламента задачи не открыта")
    driver.quit()

# заполнение поля у нового регламента задач ЦИКЛ
name_of_new_reg_task = driver.find_element(By.XPATH, "//input[@placeholder='Название регламента']")
name_of_new_reg_task.click()
name_of_new_reg_task.send_keys(name_of_new_task)

try:
    wait_for_click_groups = WebDriverWait(driver, 60).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@aria-hidden='true']//div//span[contains(text(),'Группы')]")))
    groups_regl_task = driver.find_element(By.XPATH, "//div[@aria-hidden='true']//div//span[contains(text(),'Группы')]")
    groups_regl_task.click()
    time.sleep(delay)
except TimeoutException:
    print(Fore.RED + "Не смог открыть Группы")
    driver.quit()

try:
    wait_for_dropdown_groups = WebDriverWait(driver, 60).until(
        EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Группа 5')]")))
except TimeoutException:
    print("Не смог открыть выпадающий список")
    driver.quit()
# выпадающий список групп
choose_group1_task = driver.find_element(By.XPATH, "//span[contains(text(),'Группа 1')]")
choose_group1_task.click()

choose_group2_task = driver.find_element(By.XPATH, "//span[contains(text(),'Группа 2')]")
choose_group2_task.click()

choose_group3_task = driver.find_element(By.XPATH, "//span[contains(text(),'Группа 3')]")
choose_group3_task.click()

choose_group4_task = driver.find_element(By.XPATH, "//span[contains(text(),'Группа 4')]")
choose_group4_task.click()

choose_group5_task = driver.find_element(By.XPATH, "//span[contains(text(),'Группа 5')]")
choose_group5_task.click()

# клик escape - чтобы выйти из выпадающего списка
webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
# кажется незаменимо))
time.sleep(0.5)

category_task = driver.find_element(By.XPATH, "//div[@aria-hidden='true']//div//span[contains(text(),'Категория')]")
category_task.click()
time.sleep(delay)

try:
    wait_for_dropdown_category = WebDriverWait(driver, 60).until(
        EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Биологическая опасность')]")))
    choose_category_task = driver.find_element(By.XPATH, "//span[contains(text(),'Биологическая опасность')]")
    choose_category_task.click()
except TimeoutException:
    print("Не смог открыть выпадающий список")
    driver.quit()


def fill_nameOfTask():
    try:
        WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Название регламента']")))
        name_of_newReglTask = driver.find_element(By.XPATH, "//input[@placeholder='Название регламента']")
        name_of_newReglTask.click()
        name_of_newReglTask.clear()
        name_of_newReglTask.send_keys(name_of_new_task)
    except TimeoutException:
        print("Не смог нажать на инпут с названием регламента задачи")
        driver.quit()

    try:
        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Сохранить')]")))
        save_new_reglament_task = driver.find_element(By.XPATH, "//span[contains(text(),'Сохранить')]")
        save_new_reglament_task.click()
        time.sleep(1)  # тоже хз что делать с этим
    except TimeoutException:
        print("Не смог нажать на кнопку сохранения регламента")
        driver.quit()


def check_notifications():
    try:
        notification = driver.find_element(By.XPATH, "//div[@class='noty_message']")
        message = notification.text
        if message == "Данные успешно сохранены":
            return "success"
        elif message == "Регламент с таким названием уже существует!":
            return "exists"
        else:
            return "unknown"
    except NoSuchElementException:
        return "not_found"


counter = 1
max_attempts = 10

while counter <= max_attempts:
    try:
        name_of_new_task = f"{name_of_new_task}{counter}"
        fill_nameOfTask()
        result = check_notifications()
        if result == "success":
            print(f"Задача с названием '{name_of_new_task}' успешно добавлена.")
            print(Fore.GREEN + "Уведомление 'Данные успешно сохранены' появилось")
            print(Fore.BLUE + "Test case 'ipe-43  Добавление регламента задачи' - ПРОЙДЕНО")
            try:
                notification = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, "//div[@class='noty_message']")))
                # Ожидание, пока уведомление исчезнет
                while True:
                    try:
                        notification.is_displayed()  # Проверяем, видим ли элемент
                        time.sleep(3)
                    except:
                        break  # Если элемент не видим, выходим из цикла
                    time.sleep(1)  # Если элемент видим, ждем 1 секунду и повторяем проверку
            except:
                pass  # Если элемент не найден, продолжаем выполнение программы
            break
        elif result == "exists":
            print(f"Ошибка: Задача с названием '{name_of_new_task}' уже существует.")
            close_noty = driver.find_element(By.XPATH, "//div[@class='noty_close']")  # noty_close
            close_noty.click()
            name_of_newReglTask = driver.find_element(By.XPATH, "//input[@placeholder='Название регламента']")
            name_of_newReglTask.click()
            name_of_newReglTask.clear()
            counter += 1
        else:
            # print("Уведомление не найдено.")
            driver.quit()
            break
    except TimeoutException:
        print("Ошибка: Время ожидания истекло.")
        driver.quit()
        break
    except Exception as e:
        print(Fore.RED + f"Произошла ошибка: {e}")
        driver.quit()
        break
else:
    print(Fore.RED + "Достигнуто максимальное количество попыток. Тест не может быть завершен.")

# test number 45 (ipe-45: Редактирование регламента задачи)

edit_new_reg_task = driver.find_element(By.XPATH, "(//h3[normalize-space()='autotest_new_task1 [test_sofa]'])[1]")
edit_new_reg_task.click()

try:
    wait_editorTask = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Создание регламента задач')]")))
    print(Fore.GREEN + "Страница с редактированием регламента задачи открыта")
except TimeoutException:
    print(Fore.RED + "Страница с редактированием регламента задачи не открыта")
    driver.quit()

edit_groups_reg_task = driver.find_element(By.XPATH,
                                           "//span[contains(text(),'Группа 1, Группа 2, Группа 3, Группа 4, Группа 5')]")
edit_groups_reg_task.click()

try:
    wait_for_groups_EDIT = WebDriverWait(driver, 60).until(
        EC.element_to_be_clickable((By.XPATH, "//span[@class='mat-option-text'][contains(text(),'Группа 5')]")))
    remove_groups_reg_task1 = driver.find_element(By.XPATH,
                                                  "//span[@class='mat-option-text'][contains(text(),'Группа 5')]")
    remove_groups_reg_task1.click()

    remove_groups_reg_task2 = driver.find_element(By.XPATH,
                                                  "//span[@class='mat-option-text'][contains(text(),'Группа 4')]")
    remove_groups_reg_task2.click()
except TimeoutException:
    print("Не смог изменить группы в Регламенте задач")
    driver.quit()

# клик escape - чтобы выйти из выпадающего списка
webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
# кажется незаменимо))
time.sleep(0.5)

choose_category_task = driver.find_element(By.XPATH, "//span[contains(text(),'Биологическая опасность')]")
choose_category_task.click()

try:
    wait_for_category_TASK = WebDriverWait(driver, 60).until(
        EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Коллапс')]")))
    choose_new_category_task = driver.find_element(By.XPATH, "//span[contains(text(),'Коллапс')]")
    choose_new_category_task.click()
except TimeoutException:
    print("Не смог изменить Категорию в Регламенте задач")
    driver.quit()


# изменение поля у регламента задач
def rename_nameOfTask():
    try:
        WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Название регламента']")))
        name_of_new_reg_task = driver.find_element(By.XPATH, "//input[@placeholder='Название регламента']")
        name_of_new_reg_task.click()
        name_of_new_reg_task.clear()
        name_of_new_reg_task.send_keys(edited_name_task)
    except TimeoutException:
        print("Не смог нажать на инпут с названием регламента задачи")
        driver.quit()
    try:
        WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Сохранить')]")))
        save_new_reglament = driver.find_element(By.XPATH, "//span[contains(text(),'Сохранить')]")
        save_new_reglament.click()
        time.sleep(1)  # тоже хз что делать с этим
    except TimeoutException:
        print("Не смог нажать на кнопку сохранения регламента")
        driver.quit()


def check_notifications():
    try:
        notification = driver.find_element(By.XPATH, "//div[@class='noty_message']")
        message = notification.text
        if message == "Данные успешно сохранены":
            return "success"
        elif message == "Регламент с таким названием уже существует!":
            return "exists"
        else:
            return "unknown"
    except NoSuchElementException:
        return "not_found"


counter = 1
max_attempts = 10

while counter <= max_attempts:
    try:
        edited_name_task = f"{edited_name_task}{counter}"
        rename_nameOfTask()
        result = check_notifications()
        if result == "success":
            print(f"Задача с названием '{edited_name_task}' успешно добавлена.")
            try:
                notification = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, "//div[@class='noty_message']")))
                # Ожидание, пока уведомление исчезнет
                while True:
                    try:
                        notification.is_displayed()  # Проверяем, видим ли элемент
                        print(Fore.GREEN + "Уведомление 'Данные успешно сохранены' появилось")
                        print(Fore.BLUE + "Test case 'ipe-45  Редактирование регламента задачи' - ПРОЙДЕНО")
                    except:
                        break  # Если элемент не видим, выходим из цикла
                    time.sleep(1)  # Если элемент видим, ждем 1 секунду и повторяем проверку
            except:
                pass  # Если элемент не найден, продолжаем выполнение программы
            break
        elif result == "exists":
            print(f"Ошибка: Задача с названием '{edited_name_reglament}' уже существует.")
            close_noty = driver.find_element(By.XPATH, "//div[@class='noty_close']")  # noty_close
            close_noty.click()
            edited_name_reg = driver.find_element(By.XPATH, "//input[@placeholder='Название регламента']")
            edited_name_reg.click()
            edited_name_reg.clear()
            counter += 1
        else:
            # print("Уведомление не найдено.")
            # VERY IMPORTANT: пока прописан PASS - т.к не появляется уведомление при редактировании - есть задача, заменить после фикса задачи
            pass
            break
    except TimeoutException:
        print("Ошибка: Время ожидания истекло.")
        driver.quit()
        break
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        driver.quit()
        break
else:
    print("Достигнуто максимальное количество попыток. Тест не может быть завершен.")

try:
    homepage_button = WebDriverWait(driver, 60).until(
        EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Журнал событий')]")))
    go_to_mainpage = driver.find_element(By.XPATH, "//span[contains(text(),'Журнал событий')]")
    go_to_mainpage.click()
except TimeoutException:
    print(Fore.RED + "Кнопка для перехода на главную страницу недоступна/переход не произошел")
    driver.quit()

try:
    add_new_incident = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Добавить инцидент')]")))
    add_new_incident.click()
    print(Fore.GREEN + "Перешел на основную страницу")
except TimeoutException:
    print("Не перешел на основную страницу, не открыл страницу 'Добавить инцидент' ")
    driver.quit()

try:
    wait_add_new_incident = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Информация о происшествии')]")))
    print(Fore.GREEN + "Открыл страницу 'Добавить инцидент'")
except TimeoutException:
    print(Fore.RED + "Не открыл страницу 'Добавить инцидент'")
    driver.quit()

try:
    wait_dropdown_typeIncident = WebDriverWait(driver, 60).until(
        EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='edited_autotest1']")))
    choose_type_of_new_incident = driver.find_element(By.XPATH, "//span[normalize-space()='edited_autotest1']")
    choose_type_of_new_incident.click()
    print(Fore.GREEN + "Открыл страницу для добавления нового инцидента и выбрал регламент")
except TimeoutException:
    print(Fore.RED + "Не смог выбрать тип происшествия")
    driver.quit()

click_on_plus_incident = driver.find_element(By.XPATH, "//mat-icon[normalize-space()='add']")
click_on_plus_incident.click()

try:
    wait_window_with_incident = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.XPATH, "//mat-icon[normalize-space()='refresh']")))
    print(Fore.GREEN + "Добавил новый инцидент, открылся блок 1")

except TimeoutException:
    print(Fore.RED + "Не добавил новый инцидент")
    driver.quit()

try:
    noty_message_check = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.XPATH, "//div[@class='noty_message']")))
    print(Fore.GREEN + "Уведомление 'Данные успешно сохранены' появилось")
    print(Fore.BLUE + "Test case 'ipe-46  Добавление инцидента' - ПРОЙДЕНО")
    close_noty = driver.find_element(By.XPATH, "//div[@class='noty_close']")  # noty_close
    close_noty.click()
    try:
        notification = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='noty_message']")))
        while True:
            try:
                notification.is_displayed()
            except:
                break
    except:
        pass
except TimeoutException:
    print(Fore.RED + "Уведомление 'Данные успешно сохранены' не появилось")
    driver.quit()

# заявка на ТО
go_to_mainpage = driver.find_element(By.XPATH, "//span[contains(text(),'Журнал событий')]")
go_to_mainpage.click()

try:
    request_for_TO = WebDriverWait(driver, 60).until(
        EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Заявка на ТО')]")))
    request_for_TO.click()
    print(Fore.GREEN + "Перешел на основную страницу")
except TimeoutException:
    print(Fore.RED + "Не перешел на основную страницу, не открыл страницу 'Заявка на ТО' ")
    driver.quit()

try:
    wait_add_new_request_for_TO = WebDriverWait(driver, 60).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='ФИО заявителя']")))
    print(Fore.GREEN + "Открыл страницу 'Заявка на ТО'")
    time.sleep(delay)
except TimeoutException:
    print(Fore.RED + "Не открыл страницу 'Заявка на ТО'")
    driver.quit()

input_fio = driver.find_element(By.XPATH, "//input[@placeholder='ФИО заявителя']")
input_fio.send_keys(task_fio)

input_phone = driver.find_element(By.XPATH, "//input[@placeholder='Тел. номер заявителя']")
input_phone.send_keys(task_phone)

input_address = driver.find_element(By.XPATH, "//input[@placeholder='Адрес заявителя']")
input_address.send_keys(task_address)

input_language = driver.find_element(By.XPATH, "//input[@placeholder='Язык заявителя']")
input_language.send_keys(task_language)

try:
    WebDriverWait(driver, 60).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@aria-hidden='true']//div//span[contains(text(),'Тип задачи')]")))
    open_type_of_new_task = driver.find_element(By.XPATH,
                                                "//div[@aria-hidden='true']//div//span[contains(text(),'Тип задачи')]")
    open_type_of_new_task.click()
except TimeoutException:
    print(Fore.RED + "Не смог открыть выпадающий список 'Тип задачи'")
    driver.quit()

try:
    WebDriverWait(driver, 60).until(
        EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='edited_autotest_task1']")))
    choose_type_of_new_task = driver.find_element(By.XPATH, "//span[normalize-space()='edited_autotest_task1']")
    choose_type_of_new_task.click()
except TimeoutException:
    print(Fore.RED + "Не смог выбрать элемент в 'Тип задачи'")
    driver.quit()

try:
    choose_performers = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Исполнители']")))
    choose_performers.click()
except TimeoutException:
    driver.quit()

try:
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, "//div[normalize-space()='admin']")))
    choose_performers_checkbox = driver.find_element(By.XPATH,
                                                     "//body/div/div[@dir='ltr']/div/div[@role='listbox']/mat-option[1]/span[1]")
    choose_performers_checkbox.click()
except TimeoutException:
    print(Fore.RED + "Не смог прокликать поле 'Исполнители'")
    driver.quit()

webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
time.sleep(0.5)

# //mat-icon[normalize-space()='clear'] - кнопка для скрытия этого уведомления

# оффтоп - есть оранжевое уведомление, если открыты два одинаковых юзера и происходят какие-то изменения,
# из-за этого тест падает в разные моменты времени(точно в 'Заявка на ТО', редактирование регламента инцидента) -
# не уверен, что целесообразно писать в каждом разделе проверки на наличие этого окна, будет запрос - попытаюсь реализовать

# что-то похожее, на реализацию этого
# try:
#     orange_notification = WebDriverWait(driver,2).until(EC.presence_of_element_located((By.XPATH, "//mat-icon[normalize-space()='clear']")))
#
#     try:
#         close_button = orange_notification.find_element(By.XPATH, "//mat-icon[normalize-space()='clear']")
#         close_button.click()
#     except NoSuchElementException:
#         pass
# except TimeoutException:
#     pass
try:
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Сохранить')]")))
    save_new_request_TO = driver.find_element(By.XPATH, "//span[contains(text(),'Сохранить')]")
    save_new_request_TO.click()
except TimeoutException:
    driver.quit()

try:
    noty_message_check = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.XPATH, "//div[@class='noty_message']")))
    print(Fore.GREEN + "Уведомление 'Данные успешно сохранены' появилось")
    print(Fore.BLUE + "Test case 'ipe-47  Добавление задачи' - ПРОЙДЕНО")
    close_noty = driver.find_element(By.XPATH, "//div[@class='noty_close']")  # noty_close
    time.sleep(3)
except TimeoutException:
    print(Fore.RED + "Уведомление 'Данные успешно сохранены' не появилось")
    driver.quit()

try:
    open_incident = WebDriverWait(driver, 60).until(
        EC.element_to_be_clickable((By.XPATH, "(//mat-cell[contains(text(),'Массовые беспорядки')])[1]")))
    action.double_click(open_incident).perform()
except TimeoutException:
    driver.quit()

try:
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, "//mat-icon[normalize-space()='refresh']")))
except TimeoutException:
    driver.quit()

try:
    WebDriverWait(driver, 60).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Координаты инцидента']")))
    # добавление координат инциденту
    add_coordinates = driver.find_element(By.XPATH, "//input[@placeholder='Координаты инцидента']")
    add_coordinates.click()
    add_coordinates.clear()
    add_coordinates.send_keys(coordinates)
    print(Fore.BLUE + "У инцидента edited_autotest1 указал координаты 53.228425 50.199929")
except TimeoutException:
    driver.quit()

back_to_main_page = driver.find_element(By.XPATH, "//mat-icon[normalize-space()='home']")
back_to_main_page.click()

try:
    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, "//h3[contains(text(),'Все события')]")))
    print(Fore.GREEN + "Открыл главную страницу")
except TimeoutException:
    print(Fore.RED + "Не открыл главную страницу")
    driver.quit()

# проверка координат
try:
    open_incident = WebDriverWait(driver, 60).until(
        EC.element_to_be_clickable((By.XPATH, "(//mat-cell[contains(text(),'Массовые беспорядки')])[1]")))
    action.double_click(open_incident).perform()
except TimeoutException:
    driver.quit()

try:
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, "//mat-icon[normalize-space()='refresh']")))
    print(Fore.GREEN + "Открыл инцидент edited_autotest1")
except TimeoutException:
    driver.quit()
    print(Fore.RED + "Не открыл инцидент edited_autotest1")

try:
    add_coordinates = WebDriverWait(driver, 60).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Координаты инцидента']")))
    value_in_field = add_coordinates.get_attribute("value")
    expected_value = coordinates

    if value_in_field == expected_value:
        print(Fore.GREEN + "Координаты сохранились")
        print(Fore.BLUE + "ipe-48: Установка координат инциденту - ПРОЙДЕНО")
        print(value_in_field + " -  Координаты в карточке инцидента")
    else:
        print(Fore.RED + "Координаты не сохранились")
        driver.quit()
except TimeoutException:
    driver.quit()

# перелет к координатам пока не реализован в тонком клиенте - пока закоментил
# go_home = driver.find_element(By.XPATH,"//mat-icon[normalize-space()='home']")
# go_home.click()
#
# try:
#     go_home_wait = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, "//ul[@class='filter-menu']")))
#     time.sleep(2)
# #ожидание прогрузки основной страницы
#     print(Fore.GREEN + "Перешел на основную страницу")
# except TimeoutException:
#     print(Fore.RED + "Не перешел на основную страницу")
#     driver.quit()
#
# fly_to_coordinates = driver.find_element(By.XPATH, "(//mat-cell[contains(text(),'Массовые беспорядки')])[1]")
# fly_to_coordinates.click()
#     #popup id
# try:
#     popup_wait = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.ID, "popup-content")))
#     time.sleep(2)
#     #ожидание появление попапа
#     print(Fore.GREEN + "Перелет к координатам произошел")
# except TimeoutException:
#     print(Fore.RED + "Перелет к координатам не произошел")
#     driver.quit()
