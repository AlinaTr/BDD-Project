from browser import Browser


class BasePage(Browser):

    def check_error_message(self, finder_tuple, expected_error_message):
        actual_error_message = self.chrome.find_element(*finder_tuple).text
        assert expected_error_message == actual_error_message



#finder_tuple = un tuplu care sa fie specific pt fiecare eroare de pe fiecre pagina