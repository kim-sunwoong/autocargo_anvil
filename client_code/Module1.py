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