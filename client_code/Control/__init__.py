from ._anvil_designer import ControlTemplate
from anvil import *
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import plotly.graph_objects as go

class Control(ControlTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.pinky_battery = "80"
    self.lb_power.text = self.pinky_battery
    

    #Set the contents of the data grid (which has a repeating panel inside) to the contents of 
    #the Files table. This is done on the secure server where you might only want to return user-visible data
    #self.repeating_panel_1.items = anvil.server.call('return_table')

  #Update the values in the line graph based on the selected value of the drop down menu
  def drop_down_1_change(self, **event_args):
    """This method is called when an item is selected"""
    self.y_values = anvil.server.call('return_data', self.drop_down_1.selected_value)
    self.create_line_graph()
