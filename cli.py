#imports
import rich
from rich.console import Console

from scripts import generics

console = Console()

#main
def main():
	console.print("A (kinda) useful app CLI enviroment [DevBuild 1]\n")


	while True:
		#get the user command
		command = console.input("[deep_sky_blue3]$ ")
		cmd = command.split(" ")

		if cmd[0] in ["exit"]:
			break

			#generics
		elif command[0] in generics:
			pass

#tests
if __name__ == "__main__":
	main()