import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from utilities.logger import Logger


class CatalogPage(Base):

    # Locators
    catalog_button = "//div[@class='NavigationBar_burger__j7lZE']"
    main_category_button_1 = "//li[@data-id='1537']"
    sub_category_button_1 = "//span[text()='Ноутбуки с процессором Intel']"
    select_list_product = "//div[@class='SelectableList_wrap__uvkMK SelectableList_inline__ZMCCF']"
    select_sort_product_1 = "//span[text()='Сначала дорогие']"
    minimum_price = "//input[@name='min']"
    maximum_price = "//input[@name='max']"
    pc_maker_checkbox = "//label[@for='id-Acer-Acer']"
    operating_system_list = "//span[text()='Операционная система']"
    operating_system_checkbox_1 = "//label[@for='id-Windows-11-Home-26215']"
    operating_system_checkbox_2 = "//label[@for='id-Windows-11-Professional-26522']"
    enter_product_card = "(//a[@class='CardText_link__C_fPZ link_black'])[1]"
    main_category_button_2 = "//li[@data-id='1163']"
    sub_category_button_2 = "//p[text()='Электротранспорт']"
    select_sort_product_2 = "//span[text()='Сначала с низкой ценой']"
    device_type_checkbox = "(//label[@for='id-электросамокат-28760'])[1]"
    maker_checkbox_1 = "(//label[@for='id-Xiaomi-Xiaomi'])[1]"
    add_to_favorite_1 = "(//button[@aria-label='Добавить в избранное'])[2]"
    add_to_favorite_2 = "(//button[@aria-label='Добавить в избранное'])[1]"
    favorites_button = "//span[text()='Избранное']"
    product_search = "//input[@aria-label='Поиск']"
    select_sort_product_3 = "//span[text()='По названию (А-Я)']"
    product_maker_search = "//input[@placeholder='Поиск']"
    maker_checkbox_2 = "(//label[@for='id-Dell-Dell'])[1]"
    add_to_comparison_1 = "(//button[@aria-label='Добавить в сравнение'])[2]"
    add_to_comparison_2 = "(//button[@aria-label='Добавить в сравнение'])[1]"
    comparison_button = "//span[text()='Сравнение']"

    # Getters
    def get_catalog_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.catalog_button)))
    # Клик на кнопку "Каталог"

    def get_main_category_button_1(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.main_category_button_1)))
    # Клик на раздел "Компьютеры и ноутбуки"

    def get_sub_category_button_1(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.sub_category_button_1)))
    # Клик на раздел "Ноутбуки с процессором Intel"

    def get_select_list_product(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.select_list_product)))
    # Клик на выпадающий список сортировки товаров

    def get_select_sort_product_1(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.select_sort_product_1)))
    # Выбор сортировки товаров - "Сначала дорогие"

    def get_minimum_price(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.minimum_price)))
    # Ввод значения фильтра минимальной цены продукции

    def get_maximum_price(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.maximum_price)))
    # Ввод значения фильтра максимальной цены продукции

    def get_pc_maker_checkbox(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.pc_maker_checkbox)))
    # Выбор чекбокса "Производитель" - "Acer"

    def get_operating_system_list(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.operating_system_list)))
    # Клик на выпадающий список чекбоксов "Операционная система"

    def get_operating_system_checkbox_1(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.operating_system_checkbox_1)))
    # Выбор чекбокса "Операционная система" - "Windows 11 Home"

    def get_operating_system_checkbox_2(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.operating_system_checkbox_2)))
    # Выбор чекбокса "Операционная система" - "Windows 11 Professional"

    def get_enter_product_card(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.enter_product_card)))
    # Переход на страницу товара

    def get_main_category_button_2(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.main_category_button_2)))
    # Клик на раздел "Электроника"

    def get_sub_category_button_2(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.sub_category_button_2)))
    # Клик на раздел "Электротранспорт"

    def get_select_sort_product_2(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.select_sort_product_2)))
    # Выбор сортировки товаров - "Сначала с низкой ценой"

    def get_device_type_checkbox(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.device_type_checkbox)))
    # Выбор чекбокса "Тип устройства" - "Электросамокат"

    def get_maker_checkbox_1(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.maker_checkbox_1)))
    # Выбор чекбокса "Производитель" - "Xiaomi"

    def get_add_to_favorite_1(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.add_to_favorite_1)))
    #  Добавление в избранное товара 1

    def get_add_to_favorite_2(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.add_to_favorite_2)))
    #  Добавление в избранное товара 2

    def get_favorites_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.favorites_button)))
    # Переход в раздел "Избранное"

    def get_product_search(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.product_search)))
    # Переход в раздел "Мониторы" путем ввода названия категории товаров в строку поиска

    def get_select_sort_product_3(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.select_sort_product_3)))
    # Выбор сортировки товаров - "По названию (А-Я)"

    def get_product_maker_search(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.product_maker_search)))
    # Выбор производителя мониторов через ввод в строку поиска фильтра "Производитель"

    def get_maker_checkbox_2(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.maker_checkbox_2)))
    # Выбор чекбокса "Производитель" - "Dell"

    def get_add_to_comparison_1(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.add_to_comparison_1)))
    #  Добавление к сравнению товара 1

    def get_add_to_comparison_2(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.add_to_comparison_2)))
    #  Добавление к сравнению товара 1

    def get_comparison_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.comparison_button)))
    # Переход в раздел "Сравнение"

    # Actions
    def click_catalog_button(self):
        self.get_catalog_button().click()
        print("Click Catalog Button")
        time.sleep(3)

    def click_main_category_button_1(self):
        self.get_main_category_button_1().click()
        print("Click Main Category Button")
        time.sleep(3)

    def click_sub_category_button_1(self):
        self.get_sub_category_button_1().click()
        print("Click Sub Category Button")
        print("Selecting Product Category OK")
        time.sleep(3)

    def click_select_list_product(self):
        self.get_select_list_product().click()
        print("Click Select List Product")
        time.sleep(3)

    def click_select_sort_product_1(self):
        self.get_select_sort_product_1().click()
        print("Click Select Sort Product")
        print("Product Sorting Filter OK")
        time.sleep(3)

    def input_minimum_price(self, minimum_price):
        self.get_minimum_price().send_keys(minimum_price)
        print("Input Minimum Price")
        time.sleep(3)

    def input_maximum_price(self, maximum_price):
        self.get_maximum_price().send_keys(maximum_price)
        print("Input Maximum Price")
        print("Price Filter OK")
        time.sleep(3)

    def click_pc_maker_checkbox(self):
        self.get_pc_maker_checkbox().click()
        print("Click PC Maker Checkbox")
        print("PC Maker Filter OK")
        time.sleep(3)

    def click_operating_system_list(self):
        self.get_operating_system_list().click()
        print("Click Operating System List")
        time.sleep(3)

    def click_operating_system_checkbox_1(self):
        self.get_operating_system_checkbox_1().click()
        print("Click Operating System Checkbox 1")
        time.sleep(3)

    def click_operating_system_checkbox_2(self):
        self.get_operating_system_checkbox_2().click()
        print("Click Operating System Checkbox 2")
        print("Operating System Filter OK")
        time.sleep(3)

    def click_enter_product_card(self):
        self.get_enter_product_card().click()
        print("Click Enter Product Card")
        time.sleep(3)

    def click_main_category_button_2(self):
        self.get_main_category_button_2().click()
        print("Click Main Category Button")
        time.sleep(3)

    def click_sub_category_button_2(self):
        self.get_sub_category_button_2().click()
        print("Click Sub Category Button")
        print("Selecting Product Category OK")
        time.sleep(3)

    def click_select_sort_product_2(self):
        self.get_select_sort_product_2().click()
        print("Click Select Sort Product")
        print("Product Sorting Filter OK")
        time.sleep(3)

    def click_device_type_checkbox(self):
        self.get_device_type_checkbox().click()
        print("Device Type Filter OK")
        time.sleep(3)

    def click_maker_checkbox_1(self):
        self.get_maker_checkbox_1().click()
        print("Maker Filter OK")
        time.sleep(3)

    def click_add_to_favorite_1(self):
        self.get_add_to_favorite_1().click()
        print("Add To Favorites 1 OK")
        time.sleep(3)

    def click_add_to_favorite_2(self):
        self.get_add_to_favorite_2().click()
        print("Add To Favorites 2 OK")
        time.sleep(3)

    def click_favorites_button(self):
        self.get_favorites_button().click()
        print("Click Favorites Button")
        time.sleep(3)

    def input_product_search(self, product_search):
        self.get_product_search().send_keys(product_search)
        self.get_product_search().send_keys(Keys.RETURN)
        print("Input Product Category")
        time.sleep(3)

    def click_select_sort_product_3(self):
        self.get_select_sort_product_3().click()
        print("Click Select Sort Product")
        print("Product Sorting Filter OK")
        time.sleep(3)

    def input_product_maker_search(self, product_maker_search):
        self.get_product_maker_search().send_keys(product_maker_search)
        print("Input Product Maker Search")
        time.sleep(3)

    def click_maker_checkbox_2(self):
        self.get_maker_checkbox_2().click()
        print("Maker Filter OK")
        time.sleep(3)

    def click_add_to_comparison_1(self):
        self.get_add_to_comparison_1().click()
        print("Add To Comparison 1 OK")
        time.sleep(3)

    def click_add_to_comparison_2(self):
        self.get_add_to_comparison_2().click()
        print("Add To Comparison 2 OK")
        time.sleep(3)

    def click_comparison_button(self):
        self.get_comparison_button().click()
        print("Click Comparison Button")
        time.sleep(3)

    # Methods
    # Выбор 1 товара через фильтры каталога для последующего добавления его в корзину
    def product_selection(self):
        Logger.add_start_step(method="product_selection")
        self.click_catalog_button()
        self.click_main_category_button_1()
        self.click_sub_category_button_1()
        self.click_select_list_product()
        self.click_select_sort_product_1()
        self.input_minimum_price("110000")
        self.input_maximum_price("130000")
        self.click_pc_maker_checkbox()
        self.driver.execute_script("window.scrollTo(0, 1000)")
        self.click_operating_system_list()
        self.click_operating_system_checkbox_1()
        self.click_operating_system_checkbox_2()
        self.driver.execute_script("window.scrollTo(0, 0)")
        self.click_enter_product_card()
        Logger.add_end_step(url=self.driver.current_url, method="product_selection")

    # Выбор 2-х товаров через фильтры каталога для последующего добавления их в избранное
    def select_favorites(self):
        Logger.add_start_step(method="select_favorites")
        self.click_catalog_button()
        self.click_main_category_button_2()
        self.driver.execute_script("window.scrollTo(0, 400)")
        self.click_sub_category_button_2()
        self.click_select_list_product()
        self.click_select_sort_product_2()
        self.click_device_type_checkbox()
        self.click_maker_checkbox_1()
        self.click_add_to_favorite_1()
        self.click_add_to_favorite_2()
        self.click_favorites_button()
        Logger.add_end_step(url=self.driver.current_url, method="select_favorites")

    # Выбор 2-х товаров через фильтры каталога для последующего добавления их к сравнению
    def select_comparison(self):
        Logger.add_start_step(method="select_comparison")
        self.input_product_search("Мониторы")
        self.click_select_list_product()
        self.click_select_sort_product_3()
        self.driver.execute_script("window.scrollTo(0, 400)")
        self.input_product_maker_search("Dell")
        self.click_maker_checkbox_2()
        self.click_add_to_comparison_1()
        self.click_add_to_comparison_2()
        self.click_comparison_button()
        Logger.add_end_step(url=self.driver.current_url, method="select_comparison")
