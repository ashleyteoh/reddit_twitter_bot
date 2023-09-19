from selenium import webdriver
from selenium import common
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# driver = webdriver.Chrome('./chromedriver')
options = webdriver.ChromeOptions()
options.add_argument('start-maximized')
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(options=options)

class TwitterBot:

    """
    A Bot class that provide features of:
        - Logging into your Twitter account
        - Liking tweets of your homepage
        - Searching for some keyword or hashtag
        - Liking tweets of the search results
        - Posting tweets
        - Logging out of your account

    ........

    Attributes
    ----------
    email : str
        user email for Twitter account
    password : str
        user password for Twitter account
    bot : WebDriver
        webdriver that carry out the automation tasks
    is_logged_in : bool
        boolean to check if the user is logged in or not

    Methods
    -------
    login()
        logs user in based on email and password provided during initialisation
    logout()
        logs user out
    search(query: str)
        searches for the provided query string
    like_tweets(cycles: int)
        loops over number of cycles provided, scrolls the page down and likes the available tweets on the page in each loop pass
    """
    

    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.bot = driver
        self.is_logged_in = False
        self.tweet_limit = 280


    def login(self):
        bot = self.bot
        bot.get('https://twitter.com/i/flow/login')
        time.sleep(2)

        try:
            email = bot.find_element("name","text")
            email.clear()
            email.send_keys(self.email)
        except common.exceptions.NoSuchElementException:
            time.sleep(3)
            email = bot.find_element("name", "text")
            email.clear()
            email.send_keys(self.email)
        
        email.send_keys(keys.Keys.RETURN)


        try:
            password = bot.find_element("name", "password")
            password.clear()
            password.send_keys(self.password)
        except common.exceptions.NoSuchElementException:
            time.sleep(3)
            password = bot.find_element("name", "password")
            password.clear()
            password.send_keys(self.password)


        password.send_keys(keys.Keys.RETURN)
        time.sleep(5)
        self.is_logged_in = True


    def logout(self):
        if not self.is_logged_in:
            return 

        bot = self.bot
        bot.get('https://twitter.com/home')
        time.sleep(4)

        try:
            bot.find_element(By.XPATH, "//div[@data-testid='SideNav_AccountSwitcher_Button']").click()
        except common.exceptions.NoSuchElementException:
            time.sleep(3)
            bot.find_element(By.XPATH, "//div[@data-testid='SideNav_AccountSwitcher_Button']").click()

        time.sleep(1)

        try:
            bot.find_element(By.XPATH, "//a[@data-testid='AccountSwitcher_Logout_Button']").click()
        except common.exceptions.NoSuchElementException:
            time.sleep(2)
            bot.find_element(By.XPATH, "//a[@data-testid='AccountSwitcher_Logout_Button']").click()

        time.sleep(3)

        try:
            bot.find_element(By.XPATH, "//div[@data-testid='confirmationSheetConfirm']").click()
        except common.exceptions.NoSuchElementException:
            time.sleep(3)
            bot.find_element(By.XPATH, "//div[@data-testid='confirmationSheetConfirm']").click()

        time.sleep(3) 
        self.is_logged_in = False


    def search(self, query=''):
        if not self.is_logged_in:
            raise Exception("You must log in first!")

        bot = self.bot

        try:
            searchbox = bot.find_element(By.XPATH, "//input[@data-testid='SearchBox_Search_Input']")
        except common.exceptions.NoSuchElementException:
            time.sleep(2)
            searchbox = bot.find_element(By.XPATH, "//input[@data-testid='SearchBox_Search_Input']")

        searchbox.clear()
        searchbox.send_keys(query)
        searchbox.send_keys(keys.Keys.RETURN)
        time.sleep(5)  


    def like_tweets(self, cycles=10):
        if not self.is_logged_in:
            raise Exception("You must log in first!") 

        bot = self.bot   

        likes = 0
        while likes < cycles:
            try:
                bot.find_element(By.XPATH, "//div[@data-testid='like']").click()
                likes += 1
            except common.exceptions.NoSuchElementException:
                time.sleep(3)
                bot.execute_script('window.scrollBy(0,1000)') 
                time.sleep(3)

            time.sleep(1)
            # bot.execute_script('window.scrollTo(0,document.body.scrollHeight/1.5)') 
            # time.sleep(5)
        
        time.sleep(5)
        


      
    def post_tweets(self,tweetBody):
        if not self.is_logged_in:
            raise Exception("You must log in first!")

        bot = self.bot  

        try:
            bot.find_element(By.XPATH, "//a[@data-testid='SideNav_NewTweet_Button']").click()
        except common.exceptions.NoSuchElementException:
            time.sleep(3)
            bot.find_element(By.XPATH, "//a[@data-testid='SideNav_NewTweet_Button']").click()

        time.sleep(2) 
        body = tweetBody
        actions = ActionChains(driver)

        if len(tweetBody) > self.tweet_limit:
            while len(tweetBody) > self.tweet_limit:
                body = tweetBody[0:self.tweet_limit]
                tweetBody = tweetBody[self.tweet_limit:]
                try:
                    actions.send_keys(body)
                    actions.perform()
                except common.exceptions.NoSuchElementException:
                    time.sleep(3)
                    bot.find_element(By.XPATH, "//div[@role='textbox']").send_keys(body)
                
                try:
                    bot.find_element(By.XPATH, "//div[@aria-label='Add post']").click()
                except common.exceptions.NoSuchElementException:
                    time.sleep(3)
                    bot.find_element(By.XPATH, "//div[@aria-label='Add post']").click()

        try:
            actions.send_keys(tweetBody)
            actions.perform()
            # print(tweetBody)
        except common.exceptions.NoSuchElementException:
            time.sleep(3)
            bot.find_element(By.XPATH, "//div[@role='textbox']").send_keys(body)

        time.sleep(4)
        # bot.find_element(By.CLASS_NAME, "notranslate").send_keys(keys.Keys.ENTER)
        bot.find_element(By.XPATH, "//div[@data-testid='tweetButton']").click()
        time.sleep(4) 

