from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
import threading

website = 'https://www.jpg.store/collection/'
path = '/users/roy/Desktop/chromedriver'
ptojects_file_path = '/users/roy/Desktop/projects.txt'

threads = []
floors = {}

def get_elements_from_rtf(path):
    with open(f"{path}", "r") as file:
        elements = file.readlines()
    i=0
    for element in elements:
        elements[i] = element.strip()
        i+=1
    return elements


def get_floor(project_name):
    # setup for brave
    option = webdriver.ChromeOptions()
    option.binary_location = ('/Applications/Brave Browser.app/Contents/MacOS/Brave Browser')

    srvc = Service(executable_path=path)
    driver = webdriver.Chrome(service=srvc, options=option)
    driver.get(f"{website}{project_name}")
    time.sleep(3)
    # NFTMarketplaceCard_nftMarketplaceCardPrice__H744p

    price = driver.find_element(by="xpath", value='//span[@id="asset-price"]').text
    print(f"floor price of {project_name} is: {price}")
    floors[project_name] = price

def start():
    projects = get_elements_from_rtf(path=ptojects_file_path)

    for project in projects:
        proj_thread = threading.Thread(target=get_floor, args=(project,))
        threads.append(proj_thread)
        proj_thread.start()

    for thread in threads:
        thread.join()

    return floors







