import time
from selenium import webdriver 
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC 

driver = webdriver.Firefox()
driver.get("https://www.linkedin.com/alumni")
time.sleep(5)

sign_in_link_ele = driver.find_element_by_link_text("Sign in")
action = ActionChains(driver) 
action.click(on_element = sign_in_link_ele)
action.perform()
time.sleep(3)

email_ele = driver.find_element_by_id("username")
email_ele.send_keys("your@email.id")
pass_ele = driver.find_element_by_id("password")
pass_ele.send_keys("yourpassword")
sign_in_link_ele = driver.find_element_by_xpath('//button[@aria-label="Sign in"]')
sign_in_link_ele.click()

time.sleep(5)
#close_msgs_ele = driver.find_element_by_xpath('//header[@class="msg-overlay-bubble-header"]')
#close_msgs_ele.click()

show_more_filters_button_element = driver.find_element_by_xpath('//button[@aria-label="Show more people filters"]')
show_more_filters_button_element.click()

universities = ["List", "of", "companies", "or", "universities", "whose", "alumni", "you", "want", "to", "send", "requests", "to"]
count = 1

for uni in universities:
    add_uni_ele = driver.find_element_by_xpath('//button[@aria-label="Add any company"]')
    add_uni_ele.click()
    add_uni_text_ele = driver.find_element_by_xpath('//input[@placeholder="Add any company"]')
    add_uni_text_ele.send_keys(uni)
    time.sleep(1)
    add_uni_text_ele.send_keys(Keys.ARROW_DOWN)
    add_uni_text_ele.send_keys(Keys.RETURN)
    time.sleep(3)

    text_elements = driver.find_elements_by_xpath('//div[@class="truncate"]')

    profiles_connect_button_list_elements = driver.find_elements_by_xpath('//button[@class="artdeco-button artdeco-button--2 artdeco-button--full artdeco-button--secondary ember-view full-width"]')
    driver.execute_script("window.scrollTo(0, 1750)")
    for j in range(len(profiles_connect_button_list_elements)):
        if len(text_elements[j].text) > 3:
            if (text_elements[j].text[1:3] < '20' or text_elements[j].text[1:3] > '99') and text_elements[j].text[1:3].isnumeric():
                first_button_ele = profiles_connect_button_list_elements[j]
                first_button_ele.click()
                time.sleep(0.4)
                add_a_note_button_element = driver.find_element_by_xpath('//button[@aria-label="Add a note"]')
                add_a_note_button_element.click()
                note_ele = driver.find_element_by_id("custom-message")
                note_ele.send_keys("Hey, I am currently a final year student at IIT Kgp and will be applying for masters in fall 2021. I had a few doubts and thus wanted to connect with you.")
                send_note_button_element = driver.find_element_by_xpath('//button[@aria-label="Send now"]')
                send_note_button_element.click()
                time.sleep(3)
        if count%4 == 0:
            xyz = str(1750 + count/4*284)
            driver.execute_script("window.scrollTo(0, "+xyz+")")

    driver.execute_script("window.scrollTo(0, 1000)")
    filtername_elements = driver.find_elements_by_xpath('//span[@class="org-people-bar-graph-element__category"]')
    for filter in filtername_elements:
        if filter.text == uni:
            filter.click()
            break

    driver.execute_script("window.scrollTo(0, 0)")