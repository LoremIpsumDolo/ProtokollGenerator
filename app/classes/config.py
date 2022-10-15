import json
from pathlib import Path
import os
import logging

logger = logging.getLogger(__name__)


class Config:

	def __init__(self) -> None:
		"""
		This function is the constructor of the class. It sets the current working directory and the path to the config file
		"""
		self.CWD = Path.cwd()
		self.ConfigFilePath = "app/config.json"
		self.ConfigFileContend = self.readFile()


	def readFile(self) -> dict:
		"""
		It opens the file, reads the file, and returns the file as a dictionary
		:return: A dictionary of the config file.
		"""
		with open(self.ConfigFilePath, "r") as file:
			return json.load(file)


	@property
	def PathTo_ExcelFile(self) -> Path:
		"""
		If the path to the Excel file is found in the configuration file, return the path to the Excel file
		:return: Path object
		"""
		if _path := self.ConfigFileContend["PathTo_ExcelFile"]:

			if not Path(_path).is_file():
				logger.error("PathTo_ExcelFile not found")

			return Path(_path)


	@property
	def OutputFile(self) -> Path:
		"""
		If the key "OutputfileName" exists in the dictionary "ConfigFileContend", return the value of that key, otherwise
		return the string "protocol.html"
		:return: The name of the output file.
		"""

		FileName = "protocol.html"
		if _fname := self.ConfigFileContend["OutputFileName"]:
			FileName = _fname

		FullFilePath = Path(f"{self.CWD}/{FileName}")

		if Path(FullFilePath).is_file():
			os.remove(FullFilePath)

		return FullFilePath


	@property
	def SheetNames(self) -> list:
		"""
		It returns a list of sheet names from the config file
		:return: A list of sheet names.
		"""

		if _sheetList := self.ConfigFileContend["SheetNames"]:
			return _sheetList


	@property
	def Columns(self) -> list:
		"""
		It returns the columns of the table.
		:return: A list of the columns in the table.
		"""
		if _cols := self.ConfigFileContend["Columns"]:
			return _cols


	@property
	def DateFormat(self) -> str:
		"""
		If the key "DateFormat" exists in the dictionary "ConfigFileContend", return the value of the key, otherwise return the
		string "%d.%m.%Y"
		:return: The value of the key "DateFormat" in the dictionary "ConfigFileContend"
		"""
		if _format := self.ConfigFileContend["DateFormat"]:
			return _format
		else:
			return "%d.%m.%Y"


	@property
	def IT_MitarbeiterName(self) -> str:
		"""
		The function returns the name of the IT employee
		:return: The value of the key "IT_MitarbeiterName" in the dictionary "ConfigFileContend"
		"""
		if _mitarbeiter := self.ConfigFileContend["IT_MitarbeiterName"]:
			return _mitarbeiter
