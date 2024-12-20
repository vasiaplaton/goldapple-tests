
# Отчет по лабараторной работе №3 "Написание автотестов на Python"
- Сайт: [Золотое Яблоко](https://goldenapple.ru/)
- Функционал: Поиск товаров
- Фреймворк: [Selenium](https://www.selenium.dev/), [Pytest](https://docs.pytest.org/en/stable/)
- Результат: Успешно пройдены 7 из 7 тестов
![1.png](readme_imgs%2F1.png)

## Видео
[https://youtu.be/bs5YL7C_2fw](https://youtu.be/bs5YL7C_2fw)

# Таблица с тест-кейсами

| **№** | **Название**                                   | **Функция**                         | **Предусловие**                                                                                                                                             | **Шаги теста**                                                                                                                                                                                   | **Ожидаемый результат**                                                                                                                                                                             |
|-------|------------------------------------------------|--------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1     | Поиск товара по названию (товар существует)    | `test_find_by_name_item_exists`      | 1. Открыть сайт Золотое Яблоко.<br>2. Убедиться, что сайт доступен.                                                                                         | 1. Нажать на кнопку с иконкой лупы.<br>2. Ввести в поле "хочу купить" текст: "Lash".<br>3. Нажать кнопку с иконкой отправки запроса.                                                             | 1. Открывается страница с результатами поиска.<br>2. В списке товаров присутствует "Lash Cocoon".<br>3. Количество найденных товаров больше 10.                                                   |
| 2     | Поиск товара по артикулу (товар существует)    | `test_find_by_article_item_exists`   | 1. Открыть сайт Золотое Яблоко.<br>2. Убедиться, что сайт доступен.                                                                                         | 1. Нажать на кнопку с иконкой лупы.<br>2. Ввести в поле "хочу купить" текст: "19760313937".<br>3. Нажать кнопку с иконкой отправки запроса.                                                     | 1. Открывается страница с результатами поиска.<br>2. В списке товаров присутствует "Lash Cocoon".<br>3. Количество найденных товаров равно 1.                                                     |
| 3     | Поиск товара по названию (товар не существует) | `test_find_by_name_items_not_exists` | 1. Открыть сайт Золотое Яблоко.<br>2. Убедиться, что сайт доступен.                                                                                         | 1. Нажать на кнопку с иконкой лупы.<br>2. Ввести в поле "хочу купить" текст: "ejdoiewjoigewjoigwrfiogio".<br>3. Нажать кнопку с иконкой отправки запроса.                                        | 1. На странице отображается сообщение: "Ничего не найдено. Попробуйте изменить запрос и мы поищем ещё раз".<br>2. Страница не содержит карточек товаров.                                          |
| 4     | Поиск товара по артиклу (товар не существует)  | `test_find_by_article_items_not_exists` | 1. Открыть сайт Золотое Яблоко.<br>2. Убедиться, что сайт доступен.                                                                                         | 1. Нажать на кнопку с иконкой лупы.<br>2. Ввести в поле "хочу купить" текст: "19760313937".<br>3. Нажать кнопку с иконкой отправки запроса.                                        | 1. На странице отображается сообщение: "Ничего не найдено. Попробуйте изменить запрос и мы поищем ещё раз".<br>2. Страница не содержит карточек товаров.                                          |
| 5     | Кнопка отправки недоступна при пустом поле     | `test_cant_click_if_nothing_input`   | 1. Открыть сайт Золотое Яблоко.<br>2. Убедиться, что сайт доступен.                                                                                         | 1. Нажать на кнопку с иконкой лупы.<br>2. Убедиться, что кнопка отправки запроса недоступна.                                                                                                     | 1. Кнопка с иконкой отправки запроса неактивна.                                                                                                                                                     |
| 6     | Переход на страницу бренда                     | `test_brand_page`                    | 1. Открыть сайт Золотое Яблоко.<br>2. Убедиться, что сайт доступен.                                                                                         | 1. Нажать на кнопку с иконкой лупы.<br>2. Ввести в поле "хочу купить" текст: "Darling".<br>3. Нажать кнопку с иконкой отправки запроса.                                                         | 1. Пользователь переходит на страницу бренда.<br>2. На странице отображается заголовок с названием бренда.                                                                                        |
| 7     | Исправление опечатки в поисковом запросе       | `test_autocorrect`                   | 1. Открыть сайт Золотое Яблоко.<br>2. Убедиться, что сайт доступен.                                                                                         | 1. Нажать на кнопку с иконкой лупы.<br>2. Ввести в поле "хочу купить" текст: "женские aраматы".<br>3. Нажать кнопку с иконкой отправки запроса.                                                  | 1. Поисковый запрос исправлен на "женские ароматы".<br>2. Пользователь видит результаты, соответствующие исправленному запросу.                                                                    |

Исходный код
tests/conftest.py (фикстуры с браузером)
```python
import pytest
from selenium import webdriver

@pytest.fixture
def browser():
    # Initialize WebDriver
    driver = webdriver.Chrome()  # Or use Firefox(), Edge(), etc.
    driver.implicitly_wait(10)  # Wait up to 10 seconds for elements to appear
    yield driver
    # Teardown: Quit browser after test
    driver.quit()
```

tests/test_search.py (тесты)
```python
import time

from selenium.common import NoSuchElementException

# Constants for locators
LOC_DIALOG_CLOSE_XPATH = "//button[contains(@class, 'Kvoqg') and contains(@class, 'N7b5D') and contains(@class, 'CC+dX') and contains(@class, 'ocpDn') and contains(@class, '_2K18l') and contains(@class, 'GNXKr')]"
OPEN_SEARCH_BUTTON_CLASS = "ga-header__tab_type_search"
SEARCH_INPUT_XPATH = "//input[@placeholder='хочу купить']"
SUBMIT_SEARCH_BUTTON_XPATH = "//button[@type='submit']"
RESULT_AMOUNT_LOCATOR = "//span[contains(@class, 'qHm8S')]"
NOTHING_FOUND = "//p[contains(@class, '_1bcxg')]"
BRAND_LINK_XPATH = "//a[@href='/brands/darling']"
TEXT_HELP_SPATH = "//span[text()='женские ароматы']"
SLEEP = 2


def open_site(browser):
    # Step 1: Open the website
    browser.get("https://goldapple.ru/")


def skip_loc(browser):
    # Step 2: Check if <span> exists
    try:
        button = browser.find_element("xpath", LOC_DIALOG_CLOSE_XPATH)

        # Step 2: Click the button
        button.click()
        print("Button clicked successfully.")
    except NoSuchElementException:
        print("Button not found.")


def open_search(browser):
    button = browser.find_element("class name", OPEN_SEARCH_BUTTON_CLASS)
    # Step 2: Click the button
    button.click()


def input_in_search(browser, text: str):
    input_field = browser.find_element("xpath", SEARCH_INPUT_XPATH)
    print("Input field found.")

    input_field.send_keys(text)


def get_search_button(browser):
    return browser.find_element("xpath", SUBMIT_SEARCH_BUTTON_XPATH)


def find_by_text(browser, text: str):
    open_site(browser)
    time.sleep(SLEEP)
    skip_loc(browser)
    time.sleep(SLEEP)
    open_search(browser)
    time.sleep(SLEEP)
    input_in_search(browser, text)
    time.sleep(SLEEP)

    submit_button = get_search_button(browser)
    assert submit_button.get_attribute("disabled") is None
    submit_button.click()
    time.sleep(SLEEP)


def test_find_by_name_item_exists(browser):
    find_by_text(browser, "Lash")
    assert "Lash Cocoon" in browser.page_source

    result_amount = browser.find_element("xpath", RESULT_AMOUNT_LOCATOR)
    assert int(result_amount.text.strip().split(" ")[0]) > 10


def test_find_by_article_item_exists(browser):
    find_by_text(browser, "19760313937")
    assert "Lash Cocoon" in browser.page_source

    result_amount = browser.find_element("xpath", RESULT_AMOUNT_LOCATOR)
    assert int(result_amount.text.strip().split(" ")[0]) == 1


def test_find_by_name_items_not_exists(browser):
    find_by_text(browser, "ejdoiewjoigewjoigwrfiogio")
    assert """
        Ничего не найдено. Попробуйте изменить запрос и мы поищем ещё раз.
      """ in browser.page_source

    nothing_found_label = browser.find_element("xpath", NOTHING_FOUND)
    assert nothing_found_label is not None


def test_find_by_article_items_not_exists(browser):
    find_by_text(browser, "12948274724")
    assert """
        Ничего не найдено. Попробуйте изменить запрос и мы поищем ещё раз.
      """ in browser.page_source

    nothing_found_label = browser.find_element("xpath", NOTHING_FOUND)
    assert nothing_found_label is not None


def test_cant_click_if_nothing_input(browser):
    open_site(browser)
    time.sleep(SLEEP)
    skip_loc(browser)
    time.sleep(SLEEP)
    open_search(browser)
    time.sleep(SLEEP)
    submit_button = get_search_button(browser)
    assert submit_button.get_attribute("disabled") == "true"



def test_brand_page(browser):
    find_by_text(browser, "Darling")
    nothing_found_label = browser.find_element("xpath", BRAND_LINK_XPATH)
    assert nothing_found_label is not None


def test_autocorrect(browser):
    open_site(browser)
    time.sleep(SLEEP)
    skip_loc(browser)
    time.sleep(SLEEP)
    open_search(browser)
    time.sleep(SLEEP)
    input_in_search(browser, "женские aраматы")
    time.sleep(SLEEP)
    nothing_found_label = browser.find_element("xpath", TEXT_HELP_SPATH)
    assert nothing_found_label is not None
    time.sleep(SLEEP)


```