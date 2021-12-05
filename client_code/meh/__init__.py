from ._anvil_designer import mehTemplate
from anvil import *
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class meh(mehTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.paper_data = properties['paper_data']
    
    self.paper_title = self.paper_data['title'][0]
    print(self.get_authors())

    # Any code you write here will run when the form opens.
  
  def get_authors(self):
    return [author['given'] + " " + author['family'] for author in self.paper_data['author']]
  
  