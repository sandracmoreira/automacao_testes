from selenium.webdriver.common.by import By

class HighlightsPage:
    URL = "https://www.pucminas.br/destaques/Paginas/default.aspx"

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)

    def page_title(self):
        return self.driver.title

    def highlights_list(self):
        # Ajuste este seletor conforme a estrutura real dos destaques
        return self.driver.find_elements(By.CSS_SELECTOR, ".ms-list-itemLink, .destaque-item, .ms-list-item, .highlight")

    def has_highlights(self):
        return len(self.highlights_list()) > 0
