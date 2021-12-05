from ._anvil_designer import LandingFormTemplate
from anvil import *
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class LandingForm(LandingFormTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.

  def search_doi(self, **event_args):
    """This method is called when the button is clicked"""
    url = "https://api.crossref.org/works/" + self.doi.text.lower()
    try:
      paper_data = http.request(url, json=True)['message']
      open_form('DOIQuestionsForm', paper_data=paper_data)
    except http.HttpError as e:
      alert("Paper not found")



