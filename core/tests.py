from django.test import TestCase, Client
from django.urls import reverse
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from django.contrib.auth.models import User
from message.models import *
from time import sleep


class AllpageTestCase(TestCase):
    def setUp(self):
        c = Client()
        self.response = c.get("/")


    def test_open_allpage_200_OK(self):
        self.assertEqual(self.response.status_code, 200)

    def test_open_allpage_200_fail(self):
        self.assertNotEqual(self.response.status_code, 404)


class LoginTestCase(TestCase):

    def test_login_OK(self):
        driver = webdriver.Firefox()
        driver.get("localhost:8000")
        username_input = driver.find_element_by_name("username")
        username_input.send_keys("Mick")
        password_input = driver.find_element_by_name("password")
        password_input.send_keys("mick1qa2ws")
        password_input.send_keys(Keys.RETURN)
        sleep(2)
        driver.find_element_by_xpath("//a[@href='/message/']").click()
        driver.find_element_by_xpath("//a[@href='/create-new/']").click()
        sleep(1)
        driver.close()

    def test_message_feedback(self):
        driver = webdriver.Firefox()
        driver.get("localhost:8000")
        username_input = driver.find_element_by_name("username")
        username_input.send_keys("Mail")
        password_input = driver.find_element_by_name("password")
        password_input.send_keys("mail1q2w3e")
        password_input.send_keys(Keys.RETURN)
        sleep(2)
        driver.find_element_by_xpath("//a[@href='/feedback/create/']").click()  
        text_input = driver.find_element_by_name("text")
        text_input.send_keys("Improve your tests!")
        text_input.send_keys(Keys.RETURN)
        driver.find_element_by_name("add_feedback_btn").click()
        sleep(2)
        driver.close()    
