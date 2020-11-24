from django.test import TestCase, Client
from django.urls import reverse

class NewspageTestCase(TestCase):
    
    def setUp(self):
        c = Client()
        self.response = c.get("/")



    def test_news_page_200_OK(self):
        self.assertEqual(self.response.status_code, 302)
        self.assertEqual(self.response.url, reverse())


    def test_open_news_200_fail(self):
        self.assertNotEqual(self.response.status_code, 200)













# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from time import sleep


# driver = webdriver.Chrome()
# driver.get("http://127.0.0.1:8000/")
# element = driver.find_element_by_id("id_username")
# sleep(5)



# driver.close()