from ._anvil_designer import LogoutTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Logout(LogoutTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def signin_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    #anvil.users.login_with_form()
    self.login_user()
  
  def login_user(self):
    try:
        # Prompt user to log in with email and password
        user = anvil.users.login_with_email(email="user@example.com", password="password123")
        if user:
            alert("Login successful!", title="Welcome")
        else:
            alert("Login failed. Please try again.", title="Error")
    except anvil.users.AuthenticationFailed:
        alert("Incorrect password. Please try again.", title="Login Failed")
    except anvil.users.UserNotFound:
        alert("No account found for this email. Please sign up first.", title="Login Failed")
    except Exception as e:
        alert(f"An unexpected error occurred: {e}", title="Error")
