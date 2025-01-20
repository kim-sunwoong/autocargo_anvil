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
