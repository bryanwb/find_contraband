from __future__ import with_statement
from fabric.api import * 
import datetime

def findContraband(path="/"):
	with hide('everything'):
		put('./find_contraband.py', '/tmp/', mirror_local_mode=True)
		result = run('/tmp/find_contraband.py ' + path)
	 	printReport(result)

def printReport(result):
	time = str(datetime.datetime.now())
	logName = "reports/" + env.host + ".log"
	repFile = open(logName, "a")	
	repFile.truncate()
	repFile.write("%s Scanning %s \n" % (time,env.host))
	repFile.write(result)
	repFile.close()

def hostsfile(filename):
    """Loads a group of hosts from a config file.

    group: name of the group file, one host per line
    """
    try:
        fhosts = open(filename)
    except IOError:
        abort('file not found: %s' % filename)

    def has_data(line):
        """'line' is not commented out and not just whitespace."""
        return line.strip() and not line.startswith('#')

    env.hosts = [ line.strip() for line in fhosts
                        if has_data(line)]
