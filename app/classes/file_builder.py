from app import config
from jinja2 import Environment, FileSystemLoader
import os
from datetime import datetime
import webbrowser

file_loader = FileSystemLoader('app/templates')
env = Environment(loader=file_loader)
template = env.get_template('protocol_template.html')


class FileBuilder:

	def __init__(self, data: dict):
		"""
		The function __init__() is a constructor that initializes the class with the data from the config file
		:param data: The data to be written to the file
		:type data: dict
		"""
		self.Outfile = config.OutputFile
		self.DateFormat = config.DateFormat
		self.IT_MitarbeiterName = config.IT_MitarbeiterName
		self.EmpfaengerName = "Jon Doe"
		self.Data = data


	@property
	def Date(self):
		"""
		It returns the current date in the format specified by the DateFormat property
		:return: The current date in the format specified by the DateFormat property.
		"""
		now = datetime.now()
		return now.strftime(self.DateFormat)


	def createTemplate(self):
		"""
		The function takes the template, the data, and the date, and writes the output to a file
		"""

		output = template.render(content=template,
		                         Data=self.Data,
		                         Date=self.Date,
		                         IT_MitarbeiterName=self.IT_MitarbeiterName,
		                         EmpfaengerName=self.EmpfaengerName)

		with open(self.Outfile, mode="w", encoding="utf-8") as message:
			message.write(output)

		webbrowser.open('file://' + os.path.realpath(self.Outfile))
