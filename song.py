from selenium import webdriver

class music():
    def __init__(self):
        options=webdriver.ChromeOptions()
        options.add_experimental_option("detach",True)
        self.driver = webdriver.Chrome(options=options)
    def play(self,query): 
        self.query=query
        self.driver.get(url="http://www.youtube.com/results?search_query="+query)
        video=self.driver.find_element('xpath','//*[@id="dismissible"]').click()
        