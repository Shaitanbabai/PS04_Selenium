from selenium import webdriver
from selenium.webdriver.common.by import By

# Инициализация веб-драйвера (в данном случае используется Microsoft Edge)
driver = webdriver.Edge()

# Запрашиваем у пользователя первоначальный запрос
initial_query = input("Введите запрос: ")

# Переходим на страницу Википедии по первоначальному запросу
WIKI = f"https://en.wikipedia.org/wiki/{initial_query}"
driver.get(WIKI)

# Находим первый параграф на странице
first_paragraph = driver.find_element(By.CSS_SELECTOR, 'p')

# Выводим контекст статьи
print("Контекст статьи:")
print(first_paragraph.text)

# Пользователь выбирает, что делать дальше
print("\nВыберите действие:")
print("1. Листать параграфы текущей статьи")
print("2. Перейти на связанную страницу")
print("3. Выйти из программы")

choice = int(input("Введите номер действия: "))

if choice == 1:
    # Выводим параграфы текущей статьи
    print("\nПараграфы текущей статьи:")
    paragraphs = driver.find_elements(By.CSS_SELECTOR, 'p')
    for index, paragraph in enumerate(paragraphs, start=1):
        print(f"{index}. {paragraph.text}")
elif choice == 2:
    # Выводим связанные статьи
    print("\nСвязанные статьи:")
    related_articles = driver.find_elements(By.CSS_SELECTOR, '.mw-parser-output a')
    for index, article in enumerate(related_articles, start=1):
        print(f"{index}. {article.text}")
else:
    print("Программа завершена.")

# Не забудьте закрыть веб-драйвер
driver.quit()