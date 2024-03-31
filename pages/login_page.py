import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from utilities.logger import Logger


class LoginPage(Base):

    url = 'https://www.regard.ru/'

    # Locators
    authorization_button = "//span[text()='Кабинет']"
    mail_user = "//input[@name='login']"
    password_user = "//input[@name='password']"
    login_button = "//button[text()='Войти']"
    profile_button = "//div[contains(text(), 'G')]"

    # Getters
    def get_authorization_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.authorization_button)))
    # Клик на кнопку "Кабинет"

    def get_mail_user(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.mail_user)))
    # Ввод почты пользователя

    def get_password_user(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.password_user)))
    # Ввод пароля пользователя

    def get_login_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.login_button)))
    # Клик на кнопку "Войти"

    def get_profile_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.profile_button)))
    # Проверка успешной авторизации

    # Actions
    def click_authorization_button(self):
        self.get_authorization_button().click()
        print("Click Authorization Button")
        time.sleep(3)

    def input_mail_user(self, mail_user):
        self.get_mail_user().send_keys(mail_user)
        print("Input Mail User")
        time.sleep(3)

    def input_password_user(self, password_user):
        self.get_password_user().send_keys(password_user)
        print("Input Password User")
        time.sleep(3)

    def click_login_button(self):
        self.get_login_button().click()
        print("Click Login Button")
        time.sleep(3)

    # Methods
    def authorization(self):
        Logger.add_start_step(method="authorization")
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.click_authorization_button()
        self.input_mail_user("mzlotnikov@mail.ru")
        self.input_password_user("Test12345")
        self.click_login_button()
        self.get_current_url()
        self.assert_word(self.get_profile_button(), "G")
        Logger.add_end_step(url=self.driver.current_url, method="authorization")
