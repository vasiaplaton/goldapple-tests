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


