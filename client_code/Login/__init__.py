from ._anvil_designer import LoginTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class Login(LoginTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    

  def login_btn_click(self, **event_args):
    email = self.email_box.text
    password = self.password_box.text
    
    try:
        user = anvil.users.login_with_email(email, password)
        if user:
            alert("Login successful!", title="Welcome")
    except anvil.users.AuthenticationFailed:
        alert("Incorrect email or password. Please try again.", title="Login Failed")
    except anvil.users.UserNotFound:
        alert("No account found for this email. Please sign up.", title="Login Failed")