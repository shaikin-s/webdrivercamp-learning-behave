from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class Base:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    def click(self, xpath):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
