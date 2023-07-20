import time  # для юзания дилея при открытии вебокон
from selenium.webdriver.common.by import By  # для поиска by
from selenium.webdriver import Keys
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from information import serenity, login, password, firefly, task_fio, task_phone, task_address, task_language, \
    coordinates, question_text, new_name_reglament, new_name_question, name_of_new_reglament, name_of_new_task, \
    edited_name_task
from colorama import init, Fore, Back, Style
from selenium.common.exceptions import NoSuchElementException

#   test number 41 (ipe-41: Открытие приложения)


delay = 1

driver = (webdriver.Chrome())
driver.get('http://192.168.10.237:7000/index3D.html')
chrome_options = Options()
chrome_options.add_argument("--disable-extensions")
driver.maximize_window()
time.sleep(delay)

# web_ipe = driver.find_element(By.ID, "planet-earth-app")
# web_ipe.click()


settings_log_form = driver.find_element(By.ID, 'settingsButton').click()  # клик на кнопку настроек

input_ipaddr = driver.find_element(By.ID, 'ip_address')  # заполнение поля айпи адрес
input_ipaddr.click()

input_ipaddr.send_keys(serenity)

input_login = driver.find_element(By.ID, 'id_username')  # заполнение поля логин
input_login.click()

input_login.send_keys(login)

input_password = driver.find_element(By.ID, 'id_password')  # заполнение поля пароль
input_password.click()
input_password.send_keys(password)

input_password.send_keys(Keys.RETURN)

try:
    input_firefly_wait = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'firefly')))
    input_firefly = driver.find_element(By.ID, 'firefly')  # заполнение поля фф + проверка
    input_firefly.click()
    input_firefly.send_keys(firefly)
    input_firefly.send_keys(Keys.RETURN)
except TimeoutException:
    print(Fore.RED + "Авторизация не произошла")
    driver.quit()

try:
    entry_mngr_incident = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'loginDiv')))
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

# поиск и клик на выпадающий список слева на панели НЕ РАБОТАЕТ))
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

# проверка что окно планеты открылось
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

# поиск и переключение на iframe с менеджером происшествий + изменение размера менеджера проишествий

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
time.sleep(delay)

try:
    main_page_wait = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.ID, "drop-editors")))
    # ожидание прогрузки главной страницы 60 секунд, если грузит раньше = выполняется дальше, не выполняется = выводит сообщ
    print(Fore.BLUE + "Test case 'ipe-41: Открытие приложения' -  ПРОЙДЕНО")
except TimeoutException:
    print(Fore.RED + "x")
    driver.quit()

    # test number 42 (ipe-42: Добавление регламента инцидента)

# добавить отдельную авторизацию после реализации тест кейса

settings_main_form = driver.find_element(By.XPATH,
                                         "//button[@id='drop-editors']//span[@class='mat-button-wrapper']")  # клик на шестеренку
settings_main_form.click()
time.sleep(delay)

if settings_main_form.is_displayed():
    print(Fore.GREEN + "Открыл доступные редакторы")
else:
    driver.quit()
    print(Fore.RED + "Открытие не произошло, проверить доступность кнопки")

editor_reglament = driver.find_element(By.XPATH, "//span[contains(text(),'Редактор регламентов инцидентов')]")
editor_reglament.click()

#
new_reg_editor_main_page = driver.find_element(By.XPATH, "//span[contains(text(),'Регламенты инцидентов')]")
if new_reg_editor_main_page.text == "Регламенты инцидентов":

    print(Fore.GREEN + "Страница с регламентами инцидентов открыта")
else:
    print(Fore.RED + "Страница со всеми регламентами инцидентов не открыта")
    driver.quit()


add_new_regl = driver.find_element(By.XPATH, "//span[contains(text(),'Добавить регламент')]")  # клик на кнопку "Добавить регламент"
add_new_regl.click()
time.sleep(delay)

new_reg_editor_page = driver.find_element(By.XPATH,"//div[@class='f-r-q-card f-r-q-editor ng-star-inserted']//div[1]")
if new_reg_editor_page.text == "Редактор вопросов":
    print(Fore.GREEN + "Страница с добавлением нового регламента инцидента открыта")
else:
    print(Fore.RED + "Страница с добавлением нового регламента инцидента не открыта")
    driver.quit()

type_of_incident = driver.find_element(By.XPATH, "//img[@src='assets/img/icons/unknown.png']")
time.sleep(1.5)
type_of_incident.click()
time.sleep(1.5)
modal_typeIncident = driver.find_element(By.XPATH, "//mat-dialog-container[@aria-modal='true']")

if modal_typeIncident.is_displayed():
    print(Fore.GREEN + "Окно с выбором категории регламента открыто")
else:
    print(Fore.RED + "Окно с выбором категории регламента не открыто")
    driver.quit()

choose_type_of_incident = driver.find_element(By.XPATH, "//img[@src='assets/img/icons/riots.png']")
time.sleep(1.5)
choose_type_of_incident.click()

save_type_of_incident = driver.find_element(By.XPATH, "//button[@type='button']//span[@class='mat-button-wrapper'][contains(text(),'Сохранить')]")
save_type_of_incident.click()
time.sleep(delay)


def fill_required_fields(task_name):
    name_of_new_reg = driver.find_element(By.XPATH, "//input[@placeholder='Название регламента']")
    name_of_new_reg.click()
    name_of_new_reg.clear()
    name_of_new_reg.send_keys(task_name)
    time.sleep(1.5)
    save_new_reglament = driver.find_element(By.XPATH, "//span[contains(text(),'Сохранить регламент')]")
    time.sleep(1.5)
    save_new_reglament.click()
    time.sleep(1)


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
max_attempts = 5
task_name = "Новая задача"
while counter <= max_attempts:
    try:
        task_name = f"Название задачи {counter}"
        fill_required_fields(task_name)
        result = check_notifications()
        if result == "success":
            print(f"Задача с названием '{task_name}' успешно добавлена и отредактирована.")
            break
        elif result == "exists":
            print(f"Ошибка: Задача с названием '{task_name}' уже существует.")
            counter += 1
        else:
            print("Неожиданное уведомление или уведомление не найдено.")
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