import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as Ec
from Locators.locators import LocatorsYandexSearchCatalog


class Parser():
    def executor(self, locators=LocatorsYandexSearchCatalog):
        driver_path = webdriver.Chrome('webdriver\chromedriver.exe')
        options = Options()
        options.add_argument(r"user-data-dir=C:\Users\Treid Computers\AppData\Local\Google\Chrome\User Data\Default")

        driver = webdriver.Chrome(executable_path=driver_path, options=options)

        main_url_search = 'https://partner.market.yandex.ru/business/1030699/assortment?campaignId=22031686&activeTab=mappings&mappingChangePeriod=all&mappingChecking=processed'

        driver.get(main_url_search)

        len_search_data = len(search_data)
        for l in range(len_search_data):
            Wait(driver, timeout=15).until(Ec.visibility_of_element_located(locator=locators.SEARCH_FIELD))
            time.sleep(4)

            with open('site.html', 'w', encoding='utf-8') as file:
                file.write(driver.page_source)
            file.close()

            self.element_is_present(loc_main.SEARCH_FIELD).send_keys(u'\ue009' + u'\ue003')
