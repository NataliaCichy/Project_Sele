import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

#Test date
valid_name = "Maksym"
valid_surname = "Kurylowycz"
valid_email = "maksym.kurylowycz@wp.pl"
invalid_phone = "55599955"
dateofbirth_year = "1984"
dateofbirth_month = "11" #December
#dateofbirth_day = "20"
gender = "mężczyzna"
citizenship_chosen = "ukraińskie"

class LuxMedRegistration(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(60)

    def testInvalidPhoneNumber(self):
        driver = self.driver

        #Step 1. Go to the website https://www.luxmed.pl/
        driver.get("https://www.luxmed.pl/")

        #Step 2. Click on "Zaloz konto"
        registration_btn = driver.find_element_by_xpath('//*[@class="reg"]')
        registration_btn.click()

        #Step 3. Enter first name
        name_field = driver.find_element_by_id('FirstName')
        name_field.send_keys(valid_name)

        #Step 4. Enter last name
        surname_field = driver.find_element_by_id('LastName')
        surname_field.send_keys(valid_surname)

        #Step 5. Enter an e-mail address
        email_field = driver.find_element_by_id('Email')
        email_field.send_keys(valid_email)

        #Step 6. Enter invalid phone number (1 digit missing)
        phone_field = driver.find_element_by_id('PhoneNumber')
        phone_field.send_keys(invalid_phone)

        #Step 7. Select date of birth
        dateofbirth_field = driver.find_element_by_id('rangePicker')
        dateofbirth_field.click()

        year = Select(driver.find_element_by_xpath('//*[@class="yearselect"]'))
        year.select_by_value(dateofbirth_year)

        month = Select(driver.find_element_by_xpath('//*[@class="monthselect"]'))
        month.select_by_value(dateofbirth_month)

        #days = driver.find_elements_by_xpath('//*[@class="table-condensed"]')
        day = driver.find_element_by_xpath('//table/tbody/tr[4]/td[4]')
        day.click()
        #days_list = days.find_elements_by_tag_name('tr')
        #/html/body/div[7]/div[1]/div[2]/table/tbody/tr[3]/td[2]
        #for tr in days_list:
        #    day = tr.find_elements_by_tag_name('td')
        #    for td in day:
        #        day_once = td.find_element_by_xpath('//tr/td[@class="available"]')
        #        if  dateofbirth_day in day_once.get_attribute("innerText"):
        #        #day.location_once_scrolled_into_view
        #            day_once.click()
        #            break


        #Step 8. Choose gender
        sex = driver.find_element_by_css_selector('span.caption')

        sex = driver.find_element_by_xpath('//div[@class="_select widget undefined"]')
        sex.click()
        if gender == "kobieta":
            driver.find_element_by_xpath('//*[@data-value="1"]').click()
        elif gender == "mężczyzna":
            driver.find_element_by_xpath('//*[@data-value="2"]').click()


        #Step 9. Click on "Obcokrajowiec"
        foreigner = driver.find_element_by_name('Foreigner')
        foreigner.click()


        #Step 10. Choose citizenship
        citizenship = driver.find_element_by_xpath('//div[@data-autocomplete="True"]/span')
        citizenship.click()

        citizenship_input = driver.find_element_by_xpath('//input[@class="search-select"]')
        citizenship_input.click()
        citizenship_input.send_keys(citizenship_chosen)
        driver.find_element_by_id('__selectOptions').click()

        #Step 11. Accept the privacy policy and regulations
        driver.find_element_by_xpath('//input[@class="select_white"]').click()

        #Step 12. Click on "ZALOZ KONTO"
        driver.find_element_by_id('buttonFormSubmit').click()
        driver.get_screenshot_as_file('Whether the test works?.png')

        ####### CHECKING THE EXPECTED RESULT ############
        error_notices = driver.find_elements_by_xpath('//*[@id="CreateAccountFieldError"]')


        visible_error_notices = list()
        for error in error_notices:
            if error.is_displayed():
                visible_error_notices.append(error.text)

        ####### TEST #########
        assert(len(visible_error_notices)) == 1
        assert visible_error_notices[0] == "Nieprawidłowy numer telefonu"
        self.assertEqual(visible_error_notices[0], "Nieprawidłowy numer telefonu", msg="Nie zgadzaja sie wyswietlane bledy")


    def tearDown(self):
        self.driver.quit()


if __name__=="__main__":
    unittest.main(verbosity=2)
