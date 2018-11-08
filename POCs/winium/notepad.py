from time import sleep
from selenium import webdriver

sleep(2)

driver = webdriver.Remote(
    command_executor='http://192.168.56.101:9999',
    desired_capabilities={
        "debugConnectToRunningApp": 'false',
        "app": r"C:/windows/system32/notepad.exe"
    })

window = driver.find_element_by_class_name("Notepad")
window.send_keys("Hello winium!!!")

driver.close()
