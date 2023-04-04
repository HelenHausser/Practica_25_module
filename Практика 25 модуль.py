import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="function")
def browser():
    # Инициализация браузера
    driver = webdriver.Chrome()
    # Открытие страницы
    driver.get("https://petfriends.skillfactory.ru/my_pets")
    yield driver
    # Закрытие браузера после завершения теста
    driver.quit()


def test_all_pets_are_present(browser):
    # Проверка, что присутствуют все питомцы
    pet_names = [pet.text for pet in browser.find_elements(By.XPATH, "//table[@id='all_my_pets']/tbody/tr/td[1]")]
    assert len(pet_names) == 6, "Not all pets are present"


def test_at_least_half_of_pets_have_photos(browser):
    # Проверка, что у половины питомцев есть фото
    pet_photos = browser.find_elements(By.XPATH, "//table[@id='all_my_pets']/tbody/tr/td[1]/img")
    assert len(pet_photos) >= 3, "Less than half of the pets have photos"


def test_all_pets_have_name_age_and_breed(browser):
    # Проверка, что у всех питомцев есть имя, возраст и порода
    pet_info = browser.find_elements(By.XPATH, "//table[@id='all_my_pets']/tbody/tr/td[2]")
    for info in pet_info:
        assert "Name" in info.text and "Age" in info.text and "Breed" in info.text, "Not all pets have name, age, and breed"


def test_all_pets_have_different_names(browser):
    # Проверка, что у всех питомцев разные имена
    pet_names = [pet.text for pet in browser.find_elements(By.XPATH, "//table[@id='all_my_pets']/tbody/tr/td[1]")]
    assert len(set(pet_names)) == len(pet_names), "Not all pets have different names"


def test_no_duplicate_pets(browser):
    # Проверка, что в списке нет повторяющихся питомцев
    pet_names = [pet.text for pet in browser.find_elements(By.XPATH, "//table[@id='all_my_pets']/tbody/tr/td[1]")]
    for name in pet_names:
        assert pet_names.count(name) == 1, "Duplicate pet found"
