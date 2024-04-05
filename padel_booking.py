from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import os
from dotenv import load_dotenv

def clickCorrectBookingElement(dayTime: int):
    weekDay = datetime.now().weekday()

    overviewTargetBooking = driver.find_element(By.XPATH, '//*[@id="bs_pl2D73EF61A8"]/tbody/tr[' + str(dayTime - 6) + ']/td[' + str(weekDay + 1) + ']/input')
    overviewTargetBooking.click()

if __name__ == "__main__":

    dotenv_path = ".env"  # Path to the .env file
    load_dotenv(dotenv_path)
    userMail = os.getenv('USER_MAIL')
    userPassword = os.getenv('USER_PASSWORD')
    dayTimes = [15]

    driver = webdriver.Firefox()
    driver.get('https://www.hochschulsport-muenster.de/angebote/aktueller_zeitraum_0/_Padel_Tennis.html')

    for dayTime in dayTimes:

        # reset to first window 
        driver.switch_to.window(driver.window_handles[0])

        # find correct booking element
        clickCorrectBookingElement(dayTime)

        # switch to second tab and find correct detail booking element
        driver.switch_to.window(driver.window_handles[1])

        detailTargetBooking = driver.find_element(By.XPATH, '/html/body/form/div/div[2]/div/div[2]/div[1]/label/div[2]/input')
        detailTargetBooking.click()

        # signIn with email and password
        signInElement = driver.find_element(By.XPATH, '//*[@id="bs_pw_anmlink"]/div[2]')
        signInElement.click()

        emailField = driver.find_element(By.XPATH, '//*[@id="bs_pw_anm"]/div[2]/div[2]/input')
        emailField.send_keys(userMail)
        passwordField = driver.find_element(By.XPATH, '//*[@id="bs_pw_anm"]/div[3]/div[2]/input')
        passwordField.send_keys(userPassword)

        signInButton = driver.find_element(By.XPATH, '//*[@id="bs_pw_anm"]/div[5]/div[1]/div[2]/input')
        signInButton.click()

        # check datapolicy checkbox and proceed booking
        datapolicyCheckbox = driver.find_element(By.XPATH, '//*[@id="bs_bed"]/label/input')
        datapolicyCheckbox.click()

        proceedBookingButton = driver.find_element(By.XPATH, '//*[@id="bs_submit"]')
        proceedBookingButton.click()

        # finally submit booking
        finalBookingButton = driver.find_element(By.XPATH, '//*[@id="bs_foot"]/div[1]/div[2]/input')
        finalBookingButton.click()
        driver.close()

    driver.quit()