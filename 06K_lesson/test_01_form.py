import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_form_submission(browser):
    url = "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
    browser.get(url)

    browser.find_element(By.CSS_SELECTOR, "input[name='first-name']").send_keys("Иван")
    browser.find_element(By.CSS_SELECTOR, "input[name='last-name']").send_keys("Петров")
    browser.find_element(By.CSS_SELECTOR, "input[name='address']").send_keys("Ленина, 55-3")
    browser.find_element(By.CSS_SELECTOR, "input[name='e-mail']").send_keys("test@skypro.com")
    browser.find_element(By.CSS_SELECTOR, "input[name='phone']").send_keys("+7985899998787")
    browser.find_element(By.CSS_SELECTOR, "input[name='city']").send_keys("Москва")
    browser.find_element(By.CSS_SELECTOR, "input[name='country']").send_keys("Россия")
    browser.find_element(By.CSS_SELECTOR, "input[name='job-position']").send_keys("QA")
    browser.find_element(By.CSS_SELECTOR, "input[name='company']").send_keys("SkyPro")

    browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    zip_code_field = browser.find_element(
        By.CSS_SELECTOR,
        "body > main > div > form > div:nth-child(3) > div:nth-child(2) > label > input"
    )
    assert "border-danger" in zip_code_field.get_attribute("class")

    fields_css_selectors = [
        "input[name='first-name']",
        "input[name='last-name']",
        "input[name='address']",
        "input[name='e-mail']",
        "input[name='phone']",
        "input[name='city']",
        "input[name='country']",
        "input[name='job-position']",
        "input[name='company']"
    ]

    for field_css_selector in fields_css_selectors:
        field = browser.find_element(By.CSS_SELECTOR, field_css_selector)
        assert "border-success" in field.get_attribute("class")
