# Sauce-Bot
Bot that hides nhentai's "magic numbers" as rgb valures in images. It can later retrieve them and open the hentai in your default browser.<br />
See [changelog](changelog.md) to find what's new in each version.

=========================[ USAGE - IMAGE CREATION ]=========================
 * open the tool
 * copy the numbers from nhentai link (https​://nhentai.​net/g/*NUMBERS*) for some doujin to textbox titled "Sauce" 
 * tick include hex option if you want the resulting image to include hex of it's colour
 * tick custom message to include text in the resulting image
 * write the text you want to appear on the image inside of the textbox titled "Message"
 * click the create button
 * upon being promptped choose the folder where you want to save the image, image format and name

==========================[ USAGE - OPENING IMAGE ]=========================
 * cliclk the open button
 * choose the image you want to open
 
================================[ COMPILING ]===============================
 * make sure you have all the nessesary python modules installed
 * make sure you have pyinstaller installed
 * open the python file and uncomment lines as instructed
 * ! windows !
 * run the compile.ps1 script in powershell
 * ! other platforms !
 * navigate to folder with this script in shell
 * run the pyinstaller with these parameters --onefile --icon=n.ico --splash=n-1.3.png --window "Sauce Bot 1.0.3.py"
 * copy config and ico files to the distination with compiled script
 * create folder named Sauce if you haven't specified different one in config 

===============================[ INSTALATION ]==============================
 * ! windows only !
 * download the zip file from [releases section](https://github.com/SwaggyBookshelf/Sauce-Bot/releases/) of this project
 * unzip the archive to your desired destination
 * kinda ignore the trojan warnings, windows just does that with python executables
 * to stay safe I reccomend compiling the code for yourself or using the python script as is
 * open the Sauce Bot executable to use it
 * check preferences.config to configure your preferences
