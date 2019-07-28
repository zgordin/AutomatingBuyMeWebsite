import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import RandomEmail

global driver

WEBSITE_FILE_LOCATION = "C:\\Users\\zgordin\\Downloads\\Website.txt"
USER_NAME = "aaa"
EMAIL = RandomEmail.random_email()
PASSWORD = "Asd12313"
RECEIVER_NAME = "bbb"
SENDER_NAME = "ccc"
IMAGE = "C:\\Users\\zgordin\\Downloads\\matthew-kerslake-BpH--upRlCs-unsplash.jpg"
SCREENSHOT_SCROLLDOWN = "C:\\Users\\zgordin\\Downloads\\Choose_business.png"
SENDER_EMAIL = RandomEmail.random_email()

def registration():
    driver.execute_script("arguments[0].click();",driver.find_element_by_class_name("seperator-link")) # signup
    # Press on “BUYME - כניסה ל ” button prior registration
    driver.find_element_by_xpath("//button[@type='submit']").click()
    # Validate error messages (red text)
    if driver.find_element_by_class_name("parsley-required").is_displayed():
        print("text error displayed in red text as should be")
    # Press on button "להרשמה"
    driver.find_element_by_xpath("/html/body[@class='rtl desktop chrome ember-application hover']/div[@id='ember572']/div[@class='main-container home-page-offset']/div[@class='ui-lightbox login']/div[@class='inner']/div[@class='box']/div[@class='lightbox-content']/p[@class='switch-text']/span[@class='text-btn']").click()
    # driver.find_element_by_link_text("להרשמה").click()
    # Enter first name
    driver.find_element_by_xpath("//input[@placeholder='שם פרטי']").send_keys(USER_NAME)
    # Enter Email Address
    driver.find_element_by_xpath("//input[@placeholder='מייל']").send_keys(EMAIL)
    # Enter Password
    driver.find_element_by_id("valPass").send_keys(PASSWORD)
    # Enter Password again
    driver.find_element_by_xpath("//input[@placeholder='אימות סיסמה']").send_keys(PASSWORD)
    # Checkbox
    driver.execute_script("arguments[0].click();",driver.find_element_by_class_name("fa-check"))
    # Submit button
    driver.find_element_by_xpath("//button[@type='submit']").click()


# def fast_multiselect(drive):
#     select = Select(driver.find_element_by_class_name("chosen-single"))
#     print(select.options)
    # for label in labels:
    #     select.select_by_visible_text(label)
    #     print(label)

def search_present():
    time.sleep(2)
    # Pick a price Point
    driver.find_element_by_class_name("chosen-single").click()
    driver.find_elements_by_class_name("active-result")[2].click()
    # Pick an Area
    driver.find_element_by_link_text("אזור").click()
    driver.find_elements_by_class_name("active-result")[1].click()
    # Pick Category
    driver.find_element_by_link_text("קטגוריה").click()
    driver.find_elements_by_class_name("active-result")[4].click()
    # Search present
    driver.find_element_by_link_text("תמצאו לי מתנה").click()

def choose_business_screen():
    time.sleep(1)
    #Scroll to the bottom of the business screen page
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    #Take ScreenShot
    driver.get_screenshot_as_file(SCREENSHOT_SCROLLDOWN)
    # Pick a business
    driver.find_element_by_link_text("מסעדת אורבנו").click()
    # Type a price
    driver.find_element_by_xpath("//input[@placeholder='מה הסכום?']").send_keys("150")
    # Submit button
    driver.find_element_by_xpath("//button[@type='submit']").click()

def sender_and_receiver_information():
    time.sleep(1)
    # Validate the text color of the step name למי לשלוח
    color = driver.find_element_by_class_name("step-title").value_of_css_property("color")
    if color == "rgba(250, 180, 66, 1)":
        print("Validating the text color of the step name as expected - Color Orange")
    else:
        print(color,"Validating the text color of the step name not as expected (orange)")
    # Press radio button for someone else
    driver.find_element_by_xpath("//*[@data='forSomeone']").click()
    # Enter receiver name
    driver.find_element_by_xpath("//input[@maxlength='25']").send_keys(RECEIVER_NAME)
    # Clear field of sender name
    driver.find_element_by_xpath("//input[@data-parsley-required-message='למי יגידו תודה? שכחת למלא את השם שלך']").clear()
    # Enter Sender Name
    driver.find_element_by_xpath("//input[@data-parsley-required-message='למי יגידו תודה? שכחת למלא את השם שלך']").send_keys(SENDER_NAME)
    # Enter a blessing
    driver.find_element_by_xpath("//textarea[@rows='4']").send_keys("Bless You Dear")
    # Upload Image
    driver.find_element_by_xpath("//input[@accept='image/*']").send_keys(IMAGE)
    # Pick the event
    # driver.find_element_by_class_name("ember-chosenselect").click()
    driver.find_element_by_link_text("לאיזה אירוע?").click()
    driver.find_element_by_xpath("//li[@data-option-array-index='5']").click()
    # Press radio button after payment
    driver.find_element_by_class_name("send-now").click()
    # Pick Email option
    # driver.find_element_by_link_text("במייל").click()
    driver.find_element_by_class_name("icon-envelope").click()
    # Enter Email Address to send
    driver.find_element_by_xpath("//input[@data-parsley-group='mail']").send_keys(SENDER_EMAIL)
    # submit mail
    driver.find_element_by_xpath("//button[@type='submit']").click()
    # submit - go to payment
    driver.find_element_by_xpath("//button[@type='submit']").click()

def validate_receiver_sender():
    time.sleep(1)
    # verify receiver name
    receiver = driver.find_element_by_class_name("receiver").text[3:]
    if receiver == RECEIVER_NAME:
        print("validated receiver name successfully")
    else:
        print("receiver name does not match")
    # verify sender name
    sender = driver.find_element_by_class_name("sender").text[11:]
    if sender == SENDER_NAME:
        print("validated sender name successfully")
    else:
        print("sender name does not match")
    # print blessing from validation card
    blessing = driver.find_element_by_class_name("card-text").text
    print(blessing)

if __name__ == '__main__':
    my_file = open(WEBSITE_FILE_LOCATION, 'r+', encoding='utf-8')
    WEB_SITE = my_file.read()
    my_file.close() #closing the file read
    driver = webdriver.Chrome(executable_path="C:\\Users\\zgordin\\Documents\\chromedriver.exe")
    driver.implicitly_wait(20)  # give up to 20 sec to find on all find_elemets or find_elements
    driver.get(WEB_SITE)
    # Registration press on SignUp --> enter credentials --> check-box confirmation --> Submit
    registration()
    # Home Screen
    search_present()
    # Choose business screen
    choose_business_screen()
    # Sender & Receiver information screen
    sender_and_receiver_information()
    # Validate the below information (compare the text fields with what
    # you had enter to preview text fields):
    validate_receiver_sender()
    #Comment test
    print("x")
    #Comment m
    print("m")





