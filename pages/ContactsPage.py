from selenium.webdriver.common.by import By
from BasePage import BasePage
from selenium.webdriver.support import expected_conditions as EC


class Contact(BasePage):
    submit_click = (By.LINK_TEXT,'Submit')

    forename_text = (By.CSS_SELECTOR,"#forename")
    email_text = (By.CSS_SELECTOR, "#email");
    message_text = (By.CSS_SELECTOR, "#message");

    email_error = (By.CSS_SELECTOR,"#email-err")
    message_error = (By.CSS_SELECTOR,'#message-err');
    forname_error = (By.CSS_SELECTOR,'#forename-err');

    success_message_text = (By.XPATH, "//div[@class='alert alert-success']")
    header_message = (By.CSS_SELECTOR,".alert")
    header_message_text = (By.CSS_SELECTOR,"#header-message");
    back_button = (By.XPATH,"//a[normalize-space()='« Back']")

    def click_submit_button(self):
        """Click submit button on contacts page
        """
        self._wait.until(EC.presence_of_element_located(self.submit_click))
        self.find_element(self.submit_click).click();

    def get_message_from_header(self):
        """Get top header message from UI.

        Returns:
            str: Header text from the top of the UI page.
        """
        self._wait.until(EC.visibility_of_all_elements_located(self.header_message))
        return self.find_element(self.header_message).text

    def validate_forename_error_when_blank(self):
        """This method will read UI error message when forename is not entered.

        Returns:
            str: Error message close to the forename text field
        """
        return self.find_element(self.forname_error).text

    def validate_email_error_when_blank(self):
        """This method will read UI error message when email is not entered correctly.

        Returns:
            str: Error message close to the email text field
        """
        return self.find_element(self.email_error).text

    def validate_message_error_when_blank(self):
        """This method will read UI error message when message fields is not entered correctly.

        Returns:
            str: Error message close to message field.
        """
        return self.find_element(self.message_error).text

    def set_forename(self, user_name: str):
        """This method willl set forename in the text field.

        Args:
            user_name (str): username 
        """
        self._wait.until(EC.visibility_of_element_located(self.forename_text))
        self.find_element(self.forename_text).clear()
        self.find_element(self.forename_text).send_keys(user_name)

    def set_email(self, email_id: str):
        """This method willl set forename in the email field.

        Args:
            email_id (str): emailid in the Email format.
        """
        self._wait.until(EC.visibility_of_element_located(self.email_text))
        self.find_element(self.email_text).clear()
        self.find_element(self.email_text).send_keys(email_id)

    def set_message(self, message: str):
        """set message in the message field.

        Args:
            message (str): message
        """
        self._wait.until(EC.visibility_of_element_located(self.message_text))
        self.find_element(self.message_text).clear()
        self.find_element(self.message_text).send_keys(message)

