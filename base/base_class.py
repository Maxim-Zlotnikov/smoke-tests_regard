import datetime


class Base:

    def __init__(self, driver):
        self.driver = driver

    """Method get current url"""
    def get_current_url(self):
        get_url = self.driver.current_url
        print("Current url " + get_url)

    """Method assert word"""
    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print("Good value word")

    """Method assert url"""
    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print("Good value url")

    """Method screenshot"""
    def get_screenshot_1(self):
        now_date = datetime.datetime.now().strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = 'screen_cart' + now_date + '.png'
        self.driver.save_screenshot(name_screenshot)

    def get_screenshot_2(self):
        now_date = datetime.datetime.now().strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = 'screen_favorites' + now_date + '.png'
        self.driver.save_screenshot(name_screenshot)

    def get_screenshot_3(self):
        now_date = datetime.datetime.now().strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = 'screen_comparison' + now_date + '.png'
        self.driver.save_screenshot(name_screenshot)
