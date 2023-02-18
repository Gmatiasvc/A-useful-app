# Generic commands
# This file exist because I dont want to make cli.py a command mess
# I want cli.py a switch statement mess
# Not a code mess
# -Gmatiasvc
import platform
import os
import rich
import datetime
from rich.console import Console
from rich.table import Table
from rich import box
console = Console()

from datetime import datetime
now = datetime.now()

genrics = [
	"whoami",       # Shows info about the user, passed at the start of the program => DONE
	"clear",		# Clears the console using os lib => DONE
	"cls",			  # Clear alias
	"clean",		  # Clear alias
	"date",         # Shows date using datetime lib
	"time",         # Shows time using datetime lib
	"datetime",     # Shows date and time using datetime lib
	"sysinfo",      # Shows system information 
	"network"       # Shows internet info
]


"""
Userinfo documentation:
This command generates a table with some local and global info about the instance running the app.
This command is meant to be expanded.

Userinfo table structure:

	Passed by a list as an argument, list name hardcoded
user -> str
userID -> int
perms -> str


osuser -> str
osname -> str
osver -> str

"""

def whoami_os_name():
	if os.name == "nt":
		return platform.system() + " " + platform.release()
	else:
		return platform.release()

def whoami(userinfo):

	table_whoami = Table(title="User Info",box=box.HEAVY_EDGE)
	table_whoami.add_column("Data Requested", justify="right", style="magenta")
	table_whoami.add_column("Data Value", justify="left",style="cyan")
	table_whoami.add_column("Data Perms", justify="left")

	table_whoami.add_row("Username",userinfo[0],"[blue]LOCAL")
	table_whoami.add_row("User ID",userinfo[1],"[blue]LOCAL")
	table_whoami.add_row("User perms",userinfo[2],"[blue]LOCAL")


# fetching data using os library and platform library
# os logged user
	try:
		table_whoami.add_row("OS Logged User",os.getlogin(),"[bright_green]PUBLIC")
	except:
		table_whoami.add_row("OS Logged User","Couldn't get info","[bright_red]ERROR / SUDO")

# os name
	try:
		table_whoami.add_row("OS Name",f"{platform.system()} | {os.name}","[bright_green]PUBLIC")
	except:
		table_whoami.add_row("OS Name","Couldn't get info","[bright_red]ERROR / SUDO")


#os version
	try:
		table_whoami.add_row("OS Version",whoami_os_name(),"[bright_green]PUBLIC")
	except:
		table_whoami.add_row("OS Version","Couldn't get info","[bright_red]ERROR / SUDO")


	console.print(table_whoami)


"""
Clear command documentation:
it clears the console in an overcomplicated way, just it.
"""
def clear(args):

	if os.name == "nt":
		os.system("cls")

		if args in ["-nt", "nt", "notitle", "--notitle"]:
			pass
		else:
			console.print("[green]A (kinda) useful app CLI enviroment [DevBuild 2]")

	else:
		os.system("clear")
		if args in ["-nt", "nt", "notitle", "--notitle"]:
			pass
		else:
			console.print("[green]A (kinda) useful app CLI enviroment [DevBuild 2]")

"""
Date, time and datetime documentation:

- Date command outputs the date it was executed
- Time command outputs the time it was executed
- Datetime merges the other two

The functions use the datetime library
"""
def date(now):
	date = now.strftime("%B %d, %Y")
	console.print("[magenta1]La fecha de hoy es: " + date)


def time(now):
	time =now.strftime("%H:%M:%S")
	console.print("[magenta1]La hora de hoy es: " + time)

def datetime(now):
	date = now.strftime("%B %d, %Y")
	time =now.strftime("%H:%M:%S")
	console.print("[magenta1]La fecha y hora de hoy son: " + date + "  " +time)


GenericsExe = {
	"whoami" 	:  "generics.whoami(usrinfo)",
	"clear" 	:  "generics.clear(commands[1])",
	"clean" 	:  "generics.clear(commands[1])",
	"cls"   	:  "generics.clear()",
	"date"		:  'generics.date(public_now)',
	"time"		:  "generics.time(public_now)",
	"datetime"	:  "generics.datetime(public_now)",
	"sysinfo"	:  "print(\"WIP\")",
	"nework"	:  "print(\"WIP\")",
	"ip"		:  "print(\"WIP\")",
	"ipconfig"	:  "print(\"WIP\")"
}


if __name__ == "__main__":
	date()
	time()
	datetime()