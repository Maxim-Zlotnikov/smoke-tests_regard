import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from utilities.logger import Logger


class AddFavoritesPage(Base):

    # Locators
    favorites_counter = "//span[text()='2 товара']"
    select_all_favorites = "(//label[@for='id-Выбрать-все-'])[1]"
    delete_all_favorites = "//button[text()='Удалить']"
    confirm_delete_favorites = "//button[text()='Подтвердить']"
    result_of_deleting_favorites = "//span[text()='В избранном пока ничего нет']"

    # Getters
    def get_favorites_counter(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.favorites_counter)))
    # Проверка наличия в разделе "Избранное" 2-х товаров

    def get_select_all_favorites(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.select_all_favorites)))
    # Выделение всех избранных товаров"

    def get_delete_all_favorites(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.delete_all_favorites)))
    # Удаление всех избранных товаров

    def get_confirm_delete_favorites(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.confirm_delete_favorites)))
    # Подтверждение удаления всех избранных товаров

    def get_result_of_deleting_favorites(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.result_of_deleting_favorites)))
    # Проверка очистки раздела "Избранное" по надписи "В избранном пока ничего нет"

    # Actions
    def click_select_all_favorites(self):
        self.get_select_all_favorites().click()
        print("Select All Favorites OK")
        time.sleep(3)

    def click_delete_all_favorites(self):
        self.get_delete_all_favorites().click()
        print("Delete All Favorites OK")
        time.sleep(3)

    def click_confirm_delete_favorites(self):
        self.get_confirm_delete_favorites().click()
        print("Confirm Delete All Favorites OK")
        time.sleep(3)

    # Methods
    # Проверка добавления 2-х товаров в избранное / удаление 2-х товаров из избранного
    def check_favorites_and_delete(self):
        Logger.add_start_step(method="check_favorites_and_delete")
        self.get_current_url()
        self.assert_url("https://www.regard.ru/wishlist")
        self.assert_word(self.get_favorites_counter(), "2 товара")
        self.get_screenshot_2()
        self.click_select_all_favorites()
        self.click_delete_all_favorites()
        self.click_confirm_delete_favorites()
        self.assert_word(self.get_result_of_deleting_favorites(), "В избранном пока ничего нет")
        Logger.add_end_step(url=self.driver.current_url, method="check_favorites_and_delete")
