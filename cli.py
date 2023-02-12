#imports
import rich
from rich.console import Console

from scripts import generics

console = Console()

#main
def main(usrinfo):
	generics.clear(" ")

	while True:
		#get the user command
		cmd = console.input("[deep_sky_blue3]$ ")
		cmd = cmd.lower()
		commands = cmd.split(" ")
		commands.append(" ") # if this isnt here, the app colapses, this is an empty arg.

		if commands[0] in ["exit"]:
			break

			#generics
		elif commands[0] in generics.genrics:

			eval(generics.GenericsExe.get(commands[0]))

#tests
if __name__ == "__main__":
	main(["DEVELOPER","0","normal"])