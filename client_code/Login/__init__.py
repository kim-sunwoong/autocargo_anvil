from ._anvil_designer import LoginTemplate  # Import the template for this form
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
from anvil.tables import app_tables

class Login(LoginTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)
        # Callback to the parent form
        self.on_login_success = None
        self.txt_password.hide_text = True

    def login_btn_click(self, **event_args):
        email = self.txt_email.text.strip()
        password = self.txt_password.text.strip()

        if not email or not password:
            alert("Please enter both email and password.", title="Missing Information")
            return

        try:
            user = anvil.users.login_with_email(email, password)
            if user:
                alert("Login successful!", title="Welcome")
                # Call the callback if it's set
                if self.on_login_success:
                    self.on_login_success()  # Trigger the parent's action
        except anvil.users.AuthenticationFailed:
            alert("Incorrect email or password. Please try again.", title="Login Failed")
        except Exception as e:
            alert(f"An unexpected error occurred: {e}", title="Error")