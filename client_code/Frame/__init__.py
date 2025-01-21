from ._anvil_designer import FrameTemplate
from anvil import *
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from ..Control import Control
from ..Reports import Reports
from ..Login import Login
from datetime import datetime


class Frame(FrameTemplate):
    def __init__(self, **properties):
      # Set Form properties and Data Bindings.
      self.init_components(**properties)
      # Set the Plotly plots template to match the theme of the app
      Plot.templates.default = "material_light"
      # Add the Login form and set up the callback
      login_form = Login()
      login_form.on_login_success = self.login_success  # Set callback
      self.content_panel.add_component(login_form)
      self.user_login_status = False
  
      # Set initial styles
      self.signout_link.role = "default"
      self.date_label.text = datetime.today().strftime("%B %d, %Y")

    def login_success(self):
        self.content_panel.clear()
        self.content_panel.add_component(Control())
        self.user_login_status = True
        
        # Set styles to indicate the active page
        self.sales_page_link.role = "selected"
        self.reports_page_link.role = "default"
        self.signout_link.role = "default"

    def sales_page_link_click(self, **event_args):
      #if not self.user_login_status:
      if not self.user_login_status: # or이 추가됨 (anvil server DB 가능 ???) if not anvil.users.get_user() 
        alert("Please Login!", title="Login Failed")
      elif self.user_login_status:
        self.content_panel.clear()
        self.content_panel.add_component(Control())
        self.sales_page_link.role = "selected"
        self.reports_page_link.role = "default"
        self.signout_link.role = "default"

    def reports_page_link_click(self, **event_args):
      if not self.user_login_status: # if not anvil.users.get_user()
        alert("Please Login!", title="Login Failed")
      elif self.user_login_status:
        self.content_panel.clear()
        self.content_panel.add_component(Reports())
        self.reports_page_link.role = "selected"
        self.sales_page_link.role = "default"
        self.signout_link.role = "default"
      
    def signout_link_click(self, **event_args):
        self.user_login_status = False
        anvil.users.logout()
        self.content_panel.clear()
        login_form = Login()
        login_form.on_login_success = self.login_success  # Set callback
        self.content_panel.add_component(login_form)
      
        self.signout_link.role = "selected"
        self.reports_page_link.role = "default"
        self.sales_page_link.role = "default"