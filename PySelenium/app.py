# browser.page_source() returns a string of the entire html code of the current page in the browser
from selenium import webdriver

browser = webdriver.Chrome()
browser.get("https://github.com")

signin_link = browser.find_element_by_link_text("Sign in")
signin_link.click()

username_box = browser.find_element_by_id("login_field")
username_box.send_keys("MalamaPono")

password_box = browser.find_element_by_id("password")
password_box.send_keys("Haaheo001")
password_box.submit()

# getting and pinpointing the section of page where the username is
profile_link = browser.find_element_by_class_name("user-profile-link")
# getting a String which represents the html code of the section where the username is
link_label = profile_link.get_attribute("innerHTML")

assert "MalamaPono" in link_label

browser.quit()