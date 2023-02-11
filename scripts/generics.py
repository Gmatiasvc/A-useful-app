# Generic commands
# This file exist because I dont want to make cli.py a command mess
# I want cli.py a switch statement mess
# Not a code mess
# -Gmatiasvc

import rich
from rich.console import Console
from rich.table import Table
console = Console()

genrics = [
	"whoami",       # Shows info about the user, passed at the start of the program
	"date",         # Shows date using datetime lib
	"time",         # Shows time using datetime lib
	"datetime",     # Shows date and time using datetime lib
	"sysinfo",      # Shows system information 
	"Network"        # Shows internet info
]

def whoami(userinfo):

	table = Table(title="User Info")
	table.add_column("Data Requested", justify="right", style="green", box="HEAVY_EDGE")
