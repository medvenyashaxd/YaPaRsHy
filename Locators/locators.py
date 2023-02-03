from selenium.webdriver.common.by import By


class LocatorsYandexSearchCatalog:
    SEARCH_FIELD = (By.CSS_SELECTOR, 'input[name="offerNameOrSku"]')
    SKU = (By.CSS_SELECTOR, 'span[class="style-sku___vuyKz"]')
