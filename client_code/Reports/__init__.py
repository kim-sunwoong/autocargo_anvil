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


    #Populate plot_1 with dummy data. All three Bar charts will be added to the same figure
    # self.plot_1.data = [
    #   go.Bar(
    #     x=[2019, 2020, 2021, 2022, 2023],
    #     y=[510, 620, 687, 745, 881],
    #     name="Europe"
    # ),
    #   go.Bar(
    #     x=[2019, 2020, 2021, 2022, 2023],
    #     y=[733, 880, 964, 980, 1058],
    #     name="Americas"
    # ),
    #   go.Bar(
    #     x=[2019, 2020, 2021, 2022, 2023],
    #     y=[662, 728, 794, 814, 906],
    #     name="Asia"
    # )
    # ]

    #Return the figure from the server to populate plot_2
    #self.plot_2.figure = anvil.server.call('return_bar_charts')

    #self.plot_3.data = [
    #  go.Pie(
    #    labels=["Mobile", "Tablet", "Desktop"],
    #    values=[2650, 755, 9525]
    #  )
    #]

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
    

    
