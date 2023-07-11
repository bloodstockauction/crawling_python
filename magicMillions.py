from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv
from datetime import date

total_lot_number = 45

# Get the current date
current_date = date.today()

# Format the date as DD/MM/YYYY
formatted_date = current_date.strftime("%d-%m-%Y")

# Instantiate the ChromeDriver
driver = webdriver.Chrome()

# Wait for the page to load
driver.implicitly_wait(10)

# Open a website
driver.get("https://www.magicmillions.online/login")

# Find an element by its ID and type text into an input field
username_input = driver.find_element(By.ID, "username")
password_input = driver.find_element(By.ID, "password")
terms_input = driver.find_element(By.ID, "terms")
submit_input = driver.find_element(By.NAME, "submit")



username_input.send_keys("3727")
password_input.send_keys("HFCDAGZC")
terms_input.click()
submit_input.click()

# Wait for the page to load after clicking the login button
WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.ID, "main"))
)

# Check if login was successful by looking for an element on the logged-in page
welcome_message = driver.find_element(By.ID, "main")
if welcome_message:
    print("Login successful!")
else:
    print("Login failed.")

current_catalogue_link = driver.find_element(By.XPATH, "//html/body/header/div/nav/div[1]/div/span/a")
current_catalogue = current_catalogue_link.get_attribute("href")

print(current_catalogue)
driver.get(current_catalogue)
# driver.get("https://www.magicmillions.online/sale/314/23OMJ")


time.sleep(1) #sleep for 1 sec
with open('result-'+formatted_date+'.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
    header = [
      'horseName',
      'horseCategory',
      'horseDob',
      'horseSire',
      'horseDam',
      'horseCob',
      'horseSex',
      'vandorName',
      'vandorPhone',
      'vandorMobile',
      'vandorAddress',
    ]
    csvwriter.writerow(header)

    # for index in range(1, total_lot_number + 1):
    for index in range(1, 3): # for test
        # print(i)
        find_lot_input = driver.find_element(By.NAME, "find_lot")
        find_lot_input.send_keys(str(index))
        if index == 1:
            go_button = driver.find_element(By.XPATH, "//html/body/div[1]/section[2]/div[1]/div/div/div[2]/form/div/div[2]/button")
        else:
            go_button = driver.find_element(By.XPATH, "/html/body/div[1]/section[2]/div[1]/div/div/div[1]/div/div[4]/form/div/div[2]/button")

        go_button.click()
        horse_name = driver.find_element(By.XPATH, "/html/body/div[1]/section[2]/div[2]/div[1]/div[2]/div/div[1]/div/h1")
        horseDob = driver.find_element(By.XPATH, "/html/body/div[1]/section[2]/div[2]/div[1]/div[1]/div[1]/div/div/div/div[1]/div/div[2]")
        horseSire = driver.find_element(By.XPATH, "/html/body/div[1]/section[2]/div[2]/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[2]")
        horseDam = driver.find_element(By.XPATH, "/html/body/div[1]/section[2]/div[2]/div[1]/div[1]/div[1]/div/div/div/div[3]/div/div[2]")
        horseCob = driver.find_element(By.XPATH, "/html/body/div[1]/section[2]/div[2]/div[1]/div[1]/div[1]/div/div/div/div[5]/div/div[2]")
        horseSex = driver.find_element(By.XPATH, "/html/body/div[1]/section[2]/div[2]/div[1]/div[1]/div[1]/div/div/div/div[7]/div/div[2]")
        horseCategory = driver.find_element(By.XPATH, "/html/body/div[1]/section[2]/div[2]/div[1]/div[1]/div[1]/div/div/div/div[8]/div/div[2]")
        vandorName = driver.find_element(By.XPATH, "/html/body/div[1]/section[2]/div[2]/div[1]/div[1]/div[6]/div/div[2]")
        vandorPhone = driver.find_element(By.XPATH, "/html/body/div[1]/section[2]/div[2]/div[1]/div[1]/div[6]/div/div[4]/a")
        vandorMobile = driver.find_element(By.XPATH, "/html/body/div[1]/section[2]/div[2]/div[1]/div[1]/div[6]/div/div[5]/a")
        vandorAddress = driver.find_element(By.XPATH, "/html/body/div[1]/section[2]/div[2]/div[1]/div[1]/div[6]/div/div[6]")
        vandorEmail = driver.find_element(By.XPATH, "/html/body/div[1]/section[2]/div[2]/div[1]/div[1]/div[6]/div/div[7]/a")

        print(horse_name.text, horseDob.text, horseSire.text, horseDam.text, horseCob.text, horseSex.text, horseCategory.text, vandorName.text, vandorPhone.text, vandorMobile.text, vandorAddress.text, vandorEmail.text)
        csvwriter.writerow([horse_name.text, horseDob.text, horseSire.text, horseDam.text, horseCob.text, horseSex.text, horseCategory.text, vandorName.text, vandorPhone.text, vandorMobile.text, vandorAddress.text, vandorEmail.text])
        time.sleep(1) #sleep for 1 sec

time.sleep(5) #sleep for 1 sec
driver.quit()


