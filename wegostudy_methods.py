
from time import sleep
import datetime
import wegostudy_locators as locators
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
# driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)



def setUp():
    print(f'launch {locators.app} App')
    print(f'--------------------------------------')
    # make browser full screen
    driver.maximize_window()
    # give browser up to 30 seconds to respond
    driver.implicitly_wait(30)
    # navigate to moodle App website
    driver.get(locators.wegostudy_url)
    # check that  moodle URL and the home page title are as expected
    if driver.current_url == locators.wegostudy_url and driver.title == locators.wegostudy_home_page_title:
        print(f' Yey! {locators.app} App website launched successfully!')
        print(f'{locators.app} Homepage URL: {driver.current_url}, Homepage title; {driver.title}')
        sleep(0.25)
    else:
        print(f'{locators.app} did not launch. Check your code or application!')
        print(f'Current URL: {driver.current_url}, Page title: {driver.title}')
        tearDown()


def tearDown():
    if driver is not None:
        print(f'--------------------------------------')
        print(f'The test is completed at: {datetime.datetime.now()}')
        sleep(1.5)
        driver.close()
        driver.quit()


# def create_account():
#     driver.find_element(By.XPATH, '//a[contains(@class,"z-index__2 montserrat-font")]//b[contains(text(),"CREATE AN ACCOUNT")]').click()
#     sleep(0.75)
#     driver.find_element(By.XPATH, '//span[@id="partner"]').click()
#     sleep(0.75)
#     driver.find_element(By.ID, 'user_partner_detail_attributes_first_name').send_keys(locators.first_name)
#     sleep(0.75)
#     driver.find_element(By.ID, 'user_partner_detail_attributes_last_name').send_keys(locators.last_name)
#     sleep(0.75)
#     driver.find_element(By.ID, 'user_partner_detail_attributes_date_of_birth').send_keys('1')
#     sleep(0.75)
#     driver.find_element(By.ID, 'user_partner_detail_attributes_date_of_birth').send_keys(10 * Keys.BACKSPACE)
#     sleep(0.75)
#     driver.find_element(By.ID, 'user_partner_detail_attributes_date_of_birth').send_keys(locators.date_of_birth)
#     sleep(0.75)
#     driver.find_element(By.ID, 'select2-user_partner_detail_attributes_country_of_citizenship-container').click()
#     sleep(0.75)
#     driver.find_element(By.CLASS_NAME, 'select2-search__field').send_keys(locators.country)
#     sleep(0.75)
#     driver.find_element(By.CLASS_NAME, 'select2-search__field').send_keys(Keys.RETURN)
#     sleep(0.75)
#     driver.find_element(By.ID, 'partner_phone_number').send_keys(locators.phone_number)
#     sleep(0.75)
#
#     driver.find_element(By.ID, 'user_partner_detail_attributes_address_attributes_mailing_address').send_keys(locators.address)
#     sleep(0.75)
#     driver.find_element(By.ID, 'user_partner_detail_attributes_address_attributes_mailing_address').send_keys(Keys.RETURN)
#     sleep(0.75)
#     driver.find_element(By.LINK_TEXT, 'Country').click()
#     sleep(0.75)
#     driver.find_element(By.XPATH, '//*[@id="user_partner_detail_attributes_address_attributes_country_chosen"]/div/div/input').send_keys(f'Canada{Keys.ENTER}')
#     sleep(0.75)
#     driver.find_element(By.ID,'user_partner_detail_attributes_address_attributes_state_chosen').click()
#     sleep(0.75)
#     driver.find_element(By.XPATH, '//*[@id="user_partner_detail_attributes_address_attributes_state_chosen"]/div/ul/li[2]').click()
#     sleep(0.75)
#     driver.find_element(By.ID, 'user_partner_detail_attributes_address_attributes_city_chosen').click()
#     sleep(0.75)
#     driver.find_element(By.XPATH, '//*[@id="user_partner_detail_attributes_address_attributes_city_chosen"]/div/ul/li[4]').click()
#     sleep(0.75)
#     driver.find_element(By.ID, 'user_partner_detail_attributes_address_attributes_zip_code').send_keys(locators.postalcode)
#     sleep(0.75)
#     driver.find_element(By.XPATH, '//div[@id="form_partner"]//input[@id="user_email"]').send_keys(locators.admin_email)
#     sleep(0.75)
#     driver.find_element(By.ID, 'user_password').send_keys(locators.admin_password)
#     sleep(0.75)
#     driver.find_element(By.ID, 'user_password_confirmation').send_keys(locators.admin_password)
#     sleep(0.75)



def log_in():
    if driver.current_url == locators.wegostudy_url:
        driver.find_element(By.XPATH, '//b[normalize-space()="LOGIN"]').click()
        sleep(0.75)
        driver.find_element(By.ID, 'user_email').send_keys(locators.admin_email)
        sleep(0.75)
        driver.find_element(By.ID, 'user_password').send_keys(locators.admin_password)
        sleep(0.75)
        driver.find_element(By.XPATH, '//input[@name="commit"]').click()
        sleep(1.25)
        driver.find_element(By.ID, 'authentication-popup').is_displayed()



def create_new_student():
        print(f'********* Create  new user ***********************')
        driver.find_element(By.XPATH,'//span[normalize-space()="My WeGoStudy"]').click()
        # driver.find_element(By.CSS_SELECTOR, 'a[aria-expanded="false"] span[class="my-auto mr-2"]').click()
        sleep(1.25)
        driver.find_element(By.XPATH, '//a[normalize-space()="Students"]').click()
        sleep(0.75)
        driver.find_element(By.LINK_TEXT, 'Create New Student').click()
        # driver.find_element(By.XPATH, '//a[@class="btn btn-green btn-sm"]').click()
        # driver.find_element(By.XPATH, 'a[contains(., "Create New Student")]').click()
        # assert driver.find_element(By.XPATH, '//a[@class="btn btn-green btn-sm"]').click()
        # driver.find_element(By.CSS_SELECTOR, 'btn.btn-green.btn-sm').click()
        sleep(0.75)
        driver.find_element(By.ID, 'user_student_detail_attributes_first_name').send_keys(locators.first_name)
        sleep(0.75)
        driver.find_element(By.ID, 'user_student_detail_attributes_last_name').send_keys(locators.last_name)
        sleep(0.75)
        driver.find_element(By.ID, 'user_student_detail_attributes_preferred_name').send_keys(locators.full_name)
        sleep(0.75)
        driver.find_element(By.ID, 'user_student_detail_attributes_birth_date').send_keys('1')
        sleep(0.75)
        driver.find_element(By.ID, 'user_student_detail_attributes_birth_date').send_keys(10 * Keys.BACKSPACE)
        sleep(0.75)
        driver.find_element(By.ID, 'user_student_detail_attributes_birth_date').send_keys(locators.date_of_birth)
        sleep(0.75)
        # driver.find_element(By.ID, 'user_student_detail_attributes_birth_date').send_keys(Keys.ENTER)
        # sleep(0.75)
        # driver.find_element(By.ID, 'user_student_detail_attributes_birth_date').clear()
        # sleep(0.75)
        # driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Date of Birth on passport"]').send_keys('19990810')
        # sleep(0.75)
        # driver.find_element(By.XPATH, '//input[@id="user_student_detail_attributes_birth_date"]').click()
        driver.find_element(By.ID, 'user_student_detail_attributes_passport_number').send_keys(locators.passport_number)
        sleep(0.75)
        # *********************** Contact Information ***********************************************
        driver.find_element(By.ID, 'select2-user_student_detail_attributes_country_of_citizenship-container').click()
        sleep(0.75)
        Select(driver.find_element(By.ID, 'user_student_detail_attributes_country_of_citizenship')).select_by_value("CA")
        # driver.find_element(By.XPATH, '//input[@role="searchbox"]').send_keys(locators.country)
        sleep(0.75)
        driver.find_element(By.ID, 'phone_number').send_keys(locators.phone_number)
        sleep(0.75)
        driver.find_element(By.ID, 'user_student_detail_attributes_address_attributes_mailing_address').send_keys(locators.address)
        sleep(0.75)
        driver.find_element(By.CSS_SELECTOR, 'div[id="user_student_detail_attributes_address_attributes_country_chosen"] span').click()
        sleep(0.75)
        driver.find_element(By.XPATH, '//*[@id="user_student_detail_attributes_address_attributes_country_chosen"]/div/div/input').send_keys(f'Canada{Keys.ENTER}')
        # Select(driver.find_element(By.ID, 'user_student_detail_attributes_address_attributes_country')).select_by_value("CA")
        sleep(0.75)
        driver.find_element(By.ID, 'user_student_detail_attributes_address_attributes_state_chosen').click()
        sleep(0.75)
        driver.find_element(By.XPATH,'//*[@id="user_student_detail_attributes_address_attributes_state_chosen"]/div/div/input').send_keys('British Columbia')
        sleep(0.75)
        driver.find_element(By.XPATH,'//*[@id="user_student_detail_attributes_address_attributes_state_chosen"]/div/div/input').send_keys(Keys.RETURN)
        sleep(0.75)
        driver.find_element(By.XPATH, '//span[contains(., "City")]').click()
        sleep(0.75)
        driver.find_element(By.XPATH, '//*[@id="user_student_detail_attributes_address_attributes_city_chosen"]/div/div/input').send_keys('Kelowna')
        sleep(0.75)
        driver.find_element(By.XPATH, '//*[@id="user_student_detail_attributes_address_attributes_city_chosen"]/div/div/input').send_keys(Keys.RETURN)
        sleep(0.75)
        driver.find_element(By.ID, 'user_student_detail_attributes_address_attributes_zip_code').send_keys(locators.postalcode)
        sleep(0.75)
        driver.find_element(By.ID, 'user_student_detail_attributes_address_attributes_zip_code').send_keys(Keys.RETURN)
        sleep(0.75)
        driver.find_element(By.XPATH, '//input[@id="user_email"]').send_keys(locators.email)
        sleep(0.75)


        #************* Education Information *************************

        driver.find_element(By.XPATH, '//span[contains(., "Credentials")]').click()
        sleep(0.75)
        driver.find_element(By.XPATH,'//*[@id="user_student_detail_attributes_user_educations_attributes_0_credentials_chosen"]/div/div/input').send_keys(locators.credentials)
        sleep(0.75)
        driver.find_element(By.XPATH,'//*[@id="user_student_detail_attributes_user_educations_attributes_0_credentials_chosen"]/div/div/input').send_keys(Keys.RETURN)
        sleep(0.75)
        driver.find_element(By.ID, 'user_student_detail_attributes_user_educations_attributes_0_school_name').click()
        sleep(0.75)
        driver.find_element(By.XPATH, '//input[@id="user_student_detail_attributes_user_educations_attributes_0_school_name"]').send_keys(locators.school)
        sleep(0.75)
        driver.find_element(By.XPATH, '//input[@id="user_student_detail_attributes_user_educations_attributes_0_program"]').send_keys(locators.program)
        sleep(0.75)
        driver.find_element(By.XPATH, '//span[contains(., "GPA Scale")]').click()
        sleep(0.75)
        driver.find_element(By.XPATH, '//*[@id="user_student_detail_attributes_user_educations_attributes_0_gpa_scale_chosen"]/div/div/input').send_keys('100')
        sleep(0.75)
        driver.find_element(By.XPATH,'//*[@id="user_student_detail_attributes_user_educations_attributes_0_gpa_scale_chosen"]/div/div/input').send_keys(Keys.RETURN)
        sleep(0.75)
        driver.find_element(By.XPATH, '//input[@id="user_student_detail_attributes_user_educations_attributes_0_gpa"]').send_keys('100')
        sleep(0.75)
        driver.find_element(By.XPATH, '//input[@id="user_student_detail_attributes_user_educations_attributes_0_gpa"]').send_keys(Keys.RETURN)
        sleep(0.75)

        driver.find_element(By.XPATH, '//input[@name="commit"]').click()
        sleep(2)
        driver.find_element(By.CLASS_NAME, 'toast-message').is_displayed()
        sleep(4)
        print('-------------Student is created successfully.-----------')

# def create_new_application():
#         print(f'*****************Course Information******************')
#
#         driver.find_element(By.XPATH, '//span[normalize-space()="My WeGoStudy"]').click()
#         # driver.find_element(By.CSS_SELECTOR, 'a[aria-expanded="false"] span[class="my-auto mr-2"]').click()
#         sleep(1.25)
#         driver.find_element(By.XPATH, '//a[normalize-space()="Students"]').click()
#         sleep(0.75)
#         driver.find_element(By.LINK_TEXT, 'Create Application').click()
#         sleep(0.75)
#         driver.find_element(By.XPATH, '//span[normalize-space()="Select School"]').click()
#         sleep(0.75)
#         driver.find_element(By.XPATH,'//*[@id="admission_institute_detail_id_chosen"]/div/ul/li[7]').click()
#         sleep(0.75)
#         driver.find_element(By.XPATH, '//span[normalize-space()="Select Course"]').click()
#         sleep(0.75)
#         driver.find_element(By.XPATH, '//*[@id="admission_institute_program_id_chosen"]/div/ul/li[2]').click()
#         sleep(0.75)
#         driver.find_element(By.XPATH, '//span[normalize-space()="Select Starting Semester"]').click()
#         sleep(0.75)
#         driver.find_element(By.XPATH, '//*[@id="admission_starting_semester_chosen"]/div/ul/li[3]').click()
#         sleep(0.75)
#         driver.find_element(By.XPATH, '//span[normalize-space()="Select Start Day"]').click()
#         sleep(0.75)
#         driver.find_element(By.XPATH, '//*[@id="admission_start_day_chosen"]/div/ul/li[3]').click()
#         sleep(0.75)
#         driver.find_element(By.XPATH, '//span[normalize-space()="Select Year"]').click()
#         sleep(0.75)
#         driver.find_element(By.XPATH, '//*[@id="admission_start_year_chosen"]/div/ul/li[3]').click()
#         sleep(0.75)
#         driver.find_element(By.CSS_SELECTOR, '#admission_last_name').send_keys(locators.last_name)
#         sleep(0.75)
#

        # Education Information**************************************

        # driver.find_element(By.XPATH, '//span[contains(., "Credentials")]').click()
        # sleep(0.75)
        # driver.find_element(By.CSS_SELECTOR,'div[id="admission_user_educations_attributes_0_credentials_chosen"] input[type="text"]').send_keys('Degree')
        # sleep(0.75)
        # driver.find_element(By. CSS_SELECTOR,'div[id="admission_user_educations_attributes_0_credentials_chosen"] input[type="text"]').send_keys(Keys.RETURN)
        # sleep(0.75)
        # driver.find_element(By.XPATH, '//input[@id="admission_user_educations_attributes_0_school_name"]').click()
        # sleep(0.75)
        # driver.find_element(By.CSS_SELECTOR,'#admission_user_educations_attributes_0_school_name').send_keys(locators.school)
        # sleep(0.75)
        # driver.find_element(By.CSS_SELECTOR,'#admission_user_educations_attributes_0_school_name').send_keys(Keys.RETURN)
        # sleep(0.75)
        # driver.find_element(By.XPATH,'//input[@id="admission_user_educations_attributes_0_program"]').click()
        # sleep(0.75)
        # driver.find_element(By.CSS_SELECTOR, '#admission_user_educations_attributes_0_program').send_keys(locators.program)
        # sleep(0.75)
        # driver.find_element(By.CSS_SELECTOR, '#admission_user_educations_attributes_0_program').send_keys(Keys.RETURN)
        # sleep(0.75)
        # driver.find_element(By.XPATH, '//span[contains(., "GPA Scale")]').click()
        # sleep(0.75)
        # driver.find_element(By.CSS_SELECTOR,'div[id="admission_user_educations_attributes_0_gpa_scale_chosen"] input[type="text"]').send_keys('100')
        # sleep(0.75)
        # driver.find_element(By.CSS_SELECTOR,'div[id="admission_user_educations_attributes_0_gpa_scale_chosen"] input[type="text"]').send_keys(Keys.RETURN)
        # sleep(0.75)
        # driver.find_element(By.XPATH,'//input[@id="admission_user_educations_attributes_0_gpa"]').click()
        # sleep(0.75)
        # driver.find_element(By.CSS_SELECTOR,'#admission_user_educations_attributes_0_gpa').send_keys('100')
        # sleep(0.75)
        # driver.find_element(By.CSS_SELECTOR,'#admission_user_educations_attributes_0_gpa').send_keys(Keys.RETURN)
        # sleep(0.75)

        # driver.find_element(By.XPATH, '//input[@id="admission_electronic_communication_true"]').click()
        # sleep(0.75)
        # driver.find_element(By.XPATH, '//input[@name="commit"]').click()
        # sleep(2)
        # driver.find_element(By.CLASS_NAME, 'toast-message').is_displayed()
        # sleep(4)
        # print('-------------Student is created successfully.-----------')



def view_details():
    print(f'***************** View Details ******************')
    driver.find_element(By.XPATH, '//span[normalize-space()="My WeGoStudy"]').click()
    # driver.find_element(By.CSS_SELECTOR, 'a[aria-expanded="false"] span[class="my-auto mr-2"]').click()
    sleep(1.25)
    driver.find_element(By.XPATH, '//a[normalize-space()="Students"]').click()
    sleep(3)
    driver.find_element(By.XPATH, '//a[@href="/partners/student_details/sheila-mccullough"]').click()
    # driver.find_element(By.XPATH, '//a[@href="/partners/student_details/christopher-knapp"]').click()
    sleep(3)
    driver.find_element(By.XPATH, '//body//form').click()
    sleep(6)


def view_application_list():
    print(f'***************** View Application list for one student  ******************')
    driver.find_element(By.XPATH, '//span[normalize-space()="My WeGoStudy"]').click()
    sleep(1.25)
    driver.find_element(By.XPATH, '//a[normalize-space()="Students"]').click()
    sleep(2)
    driver.find_element(By.XPATH, '//div[@id="student_list"]//div[1]//div[3]//a[3]').click()
    sleep(2)
    driver.find_element(By.XPATH, '//button[@class="btn btn-default btn-sm"]').click()
    sleep(4)


# def edit_admission_application():
#     print(f'***************** Edit Admission Application  ******************')
    # driver.find_element(By.XPATH, '//span[normalize-space()="My WeGoStudy"]').click()
    # sleep(1.25)
    # driver.find_element(By.XPATH, '//a[normalize-space()="Students"]').click()
    # sleep(2)
    # driver.find_element(By.XPATH, '/html[1]/body[1]/section[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/a[3]').click()
    # sleep(2)
    # driver.find_element(By.XPATH, '//a[normalize-space()="AS000093-55"]').click()
    # sleep(5)
    # driver.find_element(By.ID, 'admission_first_name').click()
    # sleep(5)
    # driver.find_element(By.CSS_SELECTOR, '#admission_first_name').send_keys('Mary')
    # sleep(1.25)
    # driver.find_element(By.XPATH, '//div[@class="row"]//form').click()
    # sleep(1.25)



def sort_by_dropdown_menu():
    print(f'***************** Sort By Dropdown Menu  ******************')
    driver.find_element(By.XPATH, '//span[normalize-space()="My WeGoStudy"]').click()
    sleep(1.25)
    driver.find_element(By.XPATH, '//a[normalize-space()="Students"]').click()
    sleep(2)
    driver.find_element(By.XPATH, '//div[@role="button"]').click()
    sleep(1.25)
    driver.find_element(By.XPATH, '//a[normalize-space()="First Name"]').click()
    sleep(1.25)
    driver.find_element(By.XPATH, '//div[@role="button"]').click()
    sleep(1.25)
    driver.find_element(By.XPATH, '//a[normalize-space()="Last Name"]').click()
    sleep(1.25)
    driver.find_element(By.XPATH, '//div[@role="button"]').click()
    sleep(1.25)
    driver.find_element(By.XPATH, '//a[normalize-space()="Profile Created"]').click()
    sleep(1.25)



def commissions():
    print(f' ************ Commissions ************************************')
    driver.find_element(By.XPATH, '//span[normalize-space()="My WeGoStudy"]').click()
    sleep(1.25)
    driver.find_element(By.XPATH, '//a[normalize-space()="Commission"]').click()
    sleep(2)


def filter_by_study_area():
    print(f' *********** Filter By Study Area *******************')
    driver.find_element(By.XPATH, '//a[normalize-space()="Schools"]').click()
    sleep(1.25)
    driver.find_element(By.XPATH, '//a[normalize-space()="Filter By Study Area"]').click()
    sleep(1.25)
    driver.find_element(By.XPATH, '//span[contains(., "Engineering and electronics")]').click()
    sleep(1.25)
    driver.find_element(By.XPATH, '//span[contains(., "Law programs")]').click()
    sleep(3)
    driver.find_element(By.XPATH, '//div[@id="filter_by_study_area"]//a[@class="apply_filter disable_apply"][normalize-space()="Apply"]').click()
    sleep(6)



def filter_by_city():
    print(f' *********** Filter By City *******************')
    driver.find_element(By.XPATH, '//a[normalize-space()="Schools"]').click()
    sleep(1.25)
    driver.find_element(By.XPATH, '//a[normalize-space()="Filter By City"]').click()
    sleep(1.25)
    driver.find_element(By.XPATH, '//span[contains(., "Windsor")]').click()
    sleep(1.25)
    driver.find_element(By.XPATH, '//span[contains(., "Vancouver")]').click()
    sleep(3)
    driver.find_element(By.XPATH, '//div[@id="filter_by_city"]//a[@class="apply_filter disable_apply"][normalize-space()="Apply"]').click()
    sleep(6)


def filter_by_program():
    print(f' *********** Filter By Program *******************')
    driver.find_element(By.XPATH, '//a[normalize-space()="Schools"]').click()
    sleep(1.25)
    driver.find_element(By.XPATH, '//a[normalize-space()="Filter By Program"]').click()
    sleep(1.25)
    driver.find_element(By.XPATH, '//span[contains(., "Bachelor of Engineering")]').click()
    sleep(1.25)
    driver.find_element(By.XPATH, '//span[contains(., "Master of Fine Arts (MFA)")]').click()
    sleep(3)
    driver.find_element(By.XPATH, '//div[@id="filter_by_program"]//a[@class="apply_filter disable_apply"][normalize-space()="Apply"]').click()
    sleep(6)



def add_my_favorite():
    print(f' *********** Add My Favorite *******************')
    driver.find_element(By.XPATH, '//a[normalize-space()="Schools"]').click()
    sleep(1.25)
    driver.find_element(By.XPATH, '//div[@class="col-12 col-lg-12 col-md-12"]//div[1]//div[3]//a[1]//div[1]').click()
    sleep(1.25)
    driver.find_element(By.XPATH, '//a[@class="favorites-btn"]').click()
    sleep(6)
    driver.find_element(By.XPATH, '//a[normalize-space()="Schools"]').click()
    sleep(1.25)
    driver.find_element(By.XPATH, '//div[@id="featured_institutes"]//div[1]//div[3]//a[1]//div[1]').click()
    sleep(1.25)
    driver.find_element(By.XPATH, '//i[@class="fa fa-heart"]').click()
    sleep(1.25)



def connect_to_wegostudy():
    print(f' *********** Connect To We GoStudy *******************')
    driver.find_element(By.XPATH, '//a[normalize-space()="Schools"]').click()
    sleep(2)
    driver.find_element(By.XPATH, '//div[@class="col-12 col-lg-12 col-md-12"]//div[1]//div[3]//a[1]//div[1]').click()
    sleep(4)
    original_window = driver.current_window_handle
    sleep(1.25)
    driver.find_element(By.XPATH, '//a[normalize-space()="Connect to WeGoStudy"]').click()
    sleep(4)
    driver.switch_to.window(original_window)



def visit_college_website():
    print(f' *********** Visit College Website *******************')
    driver.find_element(By.XPATH, '//a[normalize-space()="Schools"]').click()
    sleep(2)
    driver.find_element(By.XPATH, '//div[@class="col-12 col-lg-12 col-md-12"]//div[1]//div[3]//a[1]//div[1]').click()
    sleep(8)
    original_window = driver.current_window_handle
    sleep(1.25)
    driver.find_element(By.XPATH, '//a[normalize-space()="Visit College Website"]').click()
    sleep(8)
    driver.switch_to.window(original_window)



def tuition():
    print(f' *********** Tuition *******************')
    driver.find_element(By.XPATH, '//a[normalize-space()="Schools"]').click()
    sleep(2)
    driver.find_element(By.XPATH, '//div[@class="col-12 col-lg-12 col-md-12"]//div[1]//div[3]//a[1]//div[1]').click()
    sleep(6)
    original_window = driver.current_window_handle
    sleep(1.25)
    driver.find_element(By.XPATH, '//a[@class="btn btn-green btn-sm pull-right"]').click()
    sleep(4)
    driver.switch_to.window(original_window)



def apply_now():
    print(f' *********** Apply Now *******************')
    driver.find_element(By.XPATH, '//a[normalize-space()="Schools"]').click()
    sleep(2)
    driver.find_element(By.XPATH, '//div[@class="col-12 col-lg-12 col-md-12"]//div[1]//div[3]//a[1]//div[1]').click()
    sleep(2)
    driver.find_element(By.XPATH, '//a[@class="btn btn-blue btn-sm"]').click()
    sleep(1.25)
    driver.find_element(By.XPATH, '//button[normalize-space()="Close"]').click()
    sleep(1.25)



def study_area_prog_lev():
    print(f' *********** Study Area *******************')
    driver.find_element(By.XPATH, '//a[contains(.,  "Schools")]').click()
    sleep(0.25)
    driver.find_element(By.XPATH, '//h3[normalize-space()="British Columbia Institute of Technology"]').is_displayed()
    sleep(0.25)
    driver.find_element(By.XPATH, '//div[3]//div[3]//a[1]//div[1]').click()
    sleep(0.25)
    Select(driver.find_element(By.ID, 'study_area')).select_by_value('Computer, information and services')
    sleep(0.25)
    Select(driver.find_element(By.ID, 'level')).select_by_value('Bachelor of Technology')
    sleep(0.25)
    driver.find_element(By.XPATH, '//input[@value="GO"]').click()
    sleep(0.25)


def log_out():
        driver.find_element(By.CSS_SELECTOR, 'span[class="my-auto mr-2 pf-name"]').click()
        sleep(1)
        driver.find_element(By.XPATH, '//a[normalize-space()="Log out"]').click()
        sleep(1)
        driver.find_element(By.ID, 'authentication-popup').is_displayed()
        sleep(1)
        print(f'********* LOG OUT IS SUCCUSSEFUL  {datetime.datetime.now()}********************')



# setUp()
# # # create_account()
# log_in()
# # create_new_student()
# # # # # create_new_application()
# # view_details()
# # # # view_application_list()
# # # # edit_admission_application()
# sort_by_dropdown_menu()
# commissions()
# filter_by_study_area()
# filter_by_city()
# filter_by_program()
# add_my_favorite()
# connect_to_wegostudy()
# visit_college_website()
# tuition()
# apply_now()
# study_area_prog_lev()
# log_out()
# tearDown()