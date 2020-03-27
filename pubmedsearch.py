from selenium import webdriver

#gets search input from text file
with open('input.txt', mode="r") as input_file:
	search= input_file.read()
print(search)

#opens pubmed
chrome_browser=webdriver.Chrome('./chromedriver')
chrome_browser.maximize_window()
chrome_browser.get('https://www.ncbi.nlm.nih.gov/pubmed')

#Assigns variable to search button 
search_button = chrome_browser.find_element_by_class_name("button_search")
print(search_button.get_attribute('innerHTML'))


search_input= chrome_browser.find_element_by_id("term")
search_input.clear()
search_input.send_keys(search + " ") #otherwise PubMed will think more input is needed
search_button.click()






