from django.test import TestCase

# Create your tests here.
# Generated by Selenium IDE
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class TestDefaultSuite():
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self):
        self.driver.quit()

    def wait_for_window(self, timeout=2):
        time.sleep(round(timeout / 1000))
        wh_now = self.driver.window_handles
        wh_then = self.vars["window_handles"]
        if len(wh_now) > len(wh_then):
            return set(wh_now).difference(set(wh_then)).pop()

    def test_getAirQualityData(self):
        self.driver.get("https://tqsfrontend.herokuapp.com/")
        self.driver.set_window_size(838, 573)
        self.vars["window_handles"] = self.driver.window_handles
        self.driver.find_element(By.LINK_TEXT, "See air quality").click()
        self.vars["win1916"] = self.wait_for_window(2000)
        self.driver.switch_to.window(self.vars["win1916"])
        self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(7) > td:nth-child(1)").click()
        self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(7) > td:nth-child(1)").click()
        element = self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(7) > td:nth-child(1)")
        actions = ActionChains(self.driver)
        actions.double_click(element).perform()
        self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(7) > td:nth-child(1)").click()
        self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(6) > td:nth-child(1)").click()
        self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(5) > td:nth-child(1)").click()
        self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(4) > td:nth-child(1)").click()
        self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(3) > td:nth-child(1)").click()
        self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(2) > td:nth-child(1)").click()
        self.driver.find_element(By.CSS_SELECTOR, "tbody").click()
        self.driver.find_element(By.CSS_SELECTOR, "h1").click()
        self.driver.find_element(By.CSS_SELECTOR, "h1").click()
        element = self.driver.find_element(By.CSS_SELECTOR, "h1")
        actions = ActionChains(self.driver)
        actions.double_click(element).perform()
        self.driver.find_element(By.CSS_SELECTOR, "h1").click()
        self.driver.find_element(By.CSS_SELECTOR, "h1").click()

