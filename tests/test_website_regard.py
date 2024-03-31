import time

import pytest
from selenium import webdriver

from pages.add_comparison_page import AddComparisonPage
from pages.add_favorites_page import AddFavoritesPage
from pages.buy_page import BuyPage
from pages.catalog_page import CatalogPage
from pages.login_page import LoginPage
from pages.product_page import ProductPage


# 1. Открытие сайта regard.ru
# 2. Авторизация пользователя на сайте
# 3. Применение фильтров каталога для выбора 1-го товара
# 4. Переход на страницу выбранного товара и добавление товара в корзину со страницы выбранного товара
# 5. Проверка наличия товара в корзине / удаление товара из корзины

@pytest.mark.run(order=3)
def test_adding_product_to_cart(set_up, set_group):
    driver = webdriver.Chrome()

    print("Start Test 3")
    time.sleep(5)

    """AUTHORIZATION"""
    lp = LoginPage(driver)
    lp.authorization()
    print("Authorization Successful!")

    """PRODUCT SELECTION"""
    cp = CatalogPage(driver)
    cp.product_selection()
    print("Product Category Filter GOOD!")

    """PRODUCT CARD"""
    pp = ProductPage(driver)
    pp.product_card()
    print("Product Card GOOD!")

    """CART"""
    bp = BuyPage(driver)
    bp.cart()
    print("Cart GOOD!")

    print("Finish Test 3")
    time.sleep(3)


# 1. Открытие сайта regard.ru
# 2. Авторизация пользователя на сайте
# 3. Применение фильтров каталога для выбора товаров
# 4. Добавление 2-х товаров в избранное
# 5. Проверка наличия 2-х товаров в избранных / удаление всех товаров из избранных

@pytest.mark.run(order=1)
def test_adding_product_to_favorites(set_up, set_group):
    driver = webdriver.Chrome()

    print("Start Test 1")
    time.sleep(5)

    """AUTHORIZATION"""
    lp = LoginPage(driver)
    lp.authorization()
    print("Authorization Successful!")

    """SELECT FAVORITES"""
    cp = CatalogPage(driver)
    cp.select_favorites()
    print("Selecting Favorites GOOD!")

    """FAVORITES PAGE"""
    afp = AddFavoritesPage(driver)
    afp.check_favorites_and_delete()
    print("Adding Favorites GOOD!")

    print("Finish Test 1")
    time.sleep(3)


# 1. Открытие сайта regard.ru
# 2. Авторизация пользователя на сайте
# 3. Применение фильтров каталога для выбора товаров
# 4. Добавление 2-х товаров к сравнению
# 5. Проверка наличия 2-х товаров в разделе "Сравнение" / удаление всех товаров из сравнения

@pytest.mark.run(order=2)
def test_adding_product_to_comparison(set_up, set_group):
    driver = webdriver.Chrome()

    print("Start Test 2")
    time.sleep(5)

    """AUTHORIZATION"""
    lp = LoginPage(driver)
    lp.authorization()
    print("Authorization Successful!")

    """SELECT COMPARISON"""
    cp = CatalogPage(driver)
    cp.select_comparison()
    print("Selecting Comparison GOOD!")

    """COMPARISON PAGE"""
    acp = AddComparisonPage(driver)
    acp.check_comparison_and_delete()
    print("Adding Comparison GOOD!")

    print("Finish Test 2")
    time.sleep(3)
