import os
import gradio as gr
from datetime import datetime


def	custom_generate_chat_prompt(user_input, state, **kwargs):
	'''
	This extension will replace all instances of
	{{time}} and {{date}} with the current
	time and date, respectively
	Additionall replaces {{weekday}} with the day of the week.
	'''
	state['context'] = state['context'].replace('{{time}}',datetime.now().strftime("%I:%M %p")) 
	state['context'] = state['context'].replace('{{date}}',datetime.now().strftime("%B %d, %Y"))
	state['context'] = state['context'].replace('{{weekday}}',("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")[datetime.now().weekday()])
	# print(f'<<context, changed>>')
	# print(f'{state["context"]}')
	return 


def input_modifier(string):
	"""
	This function adds time context to each prompt.
	"""
	string += f' [Current time: {datetime.now().strftime("%I:%M %p")}]'
	return string

