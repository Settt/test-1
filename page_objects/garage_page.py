import time

from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage


class GaragePage(BasePage):
    def assert_guest_message_is_displayed(self):
        header = self._driver.find_element(By.XPATH, "//p[@class='header_bar']")
        assert header.text == "Logged in as guest, any changes will be lost!"

    def click_add_car_button(self):
        self._driver.find_element(
            By.XPATH, "//button[@class='btn btn-primary']"
        ).click()

    def assert_car_in_list(self, expected_car_title):
        car_title = self._driver.find_element(
            By.XPATH, "//li[@class='car-item']//p"
        ).text
        assert car_title == expected_car_title


class AddCarModal(BasePage):
    def select_brand(self, car_brand_name: str):
        time.sleep(1)
        self._driver.find_element(By.XPATH, "//select[@id='addCarBrand']").send_keys(
            car_brand_name
        )

    def select_model(self, car_model_name: str):
        time.sleep(1)
        self._driver.find_element(By.XPATH, "//select[@id='addCarModel']").send_keys(
            car_model_name
        )

    def set_mileage(self, mileage: int):
        self._driver.find_element(By.XPATH, "//input[@id='addCarMileage']").send_keys(
            mileage
        )

    def click_add_button(self):
        self._driver.find_element(
            By.XPATH, "//div[@class='modal-content']//button[@class='btn btn-primary']"
        ).click()
