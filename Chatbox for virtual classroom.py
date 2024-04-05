#!/usr/bin/env python
# coding: utf-8

# In[3]:


from ipywidgets import widgets
from IPython.display import display

class ChatBox:
    def __init__(self):
        self.messages = []
        
        # This is where the teacher will input their message in the chat
        self.teacher_input = widgets.Text(placeholder='Teacher input your message and press Enter...')
        
        # This is where the student will input their message in the chat 
        self.student_input = widgets.Text(placeholder='Student input your message and press Enter...')
        
        # This will produce the chatbox in a blue color
        self.output_area = widgets.Output(layout={'border': '1px solid blue'})

        # This function will show the chat box to the user  
        display(self.output_area)
        display(self.teacher_input)
        display(self.student_input)
        
        # This will let the user input a message in the chat box 
        self.teacher_input.on_submit(self.send_teacher_message)
        self.student_input.on_submit(self.send_student_message)
        
    # The def function will define the function for students to send messages between the teacher and students. 
    def send_teacher_message(self, sender):
        message = f'Teacher: {sender.value}'
        self.display_message(message, is_teacher=True)
        self.teacher_input.value = ''

    def send_student_message(self, sender):
        message = f'Student: {sender.value}'
        self.display_message(message, is_teacher=False)
        self.student_input.value = ''

    def display_message(self, message, is_teacher=True):
        with self.output_area:
            if is_teacher:
                print(f'\x1b[31m{message}\x1b[0m')  # Print teacher's message in red
            else:
                print(message)

# Chat box for the Established virtual classroom.
chat_box = ChatBox()




