from ._anvil_designer import NavbarTemplate
from anvil import *
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Navbar(NavbarTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('LandingForm')

  def link_2_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('LoginForm')


