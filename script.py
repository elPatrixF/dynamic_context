import os
import gradio as gr
from datetime import datetime

params = {
	'timecontext': True,
	'datecontext': False,
}

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
	This function adds time or date context to each prompt.
	"""
	if params['timecontext'] : string += f' [Current time: {datetime.now().strftime("%I:%M %p")}]'
	if params['datecontext'] : string += f' [Current date: {datetime.now().strftime("%B %d, %Y")}]'
	return string


def ui():
	with gr.Accordion("Prompt context"):
		timecontext = gr.Checkbox(value=params['timecontext'], label='Add current time context to the end of the prompt')
		datecontext = gr.Checkbox(value=params['datecontext'], label='Add current date context to the end of the prompt')
	timecontext.change(lambda x: params.update({"timecontext": x}), timecontext, None)
	datecontext.change(lambda x: params.update({"datecontext": x}), datecontext, None)
