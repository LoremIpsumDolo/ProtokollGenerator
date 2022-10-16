from app.classes.excel_reader import ExcelReader
from app.classes.file_builder import FileBuilder
from rich.prompt import Prompt
from rich.console import Console
from app import logger
import sys

console = Console()


def ask_for_DeviceID(IDs: dict) -> str:
	"""
	It asks the user for a device ID, checks if it's in the dict, and returns the data if it is

	:param IDs: dict
	:type IDs: dict
	:return: The data from the dict that matches the input
	"""
	print("Type: (q) to quit")

	if dev_id := Prompt.ask("Enter ID"):
		dev_id = str(dev_id).upper()  # makes response case insensitive

		if dev_id == "Q":
			sys.exit(0)

		if data := IDs.get(dev_id):  # check if input is in device ID dict
			logger.info(f"found matching entry for {dev_id}")
			return data
		else:
			logger.error(f"could not find '{dev_id}' in Excelsheet")
			ask_for_DeviceID()


def ask_for_Name() -> str:
	"""
	It asks for a name, formats it, and returns it
	:return: A string
	"""
	print("Type: (q) to quit")

	if _name := Prompt.ask("Enter Empfaenger Name (First Name -> Last Name)"):
		FormattedName = " ".join([name.capitalize() for name in _name.split()])
		console.clear()
		return FormattedName

	ask_for_Name()


def run() -> None:
	"""
	It asks the user for a device ID and a name, then creates a template file with the data from the device ID and the name
	"""
	IDs = ExcelReader().Data  # dict of all device IDs

	DeviceData = ask_for_DeviceID(IDs)
	EmpfaengerName = ask_for_Name()

	FileBuilder(DeviceData, EmpfaengerName).createTemplate()


if __name__ == '__main__':
	run()  # NB008
	logger.info("all done")

