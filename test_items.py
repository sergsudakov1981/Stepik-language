from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207//"

def test_user_should_see_button_basket(browser):
    browser.get(link)
    # time.sleep(10)
    basket_btn = browser.find_elements(By.CSS_SELECTOR, "#add_to_basket_form button")
    assert len(basket_btn) > 0, 'Отсутствует кнопка добавления в корзину'