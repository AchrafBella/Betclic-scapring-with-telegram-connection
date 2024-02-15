import os
import re
from time import sleep

# Third-party library imports
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Local imports
from utils import initialize_empty_list, read_list_from_file, update_list_and_file


# change URL base on the category
BASE_URL = 'https://www.betclic.fr/'
URL = 'https://www.betclic.fr/tennis-s2'

def get_match_links(url: str=URL) -> dict:
    
    response = requests.get(url)
    if response.status_code == 200:
        
        soup = BeautifulSoup(response.text, 'html.parser')
        href_attributes = [BASE_URL+a.get('href') for a in soup.find_all('a') if '/tennis-s2/' in a.get('href')]
        matchs_link = [href.encode('ascii', 'ignore').decode('unicode_escape') for href in href_attributes]

        return {"Error": False, "links": matchs_link}
    else:
        return{"Error": True}

def create_tennis_driver(link: str):

    # set up Chrome driver
    options = Options()
    options.add_argument('--no-sandbox')
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    # Navigate to the webpage you want to scrape
    driver.get(link)

    try:
        # coockies
        driver.find_element("xpath", '//*[@id="popin_tc_privacy_button_2"]').click()
        driver.implicitly_wait(3)
        # click to "points et service"
        x_path = '//*[@id="matchHeader"]/div/sports-category-filters/bcdk-tabs/div/div/div/div[last()]/span'
        driver.find_element("xpath", x_path).click()
        return driver
    
    except Exception as e:
        return None  

def retrieve_tennis_point_service(driver: webdriver):
    class_name = 'block'
    point_service = driver.find_element(By.CLASS_NAME, class_name)
    info = point_service.text
    return info

def get_tennis_matches(update, context):

    match_links = get_match_links()

    if match_links.get('Error'):
        #print("we have a problem of too many requests")
        context.bot.send_message(chat_id=update.effective_chat.id, text='There was too many requests, please try later.')
    elif len(match_links.get('links')) == 0:
        context.bot.send_message(chat_id=update.effective_chat.id, text="We cannot retrieve data for the moment.")
    else:
        links = match_links.get('links')

    if os.path.exists('visited_url.sav'):
        pre_existing_urls = read_list_from_file('visited_url.sav')
    else:
        initialize_empty_list('visited_url.sav')
        pre_existing_urls = read_list_from_file('visited_url.sav')

    for url in links:
        if url not in pre_existing_urls:
            driver = create_tennis_driver(url)
            if driver is None:
                context.bot.send_message(chat_id=update.effective_chat.id, text='There was an exception, please try again.')
            else:
                info = retrieve_tennis_point_service(driver)
                sleep(1)
                try:
                    result = re.search(r'Aces(.*?)0 selection', info, re.DOTALL)
                    if result:
                        extracted_text = result.group(1).strip()
                        context.bot.send_message(chat_id=update.effective_chat.id, text=extracted_text)
                        update_list_and_file(url, 'visited_url.sav')
                except Exception:
                    #print("No Aces found.")
                    context.bot.send_message(chat_id=update.effective_chat.id, text='No Aces found.')
    context.bot.send_message(chat_id=update.effective_chat.id, text='We finish checking all matchs')

def create_basket_driver(link: str):
    pass

def retrieve_basket_driver(driver: webdriver):
    pass

def get_basketBall_matches(update, context):
    pass