from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from Locators.locators import LocatorsYandexSearchCatalog
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as Ec


class Parser:

    def executor(self, locators=LocatorsYandexSearchCatalog):

        search_data = (
                        '30501DBS',
                        '43420DBS',
                        '43546DBS',
                        '43894DBS',
                        '43993DBS',
                        '44031DBS',
                        '44032DBS',
                        '44114DBS',
                        '44227DBS',
                        '44394DBS',
                        '44416DBS',
                        '44598DBS',
                        '44849DBS',
                        '44954DBS',
                        '45112DBS',
                        '45229DBS',
                        '45230DBS',
                        '45231DBS',
                        '45247DBS',
                        '46167DBS',
                        '46178DBS',
                        '47231DBS',
                        '49886DBS',
                        '50078DBS',
                        '51083DBS',
                        '51845DBS',
                        '52093DBS',
                        '52121DBS',
                        # '57368DBS',
                        '62057DBS',
                        '73655DBS',
                        '73781DBS',
                        '73854DBS',
                        '74551DBS',
                        '8867DBS',
                        '945601DBS',
                        '946262DBS',
                        '946287DBS',
                        '946919DBS',
                        '946927DBS',
                        '947224DBS',
                        '949802DBS',
                        '951538DBS',
                        '951596DBS',
                        '953051DBS',
                        '958011DBS',
                        '960172DBS',
                        '965866DBS',
                        '983495DBS',
                        '998708DBS',
        )

        driver_path = ('webdriver\chromedriver.exe')
        options = Options()
        options.add_argument(r"user-data-dir=C:\Users\xmedv\AppData\Local\Google\Chrome\User Data\Default")

        driver = webdriver.Chrome(executable_path=driver_path, options=options)

        main_url_search = 'https://partner.market.yandex.ru/business/1030699/assortment?campaignId=22031686&activeTab=mappings&mappingChangePeriod=all&mappingChecking=processed'

        driver.get(main_url_search)

        len_search_data = len(search_data)
        print(len_search_data)
        for l in range(len_search_data):
            Wait(driver, timeout=20).until(Ec.presence_of_element_located(locator=locators.SEARCH_FIELD)).send_keys(
                search_data[l])

            Wait(driver, timeout=20).until(Ec.text_to_be_present_in_element(locator=locators.SKU, text_=search_data[l]))

            # with open('site.html', 'w', encoding='utf-8') as file:
            #     file.write(driver.page_source)
            # file.close()

            Wait(driver, timeout=20).until(Ec.visibility_of_element_located(locator=locators.SEARCH_FIELD)) \
                .send_keys(u'\ue009' + u'\ue003')


if __name__ == '__main__':
    Parser().executor()