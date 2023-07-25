import time
import csv
from datetime import date
import mandrill
import base64
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Your Mandrill API key
MANDRILL_API_KEY = 'hnYCG2OcRIiKrcdQBHRohA'
USER_ID = '3727'
USER_PASSWORD = 'HFCDAGZC'

# Please set total lot number befor using this application
TOTAL_LOT_NUMBER = 45

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

username_input.send_keys(USER_ID)
password_input.send_keys(USER_PASSWORD)
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

try:
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

        for index in range(1, TOTAL_LOT_NUMBER + 1):
        # for index in range(1, 3): # for test
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

    # Usage example
    if __name__ == "__main__":
        subject = "Crawling MagicMillions catalogues"
        message = "<p>Please, refer attached file.</p>"
        from_email = "system@bloodstockauction.com"
        to_email = "it@bloodstockauction.com"

        # Example attachment file path
        file_path = './result-'+formatted_date+'.csv'
        attachment_filename = 'result-'+formatted_date+'.csv'
        attachment_content = read_file_content(file_path)

        send_email_with_attachment(subject, message, from_email, to_email, attachment_filename, attachment_content)

except Exception as e:
    print("Catalogue is not live now")

driver.quit()

# read local file to attach emails
def read_file_content(file_path):
    with open(file_path, 'rb') as file:
        return file.read()

# send email function
def send_email_with_attachment(subject, message, from_email, to_email, attachment_filename, attachment_content):
    try:
        mandrill_client = mandrill.Mandrill(MANDRILL_API_KEY)

        attachment = {
            'type': 'text/csv',  # Adjust the MIME type according to the file being attached
            'name': attachment_filename,
            'content': base64.b64encode(attachment_content).decode()
        }

        message = {
            'from_email': from_email,
            'to': [{'email': to_email, 'type': 'to'}],
            'subject': subject,
            'html': message,
            'attachments': [attachment]
        }

        result = mandrill_client.messages.send(message=message)
        print("Email with attachment sent successfully!")
        print(result)

    except mandrill.Error as e:
        print(f"A Mandrill error occurred: {e}")