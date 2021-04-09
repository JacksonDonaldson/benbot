run "firsttimesetup.cmd"
creates a file used by the rest of the program to store your login info
then, run "run.cmd" whenever you want to start the bot
I suggest adding run.cmd to startup
(open task scheduler, create basic task, give it a name, have it run every time the computer starts, start a program, browse and select "run.cmd.")
If you encounter errors with it not starting on boot, set it to retry after a minute
