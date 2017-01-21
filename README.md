# Kali-Setup

#Fully automated bash script to setup your Kali system, Tested on Kali 2016.2 Vmware x64.

The idea came to me when I was taking OSCP (Offensive Security Certified Professional) , it was my own initiative and even tho I've worked hard on it it's far from perfection, I used this script as a  learning process as well wich is the main reason why I did several things using different methologies.

I did use some lines from G0tmilk script however must of lines can be found on the web.

Some of the repos are included in the FULL Kali Distribution, I also added new software as result of my reasearch fixing problems.


Express Install: It will install basic apps and configure services and your system for daily use.

	Atom   		          				 Asciinema       							Pure-FTPd
	Hexchat         					 Shutter         							Apache2
	Terminator        					 htop           							Mysql
	Conky             			 		 psmisc         							SSH
	Icedove           					 Pipe Vievwer   			 				Tftp
	LibreOffice       			 		 Filezilla


Full Install: It will Install Express module apps, full package repos and let your system ready for Pentesting.

	MSF				OpenVas			Sshuttle			GCC			MITMf			Wig				GoBuster
	Armitage		VFeed			Pfi					MinGW		Wordlists		CMSmap			reGeorg	
	Python			Graudit			AccessChk			Wine		Smbspider		Droopescan		Patetor
	Pycharm			Daemonfs		PsExec.exe			Hyperion	CrackMapExec	Crowbar			Clusterd
	Wdiff			Proxychains		Veil-framework		BDFProxy	Credcrack		Subterfuge		Webhandler
	Vbindiff		HttpTunnel		OP-Packers			BetterCap	Empire			Azazel			Gnmap-Parser
	


Just do: 

# git clone https://github.com/kawaxi/kali-setup

For help do:

# start -h



Pending Ideas: 
* Working with counters inside modules
* Fix IRC Bouncer Configuration ( it fails to replace one line)
* Need to Include personalized exploits to exploit DB.
* Need to fix time no longer syncing  after resuming VM, you need to do it manually.



