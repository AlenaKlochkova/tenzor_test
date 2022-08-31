from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time


class Page_Object():

    def __init__(self, driver):
        self.driver = driver

    def go_to(self, link):

        """Переходит по указанной ссылке"""

        self.driver.get(link)

    def loading(self, selector):

        """Ожидание загрузки указанного элемента на странице"""

        wait = WebDriverWait(self.driver, 50)
        wait.until(EC.visibility_of_element_located(selector))

    def search_field_input(self, search_field, input):

        """Находит поисковую строку, вводит запрос"""

        search = self.driver.find_element(*search_field)
        search.send_keys(input)

    def press_enter(self, search_field):

        '''Имитирует нажатие клавиши "ENTER"'''

        search = self.driver.find_element(*search_field)
        search.send_keys(Keys.ENTER)

    def click_option(self, selector):

        """Ищет элемент и кликает по нему"""

        self.loading(selector)
        self.driver.find_element(*selector).click()

    def switch_to_new_window(self):

        '''Переходит на последнюю открытую вкладку'''

        self.driver.switch_to.window(self.driver.window_handles[-1])

    def get_current_url(self):

        '''Возвращает url текущей страницы'''

        time.sleep(5)
        return self.driver.current_url

    def go_to_first_link(self, selector):

        '''Переходит по первой ссылке в списке'''

        self.loading(selector)
        link = self.driver.find_elements(*selector)[0]
        link.click()

    def get_attribute(self, selector, attr):

        '''Возвращает значение искомого атрибута элемента'''

        return self.driver.find_element(*selector).get_attribute(attr)

    def get_first_link(self, selector):

        """Возвращает ссылку из первого элемента в списке"""

        self.get_attribute(selector, 'href')

    def get_search_info(self, selector):

        '''Получает текст из поля поиска'''

        self.get_attribute(selector, 'value')

    def get_category_name(self, selector):

        '''Возвращает назнание первой категории'''

        self.get_attribute(selector, 'data-grid-text')

    def get_image_src(self, selector):

        '''Возвращает ссылку на источник картинки'''

        return self.get_attribute(selector, 'src')






