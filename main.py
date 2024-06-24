from selenium import webdriver  # загрузка драйвера браузера для Селениум
import time
import random
# from selenium.webdriver import Keys
from selenium.webdriver.common.by import By  # для автоматизированного поиска на странице

# browser = webdriver.Chrome()
# browser.get("https://wikipedia.org/wiki/Document_Object_Model")
# browser.save_screenshot("dom.png")
# time.sleep(5)
# browser.get("https://wikipedia.org/wiki/Selenium")
# browser.save_screenshot("selenium.png")
# time.sleep(3)
# browser.refresh()  # или для выхода и завершения - browser.quit()
# browser = webdriver.Chrome()
# browser.get("https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0")
# assert "Википедия" in browser.title
# time.sleep(2)
# search_box = browser.find_element(By.ID, "searchInput")
# search_box.send_keys("Солнце")
# search_box.send_keys(Keys.RETURN)
#
# time.sleep(5)
# a = search_box = browser.find_element(By.LINK_TEXT, "Солнце")
# a.click()
# time.sleep(5)
browser = webdriver.Chrome()
browser.get("https://ru.wikipedia.org/wiki/%D0%A1%D0%BE%D0%BB%D0%BD%D1%86%D0%B5")
time.sleep(10)

# paragraphs = search_box = browser.find_elements(By.TAG_NAME, "p")
#
# for paragraph in paragraphs:
#     print(paragraph.text)
#     input()

hatnotes = []
for element in browser.find_elements(By.TAG_NAME, "div"):
    cl = element.get_attribute("class")
    if cl == "hatnote navigation-not-searchable":
        hatnotes.append(element)

print(hatnotes)
hatnote = random.choice(hatnotes)
link = hatnote.find_element(By.TAG_NAME, "a").get_attribute("href")
browser.get(link)
time.sleep(20)
browser.refresh()
