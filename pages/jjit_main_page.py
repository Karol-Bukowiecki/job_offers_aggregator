from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException
import time


class JustJoinItMainPage:

    def __init__(self, driver):
        self.driver = driver
        self.cookies_btn_id = "cookiescript_accept"
        self.more_filters_btn_xpath = "//button[contains(.,'More filters')]"
        self.mid_experience_checkbox_xpath = "//input[@value='mid']"
        self.permanent_employment_type_checkbox_xpath = "//input[@value='permanent']"
        self.show_offers_btn_id = "dialog-actions-confirm"
        self.job_offers_links_xpath = "//a[@href]"
        self.remote_switch_xpath = "//input[@class='PrivateSwitchBase-input MuiSwitch-input css-1m9pwf3']"

    def jjitFilterOffers(self):
        self.driver.find_element(By.ID, self.cookies_btn_id).click()
        self.driver.find_element(By.XPATH, self.more_filters_btn_xpath).click()
        self.driver.find_element(By.XPATH, self.mid_experience_checkbox_xpath).click()
        self.driver.find_element(By.XPATH, self.permanent_employment_type_checkbox_xpath).click()
        self.driver.find_element(By.ID, self.show_offers_btn_id).click()
        remote_switch_status = self.driver.find_element(By.XPATH, self.remote_switch_xpath).is_selected()
        #remote_switch_status = remote_switch.is_selected()
        return remote_switch_status

    def jjitfindOfferLinks(self):
        links_list = []
        time.sleep(3)
        while True:
            links = self.driver.find_elements(By.XPATH, self.job_offers_links_xpath)
            last_height = self.driver.execute_script("return document.body.scrollHeight")
            try:
                for link in links:
                    if link.get_attribute('href').__contains__("offers"):
                        links_list.append(link.get_attribute('href'))
            except StaleElementReferenceException:
                pass
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
            time.sleep(1)
            new_height = self.driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break

        return links_list
