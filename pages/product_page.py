import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from utilities.logger import Logger


class ProductPage(Base):

    # Locators
    add_cart_product = "//button[contains(text(), 'Добавить в корзину')]"
    add_cart_button = "//button[contains(text(), 'В корзине')]"
    cart_button = "//div[@class='IconButton_btn__eHnyM IconButton_cart__Na0hE']"
    enter_cart_button = "//a[contains(text(), 'Перейти в корзину')]"

    # Getters
    def get_add_cart_product(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.add_cart_product)))
    # Клик на кнопку "Добавить в корзину"

    def get_add_cart_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.add_cart_button)))
    # Проверка добавления товара в корзину по изменению надписи кнопки "Добавить в корзину" на надпись "В корзине"

    def get_cart_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.cart_button)))
    # Клик на кнопку "Корзина"

    def get_enter_cart_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.enter_cart_button)))
    # Клик на кнопку "Перейти в корзину"

    # Actions
    def click_add_cart_product(self):
        self.get_add_cart_product().click()
        print("Click Add Cart Product")
        time.sleep(3)

    def click_cart_button(self):
        self.get_cart_button().click()
        print("Click Cart Button")
        time.sleep(3)

    def click_enter_cart_button(self):
        self.get_enter_cart_button().click()
        print("Click Enter Cart Button")
        time.sleep(3)

    # Methods
    # Добавление товара в корзину со страницы выбранного товара
    def product_card(self):
        Logger.add_start_step(method="product_card")
        self.get_current_url()
        self.click_add_cart_product()
        self.assert_word(self.get_add_cart_button(), "В корзине")
        self.click_cart_button()
        self.click_enter_cart_button()
        Logger.add_end_step(url=self.driver.current_url, method="product_card")
