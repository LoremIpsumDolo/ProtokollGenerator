import pandas as pd
from app import config


class ExcelReader:

	def __init__(self) -> None:
		self.Columns = config.Columns
		self.SourceFile = config.PathTo_ExcelFile
		self.SheetName = config.SheetNames
		self.Data = self.mapValues()


	def readExcelFile(self) -> dict:
		"""
		It reads an Excel file and returns a dictionary of pd-dataframes
		:return: A dictionary of the data as a pd-dataframe in the excel file.
		"""
		return pd.read_excel(self.SourceFile,
		                     sheet_name=self.SheetName,
		                     usecols=self.Columns)


	def mapValues(self) -> dict:
		"""
		It reads an Excel file and returns a dictionary with the ID as key and the model and serial number as values
		"""
		IDs = {}
		SheetDict = self.readExcelFile()

		for sheet in SheetDict:
			df = SheetDict[sheet].to_dict(orient='records')
			for row in df:
				IDs[row["ID"]] = {
						"Modell"      : row["Modell"],
						"Seriennummer": row["Seriennummer"]}

		return IDs
