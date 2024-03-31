import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from utilities.logger import Logger


class BuyPage(Base):

    # Locators
    title_cart = "//h1[text()='Корзина']"
    clear_cart = "//button[@aria-label='Очистить корзину']"
    confirm_clear_cart = "//button[text()='Подтвердить']"
    title_empty_cart = "//span[text()='В корзине пока ничего нет']"

    # Getters
    def get_title_cart(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.title_cart)))
    # Проверка удачного перехода в раздел "Корзина" по заголовку "Корзина"

    def get_clear_cart(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.clear_cart)))
    # Клик на кнопку очистки корзины

    def get_confirm_clear_cart(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.confirm_clear_cart)))
    # Клик на кнопку подтверждения очистки корзины

    def get_title_empty_cart(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.title_empty_cart)))
    # Проверка очистки корзины по надписи "В корзине пока ничего нет"

    # Actions
    def click_clear_cart_1(self):
        self.get_clear_cart().click()
        print("Clear Cart")
        time.sleep(3)

    def click_clear_cart_2(self):
        self.get_confirm_clear_cart().click()
        print("Confirm Clear Cart")
        time.sleep(3)

    # Methods
    # Проверка наличия товара в корзине / удаление товара из корзины
    def cart(self):
        Logger.add_start_step(method="cart")
        self.get_current_url()
        self.assert_url("https://www.regard.ru/cart")
        self.assert_word(self.get_title_cart(), "Корзина")
        self.get_screenshot_1()
        self.click_clear_cart_1()
        self.click_clear_cart_2()
        self.assert_word(self.get_title_empty_cart(), "В корзине пока ничего нет")
        Logger.add_end_step(url=self.driver.current_url, method="cart")
