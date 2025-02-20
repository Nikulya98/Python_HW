import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data_page import DataPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_fill_form(driver):
    page = DataPage(driver)
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
    )

    page.fill_form(
        first_name="Иван",
        last_name="Петров",
        address="Ленина, 55-3",
        email="test@skypro.com",
        phone="+7985899998787",
        city="Москва",
        country="Россия",
        job_position="QA",
        company="SkyPro"
    )

    page.submit_form()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "zip-code"))
    )

    WebDriverWait(driver, 10).until(
        EC.attribute_contains((By.NAME, "zip-code"), "class", "is-invalid")
    )

    assert "is-invalid" in page.get_element_attribute(
        page.ZIP_CODE, "class"
    )
    assert "is-valid" in page.get_element_attribute(
        page.FIRST_NAME, "class"
    )
    assert "is-valid" in page.get_element_attribute(
        page.LAST_NAME, "class"
    )
    assert "is-valid" in page.get_element_attribute(
        page.ADDRESS, "class"
    )
    assert "is-valid" in page.get_element_attribute(
        page.EMAIL, "class"
    )
    assert "is-valid" in page.get_element_attribute(
        page.PHONE, "class"
    )
    assert "is-valid" in page.get_element_attribute(
        page.CITY, "class"
    )
    assert "is-valid" in page.get_element_attribute(
        page.COUNTRY, "class"
    )
    assert "is-valid" in page.get_element_attribute(
        page.JOB_POSITION, "class"
    )
    assert "is-valid" in page.get_element_attribute(
        page.COMPANY, "class"
    )
