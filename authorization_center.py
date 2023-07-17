import time  # для юзания дилея при открытии вебокон
from selenium.webdriver.common.by import By  # для поиска by
from selenium.webdriver import Keys
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from information import serenity,center_login,center_pass,firefly,new_user_login,new_user_pass,new_user_lastname,new_user_name,new_user_patronymic,edited_user_login,edited_user_pass,edited_user_name,edited_user_lastname,edited_user_patronymic,center_ff_login,center_ff_pass
from colorama import init, Fore, Back, Style


                             #   test number ipe-1378 :: Версия: 1 :: Открытие приложения


delay = 1 #пока что на всякий случай как костыль в некоторых шагах
delay = 2
driver = (webdriver.Chrome())
driver.get('http://192.168.10.237:7000/SerenityNew/#/')
chrome_options = Options()
chrome_options.add_argument("--disable-extensions")
driver.maximize_window()
time.sleep(delay)




settings_log_form = driver.find_element(By.ID, 'settingsButton').click()  # клик на кнопку настроек


input_ipaddr = driver.find_element(By.ID, 'ip_address')  # заполнение поля айпи адрес
input_ipaddr.click()

input_ipaddr.send_keys(serenity)


input_login = driver.find_element(By.ID, 'id_username')  # заполнение поля логин
input_login.click()

input_login.send_keys(center_login)


input_password = driver.find_element(By.ID, 'id_password')  # заполнение поля пароль
input_password.click()
input_password.send_keys(center_pass)

input_password.send_keys(Keys.RETURN)


# log_in_authorization = driver.find_element(By.ID, 'loginDiv')
# log_in_authorization.click()



                                         #ipe-1380:Создание нового пользователя
try:
    wait_main_page = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//div[@class='card-container']")))
    print(Fore.GREEN + "Авторизация произошла успешно")
    print(Fore.BLUE + "ipe - 1378: Открытие приложения - ПРОЙДЕНО")
except TimeoutException:
    print(Fore.RED + "Авторизация не произошла")

#клик на "+" для открытия модального окна
add_new_user = driver.find_element(By.XPATH, "//button[@id='crt-user-btn']")
add_new_user.click()

#ожидание открытия модального окна с данными для заполнения для нового юзера
try:
    new_user_popup_wait = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//body/app-root/div/app-dashboard/app-editor-users/div/div/div/div/mat-card[1]/div[1]")))
    print(Fore.GREEN + "Открыл окно с добавлением данных о новом юзере")

except TimeoutException:
    print(Fore.RED + "Окно с добавлением данных о новом юзере не открылось")
    driver.quit()


#заполнение полей логин+пароль+ФИО
input_user_login = driver.find_element(By.XPATH, "//input[@id='userName']")
input_user_login.send_keys(new_user_login)
input_user_pass = driver.find_element(By.XPATH, "//input[@id='userPass']")
input_user_pass.send_keys(new_user_pass)
input_user_lastname = driver.find_element(By.XPATH, "//input[@placeholder='Фамилия']")
input_user_lastname.send_keys(new_user_lastname)
input_user_lastname = driver.find_element(By.XPATH, "//input[@placeholder='Имя']")
input_user_lastname.send_keys(new_user_name)
input_user_lastname = driver.find_element(By.XPATH, "//input[@placeholder='Отчество']")
input_user_lastname.send_keys(new_user_patronymic)



#открытие выпадающего списка с ролями
dropdown_new_role = driver.find_element(By.XPATH, "//mat-select[@id='userRole']")
dropdown_new_role.click()

#ожидание открытия выпадающего списка
try:
    wait_dropdown_role = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//div[@class='cdk-overlay-pane']")))
    print(Fore.GREEN + "Выпадающий список с ролями открылся")
#    time.sleep(0.7)
except TimeoutException:
    print(Fore.RED + "Выпадающий список с ролями не открылся")
    driver.quit()

#ожидание пока кнопка админ станет доступной
try:
    wait_new_role = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Admin']")))
    choose_new_role = driver.find_element(By.XPATH, "//span[normalize-space()='Admin']")
    choose_new_role.click()
except TimeoutException:
    driver.quit()

#чекбокс на мультилогин
checkbox_multilogin = driver.find_element(By.XPATH, "//div[@class='mat-checkbox-inner-container mat-checkbox-inner-container-no-side-margin']")
checkbox_multilogin.click()

#сохранению юзера
save_new_user = driver.find_element(By.XPATH, "//span[contains(text(),'Сохранить')]")
save_new_user.click()

#проверка на появление уведомления после создания + его закрытия, для прохождения дальнейших тестов
try:
    noty_message = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH,"//snack-bar-container[@role='alert']")))
    print(Fore.BLUE + "ipe-1380:Создание нового пользователя - ПРОЙДЕН")
    close_noty = driver.find_element(By.XPATH, "//button[contains(text(),'Закрыть')]")
    close_noty.click()
except TimeoutException:
    print(Fore.RED + "Пользователь не создался / Не появилось уведомление")


amount_of_users = driver.find_element(By.XPATH, "//div[@class='mat-select-arrow-wrapper']")
amount_of_users.click()
#
try:
    wait_amount_of_users = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//div[@class='mat-select-content ng-trigger ng-trigger-fadeInContent']")))
    print(Fore.GREEN + "Увеличил кол-во отображаемых юзеров на странице до 100")
    increase_users = driver.find_element(By.XPATH, "//span[normalize-space()='100']")
    increase_users.click()
except TimeoutException:
    print(Fore.RED + "Выпадающий список с количество юзеров на странице не открылся")
    driver.quit()

#надо понять как искать по нескольким локаторам, то есть find.element ilya_autotest --> клик на редактировать, пока не нашел инфу
dropdown_edit_user = driver.find_element(By.XPATH, "//body[1]/app-root[1]/div[2]/app-dashboard[1]/app-editor-users[1]/div[1]/div[2]/div[1]/div[1]/mat-card[1]/div[1]/div[3]/button[1]/span[1]/mat-icon[1]")
dropdown_edit_user.click()

#ожидание прогрузки выпадающего списка с редактированием информации о юзере
try:
    wait_dropdown_editors = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//div[@class='mat-menu-content ng-trigger ng-trigger-fadeInItems']")))
    print(Fore.GREEN + "Открыл выпадающий список для редактирования юзера")
except TimeoutException:
    print(Fore.RED + "Не открыл выпадающий список для редактирования юзера")
    driver.quit()

#ожидание пока "Редактировать" станет доступной
try:
    edit_wait = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Редактировать')]")))
    time.sleep(0.75)
    edit_button = driver.find_element(By.XPATH, "//span[contains(text(),'Редактировать')]")
    edit_button.click()
except TimeoutException:
    print(Fore.RED + "Не смог выбрать из выпадающего списка кнопку 'Редактировать'")
    driver.quit()

#edit_new_user_info = driver.find_element(By.XPATH, "//span[contains(text(),'Редактировать')]")
#edit_new_user_info.click()


#ожидание открытия модального окна с данными для заполнения для нового юзера
try:
    new_user_popup_wait = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//body//app-root//app-editor-users//mat-card[1]")))
    print(Fore.GREEN + "Открыл окно с добавлением данных о новом юзере")
except TimeoutException:
    print(Fore.RED + "Окно с добавлением данных о новом юзере не открылось")
    driver.quit()

edit_user_login = driver.find_element(By.XPATH, "//input[@id='userName']")
edit_user_login.clear()
edit_user_login.send_keys(edited_user_login)

edit_user_pass = driver.find_element(By.XPATH, "//input[@id='userPass']")
edit_user_pass.clear()
edit_user_pass.send_keys(edited_user_pass)

edit_user_lastname = driver.find_element(By.XPATH, "//input[@placeholder='Фамилия']")
edit_user_lastname.clear()
edit_user_lastname.send_keys(edited_user_lastname)

edit_user_name = driver.find_element(By.XPATH, "//input[@placeholder='Имя']")
edit_user_name.clear()
edit_user_name.send_keys(edited_user_name)

edit_user_name = driver.find_element(By.XPATH, "//input[@placeholder='Отчество']")
edit_user_name.clear()
edit_user_name.send_keys(edited_user_patronymic)


#ожидание открытия выпадающего списка
try:
    wait_dropdown_role = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//div[@class='cdk-overlay-pane']")))
    print(Fore.GREEN + "Выпадающий список с ролями открылся")
#    time.sleep(0.7)
except TimeoutException:
    print(Fore.RED + "Выпадающий список с ролями не открылся")
    driver.quit()



#открытие выпадающего списка с ролями
dropdown_new_role = driver.find_element(By.XPATH, "//mat-select[@id='userRole']")
dropdown_new_role.click()

#ожидание пока кнопка админ станет доступной
try:
    wait_new_role = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Admin']")))
    choose_new_role = driver.find_element(By.XPATH, "//span[normalize-space()='Admin']")
    choose_new_role.click()
except TimeoutException:
    driver.quit()



save_new_info = driver.find_element(By.XPATH, "//span[contains(text(),'Сохранить')]")
save_new_info.click()

#проверка на появление уведомления после создания + его закрытия, для прохождения дальнейших тестов
try:
    noty_message = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH,"//snack-bar-container[@role='alert']")))
    print(Fore.BLUE + "ipe-1381 Редактирование данных пользователя - ПРОЙДЕН")
    close_noty = driver.find_element(By.XPATH, "//button[contains(text(),'Закрыть')]")
    close_noty.click()
except TimeoutException:
    print(Fore.RED + "Изменения не сохранились / Не появилось уведомление")



dropdown_edit_user = driver.find_element(By.XPATH, "//body[1]/app-root[1]/div[2]/app-dashboard[1]/app-editor-users[1]/div[1]/div[2]/div[1]/div[1]/mat-card[1]/div[1]/div[3]/button[1]/span[1]/mat-icon[1]")
dropdown_edit_user.click()

#ожидание прогрузки выпадающего списка с редактированием информации о юзере
try:
    wait_dropdown_editors = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//div[@class='mat-menu-content ng-trigger ng-trigger-fadeInItems']")))
    print(Fore.GREEN + "Открыл выпадающий список для редактирования юзера")
except TimeoutException:
    print(Fore.RED + "Не открыл выпадающий список для редактирования юзера")
    driver.quit()

#ожидание пока "Редактировать" станет доступной
try:
    edit_wait = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Редактировать')]")))
    time.sleep(0.75)
    edit_button = driver.find_element(By.XPATH, "//span[contains(text(),'Удалить')]")
    edit_button.click()
except TimeoutException:
    print(Fore.RED + "Не смог выбрать из выпадающего списка кнопку 'Удалить'")
    driver.quit()

#подтверждение на удаление юзера
try:
    warning_message = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//app-dialog[@class='ng-star-inserted']")))
    print(Fore.GREEN + "Предупреждение 'Удаление пользователя. Подтвердите удаление пользователя ... появилось'")
    time.sleep(0.5)
except TimeoutException:
    print(Fore.RED + "Предупреждение при удалении не появилось")
    driver.quit()

#подтверждение удаления
accept_delete_user = driver.find_element(By.XPATH, "//span[contains(text(),'Подтвердить')]")
accept_delete_user.click()

#проверка на уведомление
try:
    noty_message = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH,"//snack-bar-container[@role='alert']")))
    print(Fore.BLUE + "ipe-1382 Удаление пользователя - ПРОЙДЕН")
    close_noty = driver.find_element(By.XPATH, "//button[contains(text(),'Закрыть')]")
    close_noty.click()
except TimeoutException:
    print(Fore.RED + "Удаление не произошло / Не появилось уведомление")

#f5
driver.refresh()


try:
    auth_wait = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//input[@id='id_username']")))
    print(Fore.GREEN + "Страница перезапустилась, открыто окно с авторизацией")

except TimeoutException:
    print(Fore.RED + "Страница не перезапустилась / Окно авторизации не открылось")
    driver.quit()

#релогин под фф

try:
    wait_settings_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@title='Включить настройку подключений']")))
except TimeoutException:
    print("Не смог нажать на шестеренку")
    driver.quit()


#пока что закоментил, т.к хз надо или нет

#input_ipaddr = driver.find_element(By.ID, 'ip_address')  # заполнение поля айпи адрес
#input_ipaddr.click()

#input_ipaddr.send_keys(serenity)


input_login = driver.find_element(By.ID, 'id_username')  # заполнение поля логин
input_login.click()

input_login.send_keys(center_ff_login)


input_password = driver.find_element(By.ID, 'id_password')  # заполнение поля пароль
input_password.click()
input_password.send_keys(center_ff_pass)

input_password.send_keys(Keys.RETURN)

#ожидание прогрузки страницы под фф

try:
    wait_ff_page = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//mat-card-title[contains(text(),'Роли')]")))
    print(Fore.GREEN + "Авторизовался под firefly/firefly")
except TimeoutException:
    print(Fore.RED + "Не авторизовался под firefly/firefly")
    driver.quit()

dropdown_edit_user = driver.find_element(By.XPATH, "//body[1]/app-root[1]/div[2]/app-dashboard[1]/app-editor-users[1]/div[1]/div[2]/div[1]/div[1]/mat-card[1]/div[1]/div[3]/button[1]/span[1]/mat-icon[1]")
dropdown_edit_user.click()

#ожидание прогрузки выпадающего списка с редактированием информации о юзере
try:
    wait_dropdown_editors = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//div[@class='mat-menu-content ng-trigger ng-trigger-fadeInItems']")))
    print(Fore.GREEN + "Открыл выпадающий список для редактирования юзера")
except TimeoutException:
    print(Fore.RED + "Не открыл выпадающий список для редактирования юзера")
    driver.quit()

#ожидание пока "Редактировать" станет доступной
try:
    edit_wait = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Менеджер ролей')]")))
    time.sleep(0.75)
    edit_button = driver.find_element(By.XPATH, "//span[contains(text(),'Менеджер ролей')]")
    edit_button.click()
    print(Fore.GREEN + "Нажал на 'Менеджер ролей'")
except TimeoutException:
    print(Fore.RED + "Не смог выбрать из выпадающего списка кнопку 'Менеджер ролей'")
    driver.quit()


choose_mng_role = driver.find_element(By.XPATH, "//span[normalize-space()='AllReadRole']")
choose_mng_role.click()

time.sleep(0.5) #добавить проверку..

save_mng_role = driver.find_element(By.XPATH, "//span[contains(text(),'Сохранить')]")
save_mng_role.click()

#проверка на появление уведомления после создания + его закрытия, для прохождения дальнейших тестов
try:
    noty_message = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH,"//snack-bar-container[@role='alert']")))
    print(Fore.BLUE + "ipe-1383:Добавление роли пользователю - ПРОЙДЕН")
    close_noty = driver.find_element(By.XPATH, "//button[contains(text(),'Закрыть')]")
    close_noty.click()
except TimeoutException:
    print(Fore.RED + "Роль не изменилась/ Не появилось уведомление")



time.sleep(2)