from selenium import webdriver
from pages.training_ground_page import TrainingGroundPage
from pages.trial_page import TrialPage


# Test setup
browser = webdriver.Chrome()

# Trial page
trial_page = TrialPage(driver=browser)
trial_page.go()
trial_page.stone_input.input_text("rock")
trial_page.stone_button.click()

# Training grounds
training_page = TrainingGroundPage(driver=browser)
training_page.go()
assert training_page.button1.text == "Button1"
browser.quit()