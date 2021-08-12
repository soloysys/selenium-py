from behave import *

use_step_matcher('re')

@when('I open the login website "([^"]*)"')
def step_register1(context, url):
    context.driver.get(url)

@then('I expect the title is "([^"]*)"')
def step_register2(context, title_name):
    title = context.driver.title
    assert title_name in title

@when('I set the useremail as "([^"]*)"')
def step_login(context,useremail):
    context.driver.find_element_by_xpath('user_email').send_keys(useremail)

