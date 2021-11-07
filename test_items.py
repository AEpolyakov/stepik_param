import pytest
import time
from selenium.webdriver.common.by import By


def test_button_to_basket(browser):
    browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
    time.sleep(3)

    button_to_basket = browser.find_element(By.XPATH, '//form[@id="add_to_basket_form"]/button')

    assert button_to_basket, 'отсутствует кнопка "В корзину"'


if __name__ == "__main__":
    pytest.main()

