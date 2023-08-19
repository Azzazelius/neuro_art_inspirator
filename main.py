'''
to do
exclude the last href from each page, it is an adv.
'''


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import time
import os

useragent = UserAgent()
options = webdriver.ChromeOptions()
options.add_argument(f"user-agent={useragent.random}")
driver_path = r"D:\tmp\python_art_randomizer\chromedriver.exe"
service = Service(driver_path)
driver = webdriver.Chrome(service=service, options=options)

# url = 'https://www.midlibrary.io/styles?491bc942_page=49'
url = 'https://www.midlibrary.io/styles/'
driver.get(url=url)

links = []

pages = 1
try:
    styles = 0
    while True:
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        time.sleep(5)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        hrefs = soup.select('a[href*="/styles/"]')  # Ищем ссылки содержащие "/styles/"
        print(len(hrefs))
        for href in hrefs:
        #     print(href)
            styles += 1
            print(f'Styles saved: {styles} ')
            links.append(href['href'].replace("/styles/",''))

        # Сохранение списка в файл
        with open("styles_list.txt", "w") as file:
            file.write('\n'.join(map(str, links)))

        # Go next
        next_button = driver.find_element(By.XPATH, "//a[@aria-label='Next Page']")
        time.sleep(3)
        # print(f"Button next is enabled = {next_button.is_enabled()}, and displayed = {next_button.is_displayed()}")

        if next_button.is_enabled() and next_button.is_displayed():
            driver.execute_script("arguments[0].click();", next_button)
            pages += 1
            print(f"{next_button.text} page №{pages}\n---------------")
        else:
            print(f'\n==============='
                  f"\nIt was the last page."
                  f"\nTotal pages: {pages}"
                  f"\nTotal styles: {styles}"
                  f"\nList saved to styles_list.txt"
                  f"\n===============")
            break

except Exception as ex:
    print("Exception!!!\n", ex)
finally:
    driver.close()
    driver.quit()


print(f"---------------Scrapping complete-----------------")
#
# if os.path.exists('styles_list.txt'):
#     os.system(f"notepad styles_list.txt")
# else:
#     print(f"Файл styles_list.txt не найден.")
#
# exit()

