from ._anvil_designer import ReportsTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
import plotly.graph_objects as go
from anvil.tables import app_tables
import plotly.graph_objects as go


class Reports(ReportsTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # Any code you write here will run before the form opens.

  def warehouse_map_click(self, points, **event_args):
    """This method is called when a data point is clicked."""
    pass

  def drop_down_1_change(self, **event_args):
    self.lb_robotid.text = self.drop_down_1.selected_value
    if self.drop_down_1.selected_value == "A1-2":
      self.lb_power.text = '75 %'
      self.lb_status.text = "Deactivate"
      self.lb_status.font_color = "#007EBC"
    pass
    

    
