from ._anvil_designer import QuestionsListRowTemplate
from anvil import *
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class QuestionsListRow(QuestionsListRowTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.

  def question_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('QuestionForm', q=self.item['q'], paper_data=self.item['paper_data'])

