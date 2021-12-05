from ._anvil_designer import QuestionFormTemplate
from anvil import *
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

from ..AddAnswerDialog import AddAnswerDialog 

class QuestionForm(QuestionFormTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    self.paper_data = properties['paper_data']
    self.paper_title = self.paper_data['title'][0]
    self.question = properties['q']
    
    # Any code you write here will run when the form opens.
      
    self.paper_title_link.text = self.paper_title
    self.paper_title_link.url = self.paper_data["URL"]
    
    self.question_title_text.content = self.question['title']
    self.question_description_text.content = self.question['description']
    
    self.question_author_text.content = "Asked by " + self.question['author']
    
    # answers
    self.get_answers()
    
    self.related_form.paper_data = self.paper_data

  def add_answer_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    if anvil.users.get_user() is None:
      open_form('LoginForm')
      return
    
    d = AddAnswerDialog()
    BUTTONS = [("Add", True, "primary")]
    to_add = alert(d, title="Add Answer", dismissible=True, buttons=BUTTONS, large=True)
    
    if to_add:
      self.add_answer(d.answer_text.text)
    
  def get_answers(self):
    parsed_answers = [{"answer": answer['answer'],
                       "author_text": "Answered by " + answer['author']}
                      for answer in self.question['answers']]
    self.answers_list.items = parsed_answers
    
  def add_answer(self, answer_text):
    row = app_tables.questions_table.get(qid=self.question['qid'])
    
    answers = row['answers']
    answers.append({"answer": answer_text, "author": anvil.users.get_user()['email']})
    row.update(answers=answers)
    
    self.question = row
    self.get_answers()
    
    alert("Answer Added")
