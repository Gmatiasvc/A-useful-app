#imports
import rich
from rich.console import Console
import argparse

console = Console()

#main
def main():
    console.print("A (kinda) useful app CLI enviroment [DevBuild 1]\n")
    while True:
        command = console.input("[deep_sky_blue3]$ ")
        cmd = command.split(" ")
        if cmd[0] in ["exit"]:
            break


#tests
if __name__ == "__main__":
    main()