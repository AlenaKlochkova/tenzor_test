from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains as AC


class PageObject:

    def __init__(self, driver):
        self.driver = driver

    def go_to(self, link):

        '''Переходит по указанной ссылке'''

        self.driver.get(link)

    def loading_visibility(self, selector):

        '''Ожидание загрузки указанного элемента на странице'''

        wait = WebDriverWait(self.driver, 50)
        wait.until(EC.visibility_of_element_located(selector))

    def loading_clickable(self, selector):

        '''Ожидает, когда указанный элемент станет доступным для клика по нему'''

        wait = WebDriverWait(self.driver, 50)
        wait.until(EC.element_to_be_clickable(selector))

    def search_field_input(self, search_field, input_content):

        '''Находит поисковую строку, вводит запрос'''

        self.loading_visibility(search_field)
        search = self.driver.find_element(*search_field)
        search.send_keys(input_content)

    def press_enter(self, search_field):

        '''Имитирует нажатие клавиши "ENTER"'''

        search = self.driver.find_element(*search_field)
        search.send_keys(Keys.ENTER)

    def click_option(self, selector):

        '''Ищет элемент и кликает по нему'''

        self.loading_visibility(selector)
        self.driver.find_element(*selector).click()

    def switch_to_new_window(self):

        '''Переходит на последнюю открытую вкладку'''

        self.driver.switch_to.window(self.driver.window_handles[-1])

    def get_current_url(self):

        '''Возвращает url текущей страницы'''

        return self.driver.current_url

    def go_to_first_link(self, selector):

        '''Переходит по первой ссылке в списке'''

        self.loading_visibility(selector)
        link = self.driver.find_elements(*selector)[0]
        link.click()

    def get_attribute(self, selector, attr):

        '''Возвращает значение искомого атрибута элемента'''

        self.loading_visibility(selector)
        return self.driver.find_element(*selector).get_attribute(attr)

    def get_first_link(self, selector):

        '''Возвращает ссылку из первого элемента в списке'''

        return self.get_attribute(selector, 'href')

    def get_search_info(self, selector):

        '''Получает текст из поля поиска'''

        return self.get_attribute(selector, 'value')

    def get_category_name(self, selector):

        '''Возвращает назнание первой категории'''

        return self.get_attribute(selector, 'data-grid-text')

    def get_image_src(self, selector):

        '''Возвращает ссылку на источник картинки'''

        return self.get_attribute(selector, 'src')

    def check_equality(self, item1, item2):

        '''Проверяет равенство значений двух объектов'''

        assert item1 == item2

    def check_difference(self, item1, item2):

        '''Проверяет неравенство значений двух объектов'''

        assert item1 != item2

    def hover_to_item(self, selector):

        '''Помещает курсор мыши на указанном элементе'''

        item = self.driver.find_element(*selector)
        hover = AC(self.driver).move_to_element(item)
        hover.perform()
