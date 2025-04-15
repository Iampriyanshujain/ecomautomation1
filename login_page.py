from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def enter_email(self, email):
        email_input = self.driver.find_element(By.XPATH, "//input[@data-qa='login-email']")
        email_input.send_keys(email)

    def enter_password(self, password):
        password_input = self.driver.find_element(By.XPATH, "//input[@placeholder='Password']")
        password_input.send_keys(password)

    def click_login(self):
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()