from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

NAVIGATOR_ERROR_MESSAGE = 'SOMETHING WENT WRONG WITH THE NAVIGATOR!\nTHE LOGIN MUST BE DONE MANUALLY.'
EXPLICITWAIT = 5

# xpath locators
initial_pop_up_agree_btn_xpath = "//span[text()='Got it, thanks!']/parent::button"
sing_up_id = "jsid-signup-button"
login_a_tag_xpath = "//p[text()='Have an account? ']/a"
login_email_field_id = "login-email-name"
login_password_field_id = "login-email-password"
final_log_in_button_xpath = "//input[@type='submit' and @value='Log in']"


class GagNavigationTools:
    def __init__(self, webdriver):
        self.explicit_wait = EXPLICITWAIT
        self.driver = webdriver

    def click_button_xpath(self, locator):
        button = WebDriverWait(self.driver, self.explicit_wait).until(
            EC.presence_of_element_located((By.XPATH, locator))
        )
        button.click()

    def click_button_id(self, locator):
        button = WebDriverWait(self.driver, self.explicit_wait).until(
            EC.presence_of_element_located((By.ID, locator))
        )
        button.click()

    def insert_in_field_id(self, locator, text):
        field = WebDriverWait(self.driver, self.explicit_wait).until(
            EC.presence_of_element_located((By.ID, locator))
        )
        field.send_keys(text)


def log_in_9gag(webdriver, username, password, gui_alert_instance):
    navigator = GagNavigationTools(webdriver)
    try:
        navigator.click_button_xpath(initial_pop_up_agree_btn_xpath)
        navigator.click_button_id(sing_up_id)
        navigator.click_button_xpath(login_a_tag_xpath)
        navigator.insert_in_field_id(login_email_field_id, username)
        navigator.insert_in_field_id(login_password_field_id, password)
        navigator.click_button_xpath(final_log_in_button_xpath)
    except TimeoutException:
        print(NAVIGATOR_ERROR_MESSAGE)
        alert = gui_alert_instance()
        alert.setText(NAVIGATOR_ERROR_MESSAGE)
        alert.exec_()
