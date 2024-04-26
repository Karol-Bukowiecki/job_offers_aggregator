import pytest
from selenium import webdriver
from pages.jjit_main_page import JustJoinItMainPage
from pages.jjit_offert_page import JustJoinItOfferPage


class TestJustJoinIt:

    @pytest.fixture()
    def setup(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(15)
        self.driver.maximize_window()
        yield
        self.driver.quit()

    def test_just_join_it(self, setup):
        self.driver.get("https://justjoin.it/all-locations/testing/remote_yes")
        jj_main_page = JustJoinItMainPage(self.driver)
        remote_switch_status = jj_main_page.jjitFilterOffers()
        assert remote_switch_status == True
        jj_offer_page = JustJoinItOfferPage(self.driver)
        offer_list = jj_main_page.jjitfindOfferLinks()
        jj_offer_page.jjitOpenOfferDetail(offer_list)
