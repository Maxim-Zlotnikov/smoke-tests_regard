import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from utilities.logger import Logger


class AddComparisonPage(Base):

    # Locators
    comparison_counter = "//div[text()='Мониторы (2)']"
    delete_all_comparison = "//button[@aria-label='Очистить сравнение']"
    confirm_delete_comparison = "//button[text()='Удалить все']"
    result_of_deleting_comparison = "//span[text()='В сравнении пока ничего нет']"

    # Getters
    def get_comparison_counter(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.comparison_counter)))
    # Проверка наличия в разделе "Сравнение" 2-х товаров

    def get_delete_all_comparison(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.delete_all_comparison)))
    # Удаление всех добавленных к сравнению товаров

    def get_confirm_delete_comparison(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.confirm_delete_comparison)))
    # Подтверждение удаления всех добавленных к сравнению товаров

    def get_result_of_deleting_comparison(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.result_of_deleting_comparison)))
    # Проверка очистки раздела "Сравнение" по надписи "В сравнении пока ничего нет"

    # Actions
    def click_delete_all_comparison(self):
        self.get_delete_all_comparison().click()
        print("Delete All Comparison OK")
        time.sleep(3)

    def click_confirm_delete_comparison(self):
        self.get_confirm_delete_comparison().click()
        print("Confirm Delete All Comparison OK")
        time.sleep(3)

    # Methods
    # Проверка добавления 2-х товаров к сравнению / удаление 2-х товаров из сравнения
    def check_comparison_and_delete(self):
        Logger.add_start_step(method="check_comparison_and_delete")
        self.get_current_url()
        self.assert_url("https://www.regard.ru/compare")
        self.assert_word(self.get_comparison_counter(), "Мониторы (2)")
        self.get_screenshot_3()
        self.click_delete_all_comparison()
        self.click_confirm_delete_comparison()
        self.assert_word(self.get_result_of_deleting_comparison(), "В сравнении пока ничего нет")
        Logger.add_end_step(url=self.driver.current_url, method="check_comparison_and_delete")
