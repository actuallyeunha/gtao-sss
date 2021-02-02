## GTA ONLINE - SOLO SESSION SCRIPT ~ BY: EUNHA ##
import psutil
from os import system, name
from time import sleep
from rich.console import Console
from rich.style import Style

base_style = Style(color="#75d1ff", bold=True)
console = Console(color_system='auto', style=base_style)

def clear():
	if name == 'nt':
		_ = system('cls')
	else:
		_ = system('clear')

def checkGtaProcess():
	for proc in psutil.process_iter():
		try:
			if "GTA5".lower() in proc.name().lower():
				return True
		except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
			pass
		return False

def findGtaProcess():
	listOfProcesses = []
	for proc in psutil.process_iter():
		try:
			pinfo = proc.as_dict(attrs=['pid', 'name'])
			if "GTA5".lower() in pinfo['name'].lower():
				listOfProcesses.append(pinfo)
		except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
			pass
	return listOfProcesses

def main():
	gtaprocess = findGtaProcess()
	if len(gtaprocess) > 0:
		console.print("{+} Found GTA process.")
		for elem in gtaprocess:
			PID = elem['pid']
			console.print(f"Process ID: [#de099e]{PID}")
		console.print("{+} Suspending for [#de099e]12 [#75d1ff]seconds[#75d1ff]...")
		p = psutil.Process(PID)
		p.suspend()
		sleep(12)
		console.print("{+} Resuming[#75d1ff]...")
		p.resume()
		console.print("[#de099e]Done")
		console.print("Please verify if you are alone in the session.")
		console.print("If not, run the program again.")
	else:
		console.print("{-} GTA process not found, did you open the game?")


if __name__ == '__main__':
	clear()
	console.rule("- [#de099e]GTA Online -", style=base_style)
	console.print("[#de099e]Solo [#75d1ff]Public Session 1.0", justify='center')
	console.rule("[#de099e]by: eunha", style=base_style)
	with console.status("Working...", spinner='aesthetic', spinner_style="#09deda", speed=0.2):
		main()
	sleep(5)
