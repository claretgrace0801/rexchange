from ._anvil_designer import DOIQuestionsFormTemplate
from anvil import *
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

from ..AddQuestionDialog import AddQuestionDialog

class DOIQuestionsForm(DOIQuestionsFormTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    
    self.paper_data = properties['paper_data']
    self.paper_title = self.paper_data['title'][0]
      
    self.paper_title_link.text = self.paper_title
    self.paper_title_link.url = self.paper_data["URL"]
    
    self.authors_text.content = ", ".join(self.get_authors())
    
    self.get_questions()
    
    self.related_form.paper_data = self.paper_data
    
    # Any code you write here will run when the form opens.
  
  def get_authors(self):
    return [author['given'] + " " + author['family'] for author in self.paper_data['author']]

  def get_questions(self):
    questions = app_tables.questions_table.search(doi=self.paper_data["DOI"])
    question_titles = [{"q": question, "title": question['title'], "paper_data": self.paper_data} for question in questions]
    
    self.questions_list.items = question_titles

      
  def add_question(self, title, desc):
    n_rows = len(app_tables.questions_table.search())
    row = app_tables.questions_table.add_row(qid=n_rows,title=title, description=desc,
                                             answers=[], doi=self.paper_data['DOI'], author=anvil.users.get_user()['email'])
    alert("Question Added")
    self.get_questions()
    

  def add_question_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    
    if anvil.users.get_user() is None:
      open_form('LoginForm')
      return
    
    d = AddQuestionDialog()
    BUTTONS = [("Add", True, "primary")]
    to_add = alert(d, title="Add Question", dismissible=True, buttons=BUTTONS, large=True)
    
    if to_add:
      self.add_question(d.title_text.text, d.description_text.text)

