import pytest
from selenium import webdriver

from yandex_object import Yandex_Object
from constants import *


@pytest.fixture()
def browser():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()

def test_one(browser):
    yandex = Yandex_Object(browser)
    yandex.main_page()
    yandex.loading(yandex_search_field)
    yandex.search_field_input(yandex_search_field, 'Тензор')
    yandex.loading(suggest)
    yandex.press_enter(yandex_search_field)
    yandex.loading(result_table)
    yandex.check_link(result_link_list, tensor_link)


def test_two(browser):
    yandex = Yandex_Object(browser)
    yandex.main_page()
    yandex.loading(pictures_link)
    yandex.link_to_new_window(pictures_link)
    yandex.check_url(pictures_url)
    yandex.loading(pictures_category)
    yandex.check_category_name(pictures_category, pictures_category_link, pictures_search_field)
    yandex.go_to_first_link(image_link)
    yandex.loading(image_full)
    image_one = yandex.get_image_src(image_full)
    yandex.click_option(next_image)
    image_two = yandex.get_image_src(image_full)
    assert image_one != image_two
    yandex.click_option(previous_image)
    image_back = yandex.get_image_src(image_full)
    assert image_one == image_back

