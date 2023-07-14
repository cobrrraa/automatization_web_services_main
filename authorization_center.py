import time  # для юзания дилея при открытии вебокон
from selenium.webdriver.common.by import By  # для поиска by
from selenium.webdriver import Keys
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from information import serenity,center_login,center_pass,firefly,new_user_login,new_user_pass
from colorama import init, Fore, Back, Style


                             #   test number ipe-1378 :: Версия: 1 :: Открытие приложения


delay = 1 #пока что на всякий случай как костыль в некоторых шагах

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

wait_main_page = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@class='card-container']")))

add_new_user = driver.find_element(By.XPATH, "//button[@id='crt-user-btn']")
add_new_user.click()

#заполнение полей для нового юзера
try:
    new_user_popup_wait = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//body/app-root/div/app-dashboard/app-editor-users/div/div/div/div/mat-card[1]/div[1]")))
    input_user_login = driver.find_element(By.XPATH, "//input[@id='userName']")
    input_user_login.send_keys(new_user_login)
    input_user_pass = driver.find_element(By.XPATH, "//input[@id='userPass']")
    input_user_pass.send_keys(new_user_pass)

    dropdown_new_role = driver.find_element(By.XPATH, "//mat-select[@id='userRole']")
    dropdown_new_role.click()

    time.sleep(delay)

    choose_new_role = driver.find_element(By.XPATH, "//span[normalize-space()='Admin']")
    choose_new_role.click()

    checkbox_multilogin = driver.find_element(By.XPATH, "//div[@class='mat-checkbox-inner-container mat-checkbox-inner-container-no-side-margin']")
    checkbox_multilogin.click()

    print(Fore.GREEN + "Открыл окно с добавлением данных о новом юзере")
except TimeoutException:
    print(Fore.RED + "Окно с добавлением данных о новом юзере не открылось")
    driver.quit()


save_new_user = driver.find_element(By.XPATH, "//span[contains(text(),'Сохранить')]")
save_new_user.click()
time.sleep(2)
print(Fore.BLUE + "ipe-1380:Создание нового пользователя - ПРОЙДЕН")
#вынести в проверку