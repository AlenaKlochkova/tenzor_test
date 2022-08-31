from page_object import Page_Object

from constants import yandex_link, adv_close


class Yandex_Object(Page_Object):

    def main_page(self):

        '''Открывает главную страницу, закрывает всплывающее окно'''

        self.go_to(yandex_link)
        self.click_option(adv_close)

    def check_link(self, selector, link):

        '''Сравнивает первую ссылку из результатов поиска с искомой ссылкой'''

        result_link = self.get_first_link(selector)
        assert result_link == link

    def link_to_new_window(self, selector):

        '''Кликает по ссылке, переходит на новую вкладку'''

        self.click_option(selector)
        self.switch_to_new_window()

    def check_url(self, url):

        '''Проверяет, совпадает ли текущий url с искомым, либо начинается с него'''

        current_url = self.get_current_url()
        assert current_url.startswith(url)

    def check_category_name(self, category, link, input):

        '''Получает имя первой категории, переходит по ссылке первой категории, проверяет, что название категории отображается в
        поле поиска'''

        category_name = self.get_category_name(category)
        self.go_to_first_link(link)
        input_value = self.get_search_info(input)
        assert input_value == category_name
