from ._anvil_designer import RowTemplate2Template
from anvil import *
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class RowTemplate2(RowTemplate2Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.

  def title_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('DOIQuestionsForm', paper_data=self.item)

