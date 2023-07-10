import time  # для юзания дилея при открытии вебокон
from selenium.webdriver.common.by import By  # для поиска by
from selenium.webdriver import Keys
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from information import serenity,login,password,firefly,task_fio,task_phone,task_address,task_language
from colorama import init, Fore, Back, Style

                             #   test number 41 (ipe-41: Открытие приложения)

delay = 1

driver = (webdriver.Chrome())
driver.get('http://192.168.10.237:7000/index3D.html')

driver.maximize_window()
time.sleep(delay)

#web_ipe = driver.find_element(By.ID, "planet-earth-app")
#web_ipe.click()



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

time.sleep(2)

#проверка где я нахожусь, ищу по левой панели
try:
    main_page_waiting = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, "//div[@id='main-sidenav']")))
    time.sleep(delay)
    print(Fore.GREEN + "Планета открылась")
except TimeoutException:
    print(Fore.RED + "Планета не открылась")
    driver.quit()

#поиск и клик на выпадающий список слева на панели
time.sleep(3)
drop_down_list = driver.find_element(By.XPATH, "//div[@id='sidenav-toggle']")
drop_down_list.click()

#ожидание на доступность кнопки с планетой, требуется, если планета закрыта
try:
    options_wait = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.ID, "sidenav-menu-planet")))
    print(Fore.GREEN + "Открыл выпадающий список в Интегра-4д")
except TimeoutException:
    print(Fore.RED + "Не открыл выпадающий список в Интегра-4Д")
    driver.quit()
time.sleep(3)
#открытие менеджера происшествий
mngr_open_window = driver.find_element(By.XPATH, "//a[@id='sidenav-menu-cardevent']")
mngr_open_window.click()
time.sleep(3)
#поиск и переключение на iframe с менеджером происшествий
iframe_cardevent = driver.find_element(By.XPATH, "//iframe[@class='nodrag']")
driver.switch_to.frame(iframe_cardevent)


time.sleep(13)
# script = ""
# driver.execute_script(script)

time.sleep(3)