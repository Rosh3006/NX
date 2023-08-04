from selenium import webdriver

class infow():
    def __init__(self):
        options=webdriver.ChromeOptions()
        options.add_experimental_option("detach",True)
        self.driver = webdriver.Chrome(options=options)
    def get_info(self,query): 
        self.query=query
        self.driver.get(url="http://www.wikipedia.org")
        search=self.driver.find_element('xpath','//*[@id="searchInput"]')
        search.send_keys(query)
        enter=self.driver.find_element('xpath','//*[@id="search-form"]/fieldset/button').click()








    