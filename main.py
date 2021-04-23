from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
import pyautogui
import keyboard
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

username = "EMAIL GOES HERE"
password = "PASSWORD GOES HERE"
keywords = ["israel", "palestine", "scotland independence", "russia", "greensill affair", "myanmar", "chad", "qatar", "terrorism"]
folders = ["israel", "palestine", "scotland", "russia", "british government", "myanmar", "chad", "qatar", "terrorism"]
image_path = r"C:\Users\gchung22\Desktop\fast-catch-icon-128.png"
reputableNewsSources = ['foreignaffairs.com', 'theatlantic.com', 'politico.com', 'newyorker.com', 'economist.com', 'apnews.com', 'cnn.com', 'nytimes.com', 'bbc.com', 'washingtonpost.com', 'reuters.com', 'aljazeera.com', 'thegaurdian.com', 'wsj.com']
catches = 0
page = 7
k_index = 8
needed_catches = 100
maxWait = 100

chop = webdriver.ChromeOptions()
chop.add_extension(r'C:\Users\gchung22\Desktop\giahjhmjbiiopleefbmlmjfaafdihidd.crx')
chop.add_extension(r'C:\Users\gchung22\Desktop\bypass-paywalls-chrome.crx')
browser = webdriver.Chrome(ChromeDriverManager().install(), options=chop)
browser.maximize_window()
login = ActionChains(browser)
browser.get(r'chrome-extension://giahjhmjbiiopleefbmlmjfaafdihidd/index.html')
time.sleep(2.5)
currentHandle = browser.current_window_handle
for handle in browser.window_handles:
	if handle != currentHandle:
		browser.switch_to.window(handle)
		browser.close()
browser.switch_to.window(browser.window_handles[0])
# log in
try:
	element = WebDriverWait(browser, maxWait).until(ec.presence_of_element_located((By.XPATH, r'/html/body/fast-catch-app/div/fast-catch-login/fast-catch-header/form/div[1]/input[1]')))
finally:
	browser.find_element_by_xpath(r'/html/body/fast-catch-app/div/fast-catch-login/fast-catch-header/form/div[1]/input[1]').send_keys(username)
	browser.find_element_by_xpath(r'/html/body/fast-catch-app/div/fast-catch-login/fast-catch-header/form/div[1]/input[2]').send_keys(password)
	browser.find_element_by_xpath(r'/html/body/fast-catch-app/div/fast-catch-login/fast-catch-header/form/div[2]/fast-catch-actions/button').click()
time.sleep(2)

while k_index < len(keywords):
	while catches < int(needed_catches):
		for i in range(0, int(needed_catches / len(keywords) / 5)):
			if page > 40:
				k_index = k_index + 1
				page = 0
				break
			if keyboard.is_pressed('q'):
				browser.quit()
				break
			browser.get(r'http://google.com/search?q=' + keywords[k_index] + '&tbm=nws&start=' + str(page * 10))
			links = browser.find_elements_by_tag_name('a')
			for link in links:
				location = str(link.get_attribute('href'))
				works = False
				for source in reputableNewsSources:
					if source.lower() in location.lower() and keywords[k_index].split()[0].lower() in location.lower():
						works = True
						break
				if works:
					if keyboard.is_pressed('q'):
						browser.quit()
						break
					browser.execute_script('''window.open("''' + location + '''","_blank");''')
					browser.switch_to.window(browser.window_handles[1])
					time.sleep(1)
					failed = True
					while failed:
						try:
							pyautogui.click(2700 - 180, 100)
							time.sleep(1)
							browser.switch_to.frame(browser.find_element_by_id(r'fast-catch-KFoi8cNdjb'))
							failed = False
						except:
							failed = True
					
					try:
						element = WebDriverWait(browser, maxWait).until(ec.presence_of_element_located((By.XPATH, r'/html/body/fast-catch-app/div/fast-catch-dashboard/fast-catch-choose-team/fast-catch-body/fast-catch-user-options/form/div/div/fast-catch-actions/button[2]')))
					finally:
						browser.find_element_by_xpath(r'/html/body/fast-catch-app/div/fast-catch-dashboard/fast-catch-choose-team/fast-catch-body/fast-catch-user-options/form/div/div/fast-catch-actions/button[2]').click()
					
					try:
						element = WebDriverWait(browser, maxWait).until(ec.presence_of_element_located((By.XPATH, r'/html/body/fast-catch-app/div/fast-catch-dashboard/fast-catch-save-to/fast-catch-body/save-to-notification/pp-notice/div/div')))
					finally:
						catchCheck = browser.find_element_by_xpath(r'/html/body/fast-catch-app/div/fast-catch-dashboard/fast-catch-save-to/fast-catch-body/save-to-notification/pp-notice/div/div').text.lower()
					
					if not "Good news! Someone from The Pembroke Hill School has already caught this article.".lower() in catchCheck:
						browser.find_element_by_xpath(r'/html/body/fast-catch-app/div/fast-catch-dashboard/fast-catch-save-to/fast-catch-header/div/fast-catch-actions[1]/button[1]').click()
						try:
							element = WebDriverWait(browser, maxWait).until(ec.presence_of_element_located((By.XPATH, r'/html/body/fast-catch-app/div/fast-catch-dashboard/fast-catch-save-to/fast-catch-body/save-to-extemp-folders/save-to-extemp-sort-filter-create-folder/form/input')))
						finally:
							browser.find_element_by_xpath(r'/html/body/fast-catch-app/div/fast-catch-dashboard/fast-catch-save-to/fast-catch-body/save-to-extemp-folders/save-to-extemp-sort-filter-create-folder/form/input').send_keys(folders[k_index])
						time.sleep(1)
						j = 1
						while True:
							elements = browser.find_elements_by_xpath(r'/html/body/fast-catch-app/div/fast-catch-dashboard/fast-catch-save-to/fast-catch-body/save-to-extemp-folders/pp-save-to-list/pp-save-to-item/div/pp-save-to-label/p')
							content = ''
							if len(elements) == 0:
								content = browser.find_element_by_xpath(r'/html/body/fast-catch-app/div/fast-catch-dashboard/fast-catch-save-to/fast-catch-body/save-to-extemp-folders/pp-save-to-list/pp-save-to-item[' + str(j) + r']/div/pp-save-to-label/p').text
							else:
								content = elements[0].text
							if folders[k_index].lower() == content.lower():
								if len(elements) == 0:
									browser.find_element_by_xpath(r'/html/body/fast-catch-app/div/fast-catch-dashboard/fast-catch-save-to/fast-catch-body/save-to-extemp-folders/pp-save-to-list/pp-save-to-item[' + str(j) + r']/div/pp-save-to-label/p').click()
								else:
									browser.find_element_by_xpath(r'/html/body/fast-catch-app/div/fast-catch-dashboard/fast-catch-save-to/fast-catch-body/save-to-extemp-folders/pp-save-to-list/pp-save-to-item/div/pp-save-to-label/p').click()
								catches = catches + 1
								print(catches)
								break
							j = j + 1
							if j > 20:
								break
						browser.find_element_by_xpath(r'/html/body/fast-catch-app/div/fast-catch-dashboard/fast-catch-save-to/fast-catch-body/save-to-extemp-folders/fast-catch-actions/button[2]').click()
						time.sleep(0.5)
					browser.close()
					browser.switch_to.window(browser.window_handles[0])
			page = page + 1
browser.close()
