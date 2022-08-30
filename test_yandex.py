import pytest
from selenium import webdriver

from page_object import Page_Object
from constants import *


@pytest.fixture()
def browser():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()

def test_one(browser):
    yandex = Page_Object(browser)
    yandex.go_to(yandex_link)
    yandex.click_option(adv_close)
    yandex.loading(yandex_search_field)
    yandex.search_field_input(yandex_search_field, 'Тензор')
    yandex.loading(suggest)
    yandex.press_enter(yandex_search_field)
    yandex.loading(result_table)
    result_link = yandex.get_first_link(result_link_list)
    result_link == tensor_link

