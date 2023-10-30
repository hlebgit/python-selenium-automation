from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# Exercise 2
driver.get('https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_ya_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&')

sleep(5)

amazon_logo = driver.find_element(By.XPATH, "//i[@aria-label='Amazon']")
email_field = driver.find_element(By.ID, "ap_email")
continue_button = driver.find_element(By.XPATH, "//input[@id='continue']")
conditions_of_use_link = driver.find_element(By.XPATH, "//a[contains(@href, '/gp/help/customer/display.html/ref=ap_desktop_footer_cou?ie=UTF8&nodeId=508088')]")
privacy_notice_link = driver.find_element(By.XPATH, "//a[contains(@href, '/gp/help/customer/display.html/ref=ap_desktop_footer_privacy_notice?ie=UTF8&nodeId=468496')]")
need_help_link = driver.find_element(By.XPATH, "//div[@class='a-row a-expander-container a-expander-inline-container']//span[@class='a-expander-prompt']")
forgot_your_password_link = driver.find_element(By.ID, "auth-fpp-link-bottom")
other_issues_with_sign_in_link = driver.find_element(By.ID, "ap-other-signin-issues-link")
create_your_amazon_account_button = driver.find_element(By.ID, "createAccountSubmit")

driver.quit()


