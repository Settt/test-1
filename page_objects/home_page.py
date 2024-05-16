from selenium import webdriver
from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage


class HomePage(BasePage):
    def open(self):
        self._driver.get("https://guest:welcome2qauto@qauto.forstudy.space/")

    def click_guest_login_button(self):
        self._driver.find_element(
            By.XPATH, "//button[@class='header-link -guest']"
        ).click()
