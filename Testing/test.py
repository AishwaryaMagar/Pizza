from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
import time

class TestLogin(StaticLiveServerTestCase):
    def setUp(self):
        global driver
        self.driver = webdriver.Chrome('Testing/chromedriver.exe')
        self.driver.get('http://127.0.0.1:8000/')
        self.driver.maximize_window()

    def test(self):
        
        #SIGN UP
        text = self.driver.find_element_by_name('heading1').text
        if text == 'PIZZA ORDERING SYSTEM':
            print("HOME PAGE SUCCESFULLY LOADED")
        
        self.driver.find_element_by_name('username').send_keys('Soham')
        self.driver.find_element_by_name('password').send_keys('soham')
        self.driver.find_element_by_name('phoneno').send_keys('9420169458')
        self.driver.find_element_by_name('email').send_keys('soham@gmail.com')
        time.sleep(1)
        self.driver.find_element_by_name('btnK').click()
        time.sleep(1)
        print("SIGN UP SUCCESFULL")

        #LOGIN

        self.driver.find_element_by_partial_link_text("Login")
        self.driver.find_element_by_xpath('//a[contains(@href,"/loginuser")]')
        self.driver.find_element_by_name('LoginBtn').click()
        
        text1 = self.driver.find_element_by_name('headingLog').text
        if text1 == 'Login':
            print("LOGIN PAGE SUCCESFULLY LOADED")
    
        self.driver.find_element_by_name('username').send_keys('Soham')
        self.driver.find_element_by_name('password').send_keys('soham')
        time.sleep(1)
        self.driver.find_element_by_name('logBtn').click()
        time.sleep(1)
        print("LOGIN SUCCESFULL")

        #SELECT PIZZA
        
        text2 = self.driver.find_element_by_name('view').text
        if text2 == 'View My Orders':
            print("VIEW ORDER PAGE SUCCESFULLY LOADED")

        self.driver.find_element_by_name("23").send_keys("1") 
        self.driver.find_element_by_name("23").click()
        time.sleep(2)
        self.driver.find_element_by_name("25").send_keys("3") 
        self.driver.find_element_by_name("25").click()
        time.sleep(2)
        print("SELECT PIZZA SUCCESFULL")

        #Place Order
        self.driver.find_element_by_name("address").send_keys('Pune')
        self.driver.find_element_by_name("placeorder").click()
        time.sleep(2)
        print("PLACE ORDER SUCCESFULL")
    
        #view orders
        
        self.driver.find_element_by_partial_link_text("View My Orders")
        self.driver.find_element_by_xpath('//a[contains(@href,"/userorder")]')
        self.driver.find_element_by_name('view').click()
        time.sleep(2)
        text3 = self.driver.find_element_by_name('myorder').text
        if text3 == 'My Orders':
            print("My Order PAGE SUCCESFULLY LOADED")
        print("VIEW ORDER SUCCESFULL")

        self.driver.find_element_by_partial_link_text("Welcome")
        self.driver.find_element_by_xpath('//a[contains(@href,"http://127.0.0.1:8000/userorder/")]')
        self.driver.find_element_by_name('wel').click()

        text4 = self.driver.find_element_by_name('myorder').text
        if text4 == 'My Orders':
            print("My Order PAGE REFRESH SUCCESFULLY LOADED")
        time.sleep(2)
        print("REFRESH SUCCESFULL")

        #back to place order
        self.driver.find_element_by_partial_link_text("Back")
        self.driver.find_element_by_xpath('//a[contains(@href,"/customer/welcome/")]')
        self.driver.find_element_by_name('bk').click()
        time.sleep(2)
        print("BACK SUCCESFULL")
        
        #Logout
        self.driver.find_element_by_partial_link_text("Logout")
        self.driver.find_element_by_xpath('//a[contains(@href,"/userlogout/")]')
        self.driver.find_element_by_name('logout').click()
        time.sleep(2)

        text6 = self.driver.find_element_by_name('headingLog').text
        if text6 == 'Login':
            print("LOGIN PAGE SUCCESFULLY LOADED AFTER LOGOUT")

        print("LOGOUT SUCCESFULL")
        
    def tearDown(self):
        self.driver.close()
    