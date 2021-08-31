import time
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


# settings

TIME_BETWEEN_POSTS = 60



class kitty:
    def __init__(self, d, e, f, g, i, j):
        self.breeding = "Not Allowed"
        self.delivery_range = "Worldwide"
        self.shipping_fee = "Varies by destination"
        self.name = d
        self.dob = e
        self.breed = f
        self.gender = g
        self.whats_included = "."
        self.description = i
        self.price = j
    
    

# set up remote
driver = webdriver.Chrome()
driver.maximize_window()


# open goKitty
driver.get("https://gokitty.com/login/index")



# log in as zahar
username = driver.find_element_by_id("login").send_keys(USERNAME)
password = driver.find_element_by_id("pass").send_keys(PASSWORD)

driver.find_element_by_class_name("button").click()



# go to my kitties
driver.find_element_by_link_text("My Kitties").click()

# accept cookies
cookie_div = driver.find_element_by_class_name("cc-compliance")
cookie_div.find_element_by_css_selector("a").click()


# loop through each listing and fill list of kitty information
results = driver.find_elements_by_class_name("list_cat")

kitties = []

for x in range(len(results)):

    # click link for kitty
    results[x].click()

    # scrape information for kitty
    rows = driver.find_elements_by_class_name("formRow")

    name = driver.find_element_by_class_name("profile_title").text

    dob = rows[9].find_element_by_class_name("formRight").text[0:10].replace("/", "")

    breed = rows[2].find_element_by_class_name("formRight").text

    gender = rows[3].find_element_by_class_name("formRight").text

    description = rows[17].text

    price = rows[0].find_element_by_class_name("price").get_attribute("data-price")

    kitties.append(kitty(name, dob, breed, gender, description, price))

    driver.back()



    # delete post of kitty

    delete_link = driver.find_elements_by_class_name("actions_popup")[x].find_elements_by_css_selector("a")[1].get_attribute("href")
    driver.get(delete_link)


    # create new post for kitty

    # click add kitty button
    driver.find_element_by_class_name("button").click()

    # fill kitty/litter name
    driver.find_element_by_id("kitten_name").send_keys(kitties[x].name)

    # fill date of birth
    driver.find_element_by_id("dob").click()
    driver.find_element_by_id("dob").send_keys(kitties[x].dob)

    # fill breed
    driver.find_element_by_id("breed_id").send_keys(kitties[x].breed)

    # fill gender
    driver.find_element_by_id("gender").send_keys(kitties[x].gender)

    # fill breeding
    driver.find_element_by_id("breeding").send_keys(kitties[x].breeding)

    # fill delivery range
    driver.find_element_by_id("shipping_area").send_keys(kitties[x].delivery_range)

    # fill shipping fee
    driver.find_element_by_id("shipping_included").send_keys(kitties[x].shipping_fee)

    # fill what's included
    driver.find_element_by_id("whats_included").send_keys(kitties[x].whats_included)

    # fill description
    driver.find_element_by_id("description").send_keys(kitties[x].description)

    # fill low (required) price range
    driver.find_element_by_id("price_from").send_keys(kitties[x].price)

    # click add images
    driver.find_element_by_xpath("//input[@value='Add photos']").click()

    # click add images again
    button = driver.find_element_by_class_name("qq-upload-button")

    

    filename = FOLDER_PATH + kitties[x].name

    directory = os.listdir(filename + ".")

    for file in directory:
    
        button.find_element_by_css_selector("input").send_keys(FOLDER_PATH + kitties[x].name + "\\" + file)

    
    # wait before posting
    time.sleep(TIME_BETWEEN_POSTS)

    # hit submit button
    driver.find_element_by_class_name("button").click()
    
    results = driver.find_elements_by_class_name("list_cat")
