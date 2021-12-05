from ._anvil_designer import LoginFormTemplate
from anvil import *
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

import custom_signup.login_flow

class LoginForm(LoginFormTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
  
  def login_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    custom_signup.login_flow.login_with_form()
    
    if anvil.users.get_user() is not None:
      alert("Logged in as " + anvil.users.get_user()['email'])
      open_form('LandingForm')
    
    
  def signup_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    custom_signup.login_flow.signup_with_form()

