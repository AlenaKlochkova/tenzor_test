from selenium.webdriver.common.by import By


yandex_link = 'https://www.yandex.ru/'
adv_close = (By.CSS_SELECTOR, 'div.modal__close')
yandex_search_field = (By.CSS_SELECTOR, 'input#text')
suggest = (By.CSS_SELECTOR, 'ul.mini-suggest__popup-content')
result_table = (By.CSS_SELECTOR, 'ul#search-result')
result_link_list = (By.CSS_SELECTOR, 'li.serp-item.serp-item_card a')
tensor_link = 'https://tensor.ru/'