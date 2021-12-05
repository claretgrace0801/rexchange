from ._anvil_designer import RelatedFormTemplate
from anvil import *
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class RelatedForm(RelatedFormTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    
  def references_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('ReferencesForm', paper_data=self.paper_data)

