# Kali-Setup

#Fully automated bash script to setup your Kali system, Tested on Kali 2016.2 Vmware x64.

This idea came to me while taking the OSCP.  I took my own initiative to create this script, though it's far from perfect,I created this script as part of continuing my education, as a result I applied several different methodologies in creating it.

I borrowed several lines from g0tmi1ks script though most of the lines are available open source on the net.


Some of the repos are included in the full Kali Distro, I also added additional software in order to fix several known issues with Kali


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

# Start -h



Pending Ideas: 
* Working with counters inside modules
* Fix IRC Bouncer Configuration ( it fails to replace one line)
* Need to Include personalized exploits to exploit DB.
* Add Off the record messaging plug in -otr
* Set key macros for programming.  
* Make script to trap TERM signal.

# Change Log

March 4th 
* Fxed time sync problem by adding another safety layer by changging daemon behavior.
* Added Sublime text as an option for the 32 bits version
* Enabled favorites for gnome dash to dock for 32 bits OS.
* Condition added to check for MingW Libs in order to save time when Installing.
* Condition added to check for Wine in order to save time.
* Condition added to skip installed for Veil-Evasion.

Feb 25th 
* Fixed time sync problem
* Wordked on comment standard 
* Add msf alias for Msfconsole
* Cleaning Module Created.
* Moved Colors definition to Visual Module.
* Added Tilda to express Installation Module.

Feb 22nd 
* Copied Windows-binaries to FTP, TFTP, and Apache services folder.

Feb 20th 
* Fixed Little Issue with Irc peventsfile.

Feb 19th 2017
* Fixed problem with  gsettings and Dash to Dock
* Fixed linked for pshtoolkit
* Added Bookmarks for nautilus
* Added Wallpapers
* Random Wallpapers for Gnome enabled

Feb 1st 2017
* Fixed Commenting format in Start File.
* Fixed Several minor issues.
