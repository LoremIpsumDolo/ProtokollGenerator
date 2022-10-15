from app.classes.excel_reader import ExcelReader
from app.classes.file_builder import FileBuilder
from rich.prompt import Prompt
from app import logger
import sys


def run(id=None) -> None:
	IDs = ExcelReader().Data

	if id:
		FileBuilder(IDs.get(id)).createTemplate()
		sys.exit(0)
		

	print("Type: (q) to quit")

	if dev_id := Prompt.ask("Enter ID"):
		dev_id = str(dev_id).upper()  # makes response case insensitive

		if dev_id == "Q":
			sys.exit(0)

		if data := IDs.get(dev_id):
			FileBuilder(data).createTemplate()
		else:
			logger.error(f"could not find '{dev_id}' in Excelsheet")
			run()


if __name__ == '__main__':
	run("NB008")
