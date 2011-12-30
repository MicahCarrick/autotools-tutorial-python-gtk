SUBDIRS = icons

desktopdir = $(datadir)/applications
desktop_DATA = hello-world.desktop

DESKTOP_UPDATE = update-desktop-database $(datadir)/applications || :

install-data-hook: 
	$(DESKTOP_UPDATE)
uninstall-hook: 
	$(DESKTOP_UPDATE)
	
