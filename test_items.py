import pytest
import time
from selenium.webdriver.common.by import By


def test_button_to_basket(browser):
    browser.get('http://selenium1py.pythonanywhere.com/nl/catalogue/coders-at-work_207/')

    button_to_basket = browser.find_element(By.XPATH, '//form[@id="add_to_basket_form"]/button')
    time.sleep(10)
    assert button_to_basket


if __name__ == "__main__":
    pytest.main()

