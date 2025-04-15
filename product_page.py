from selenium.webdriver.common.by import By
class ProductPage:
    def __init__(self, driver):
        self.driver = driver

    def click_product(self):
        self.driver.find_element(By.XPATH,"//a[@href='/products']").click()

    def search_product(self, term):
        self.driver.find_element(By.XPATH, "//input[@id='search_product']").send_keys(term)

    def click_search(self):
        self.driver.find_element(By.XPATH,"//button[@id='submit_search']").click()

    def select_product(self):
        self.driver.find_element(By.XPATH, "/html[1]/body[1]/section[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/ul[1]/li[1]/a[1]").click()


    def add_to_cart(self):
        self.driver.find_element(By.XPATH, "//button[@type='button']").click()

    def close_modal(self):
        self.driver.find_element(By.XPATH, "//button[@class='btn btn-success close-modal btn-block']").click()
