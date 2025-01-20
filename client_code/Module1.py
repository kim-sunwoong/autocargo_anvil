import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
# This is a module.
# You can define variables and functions here, and use them from any form. For example, in a top-level form:
#
#    from .. import Module1
#
#    Module1.say_hello()
#


def say_hello():
  print("Hello, world")

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
          return True
    except anvil.users.AuthenticationFailed:
        alert("Incorrect email or password. Please try again.", title="Login Failed")
    except Exception as e:
        alert(f"An unexpected error occurred: {e}", title="Error")

