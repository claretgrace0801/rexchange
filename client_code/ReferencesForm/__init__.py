from ._anvil_designer import ReferencesFormTemplate
from anvil import *
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class ReferencesForm(ReferencesFormTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    
    self.paper_data = properties['paper_data']
    
    self.paper_title_link.text = self.paper_data['title'][0]
    self.paper_title_link.url = self.paper_data["URL"]
    
    # Any code you write here will run when the form opens.
    self.authors_text.content = ", ".join(self.get_authors())
    
    self.get_references()
    
  def get_authors(self):
    return [author['given'] + " " + author['family'] for author in self.paper_data['author']]

  
  def get_references(self):
    references = self.paper_data['reference']
    
    references_list = []
    for i in range(len(references)):
      try:
        if "DOI" in references[i]:
          doi = references[i]["DOI"]
          url = "https://api.crossref.org/works/" + doi.lower()
          paper_data = http.request(url, json=True)['message']
          references_list.append(paper_data)
      except http.HttpError as e:
        pass
      
    self.references_repeating_panel.items = references_list
