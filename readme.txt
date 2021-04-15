1. Create a new google account. Don't use it for anything else.
2. Go to my account-> security-> less secure app access-> on
3. install firefox if it is not already installed on your computer
4. Create a best buy account using that email address. Don't sign in with google, actually create an account
5. Save as much information as you can to that account 
	(1 credit card number, shipping address, ect)
6. Ensure you have verified your email through bestbuy, then delete all emails you have recieved in that account
7. Try not to log in to that google account, or to the bestbuy account
8. run "firstTimeSetup.cmd"
	this creates a file used by the rest of the program to store your login info
9. Every time you want to start the bot, run "run.cmd"
I suggest adding run.cmd to startup
	open task scheduler, 
	create basic task, 
	give it a name, 
	have it run every time the computer starts, 
	start a program, 
	browse and select "run.cmd."
If you encounter errors with the program not starting on boot, set it to retry 
after a minute (it's an option available in task scheduler)

run.cmd runs a python program that essentially refreshes the urls given as often as it
can, looking for a change in the "sold out" button.
Once it detects one, it notifies you and launches a selenium browser that attempts to
purchase the item. I still recommend trying to get to your pc as fast as possible when
you receive the discord notification, as the bot will fail after it gets to checkout in
some circumstances.

Other errors: Contact Jackson
