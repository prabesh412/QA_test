from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

def add_species(self, url):
    self.get(url)
    self.implicitly_wait(5)
    new_species = self.find_element(By.XPATH, "//div[@class='MuiBox-root css-6su6fj']").click()