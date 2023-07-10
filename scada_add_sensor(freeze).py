from selenium import webdriver  # для открытия браузера
import time  # для юзания дилея при открытии вебокон
from selenium.webdriver.common.by import By  # для поиска by
from selenium.webdriver import Keys
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

delay = 1
#в будущем создать отдельный файл для заполнений логинов+паролей+ссылок
driver = (webdriver.Chrome())
driver.get('http://192.168.10.72:10000//Widgets/scadaEmber/index.html')
driver.maximize_window()
time.sleep(delay)

scada_log_form = driver.find_element(By.ID, 'settingsButton')  # клик на кнопку настроек
scada_log_form.click()
time.sleep(delay)

input_ipaddr = driver.find_element(By.ID, 'ip_address')  # заполнение поля айпи адрес
input_ipaddr.click()

input_ipaddr.send_keys("192.168.11.112:8888")
time.sleep(delay)

input_login = driver.find_element(By.ID, 'id_username')  # заполнение поля логин
input_login.click()

input_login.send_keys("malashkin")
time.sleep(delay)

input_password = driver.find_element(By.ID, 'id_password')  # заполнение поля пароль
input_password.click()

input_password.send_keys("malashkin")

input_password.send_keys(Keys.RETURN)
time.sleep(delay)

input_firefly = driver.find_element(By.ID, 'firefly')  # заполнение поля фф
time.sleep(3)
input_firefly.click()
input_firefly.send_keys("192.168.11.112:5555")
input_firefly.send_keys(Keys.RETURN)
time.sleep(delay)

entry_scada = driver.find_element(By.ID, 'loginDiv')  # клик на кнопку подключение и ожидании прогрузки графа
entry_scada.click() #для выбора разных подключений
time.sleep(15)



# поиск по shadow-root элементов
shadow_main_url = driver.find_element(By.CSS_SELECTOR, 'scada-div')
print(shadow_main_url)

enter_shadow = shadow_main_url.shadow_root #для входа в теневое дерево
shadow_tree = enter_shadow.find_element(By.CSS_SELECTOR, '#scadaLeftPane') #вход в теневое дерево
print(shadow_tree) #проверка возврата значения

element_types_enter = enter_shadow.find_element(By.CSS_SELECTOR, '#leftTabs > li.bg-solid.btn.scadaTabButton.scadaTabButton2 > a') #выбор кнопки "типы элементов"
element_types_enter.click()
time.sleep(2)


#переход в следующее теневое поддерево
shadow_tree2 = enter_shadow.find_element(By.CSS_SELECTOR, '#itemTypesTree')
print(enter_shadow, "456")


second_shadow_tree = shadow_tree2.shadow_root
dropout_video = second_shadow_tree.find_element (By.CSS_SELECTOR, 'div:nth-child(2) > div:nth-child(2) > ul:nth-child(1) > li:nth-child(1) > i:nth-child(1)')
dropout_video.click()
time.sleep(delay)
print(dropout_video, "321")


drag_sensor = second_shadow_tree.find_element(By.CSS_SELECTOR, '#VideosourceCategory\.IpVideoCamera_anchor')
print(drag_sensor, "sensor")


third_shadow = shadow_tree2.shadow_root
pre_find_graph = third_shadow.find_element(By.CSS_SELECTOR, '#itemAbstractTypesDiv')
print(pre_find_graph, "pre-graf")


drop_graph = second_shadow_tree.find_element(By.CSS_SELECTOR, '')
print(drop_graph, "graph")


actions = ActionChains(driver)
actions.click_and_hold(drag_sensor).move_to_element(drop_graph).release().perform()


time.sleep(10)
