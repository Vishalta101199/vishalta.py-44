test_data = [
    ("TC_Login_01", "Admin", "admin123", "Success"),  # Valid Login
    ("TC_Login_02", "Admin", "invalid_password", "Invalid Credentials"),  # Invalid Password
    ("TC_PIM_01", "John Doe", "john.doe@example.com", "Employee Added"),  # Add Employee
    ("TC_Pim_02", "Existing Employee ID", "Updated Details", "Employee Updated"),  # Edit Employee
    ("TC_Pim_03", "Employee to Delete ID", None, "Employee Deleted"),  # Delete Employee (No expected password for deletion)
]

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from test_data import test_data  # Import your test data

class TestOrangeHRM:

    def setup_method(self):
        self.driver = webdriver.Chrome()  # Replace with your browser's webdriver
        self.driver.get("https://opensource-demo.orangehrmlive.com/")  # Replace with your OrangeHRM URL

    def teardown_method(self):
        self.driver.quit()

    @pytest.mark.parametrize("test_id, username, password, expected_result", test_data)
    def test_login(self, test_id, username, password, expected_result):
        # Login steps
        username_field = self.driver.find_element(By.ID, "txtUsername")
        username_field.send_keys(username)
        password_field = self.driver.find_element(By.ID, "txtPassword")
        password_field.send_keys(password)
        self.driver.find_element(By.ID, "btnLogin").click()

        # Check for successful login or presence of error message
        if expected_result == "Success":
            assert self.driver.find_element(By.ID, "welcome").is_displayed()  # Check for successful login element
        else:
            error_message = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "spanMessage"))
            ).text
            assert expected_result in error_message

    @pytest.mark.parametrize("test_id, name, details, expected_result", test_data[2:])
    def test_pim(self, test_id, name, details, expected_result):
        # Implement specific steps for adding, editing, and deleting employees
        # based on OrangeHRM functionalities and your test data

        # Example for adding an employee (replace with actual implementation)
        if test_id == "TC_PIM_01":
            # Navigate to PIM module, find add employee element, enter details from test data, save
            # Assert success message based on expected_result
            pass

        # Implement similar logic for editing and deleting employees based on your test data
