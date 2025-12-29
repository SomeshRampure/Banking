from behave import given
from selenium import webdriver
from pages.login_page import LoginPage

@given('I am on the banking login page')
def step_login_page(context):
    context.driver = webdriver.Chrome()
    context.login_page = LoginPage(context.driver)
    context.login_page.go_to_url("https://parabank.parasoft.com/parabank/index.htm")

@when('I enter valid crendentails')
def setp_valid_credentails(context):