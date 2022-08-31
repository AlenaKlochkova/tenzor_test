from selenium.webdriver.common.by import By


yandex_link = 'https://www.yandex.ru/'
adv_close = (By.CSS_SELECTOR, 'div.modal__close')
yandex_search_field = (By.CSS_SELECTOR, 'input#text')
suggest = (By.CSS_SELECTOR, 'ul.mini-suggest__popup-content')
result_table = (By.CSS_SELECTOR, 'ul#search-result')
result_link_list = (By.CSS_SELECTOR, 'li.serp-item.serp-item_card a')
tensor_link = 'https://tensor.ru/'
pictures_link = (By.CSS_SELECTOR, 'a[data-id="images"]')
pictures_url = 'https://yandex.ru/images/'
pictures_category = (By.CSS_SELECTOR, '[data-grid-name="im"]')
pictures_category_link = (By.CSS_SELECTOR, 'a.Link.PopularRequestList-Preview')
pictures_search_field = (By.CSS_SELECTOR, 'input.input__control.mini-suggest__input')
image_link = (By.CSS_SELECTOR, 'a.serp-item__link')
image_full = (By.CSS_SELECTOR, 'img.MMImage-Preview')
next_image = (By.CSS_SELECTOR, 'div.MediaViewer-ButtonNext')
previous_image = (By.CSS_SELECTOR, 'div.MediaViewer-ButtonPrev')
