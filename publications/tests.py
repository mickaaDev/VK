from django.test import TestCase, Client
from django.urls import reverse
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep





class AuthTestCase(TestCase):
    def test_load_page_success(self):
        driver = webdriver.Firefox()
        driver.get("localhost:8000")
        username_input = driver.find_element_by_name("username")
        username_input.send_keys("Job")
        password_input = driver.find_element_by_name("password")
        password_input.send_keys("job1q2w3e")
        password_input.send_keys(Keys.RETURN)
        sleep(2)
        driver.close()



