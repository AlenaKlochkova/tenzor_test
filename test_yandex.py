import pytest
from selenium import webdriver

from yandex_object import YandexObject
from constants import *


@pytest.fixture()
def browser():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()


def test_one(browser):
    yandex = YandexObject(browser)
    yandex.main_page()
    yandex.search_field_input(yandex_search_field, 'Тензор')
    yandex.loading(suggest)
    yandex.press_enter(yandex_search_field)
    yandex.loading(result_table)
    yandex.check_link(result_link_list, tensor_link)


def test_two(browser):
    yandex = YandexObject(browser)
    yandex.main_page()
    yandex.link_to_new_window(pictures_link)
    yandex.loading(pictures_category)
    yandex.check_url(pictures_url)
    yandex.check_category_name(pictures_category, pictures_category_link, pictures_search_field)
    yandex.go_to_first_link(image_link)
    image_one = yandex.get_image_src(image_full)
    yandex.change_image(next_image)
    image_two = yandex.get_image_src(image_full)
    yandex.check_difference(image_one, image_two)
    yandex.change_image(previous_image)
    image_back = yandex.get_image_src(image_full)
    yandex.check_equality(image_one, image_back)
