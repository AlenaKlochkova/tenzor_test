from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


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

    def get_first_link(self, selector):

        """Возвращает ссылку из первого элемента в списке"""

        search_list = self.driver.find_elements(*selector)
        return search_list[0].get_attribute('href')

    def click_option(self, selector):

        """Ищет элемент и кликает по нему"""

        self.loading(selector)
        self.driver.find_element(*selector).click()





