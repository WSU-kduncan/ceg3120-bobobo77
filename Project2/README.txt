How to build a Discord bot with minimal fuss using this script:

You will need: A Discord account, a server you have Admin privileges in, and a browser

Step 1: Go into the Discord Development Portal in your browser. Log in with your credentials  

Step 2: select "New Application" as a button. Give it a name. Now select it from the home page.

Step 3: You will select the OAuth2 to help grant permissions. Select "bot" from the checkbox table below that. Another table will generate and select "Administrator"

Step 4: Copy the URL in the first checkbox table. Open it up in another tab and link it to your server from the drop down.

Step 5: Go to the Bot section of your application and copy the token.

Step 6: Make a .env file for the script int this repo and Write "DISCORD-TOKEN:" and paste the token you copied.

Step 7: Write in the .env file "GUILD-TOKEN:" and paste the server name you wish to connect to.

Step 8: download a python version that's 3.7+. You'll need it to run the bot script.

Step 9: We are going to download 2 libraries for python. discord.py and python-dotenv should be installed with "pip3 install -U" preceding them if you open a shell terminal

Step 10: Run the script with "Python3 bot.py" to get it going.


The command for this bot is "Summon!" 
As of this development, one of the 8 servants from the original Fate/Stay Night series will be printed with both class and name as a reply. 
Perhaps it will be expanded upon with the full system from Fate/Grand Order.



To keep the script running, an idea might be to run it from a paird server space, like AWS, and to have it run there 24/7.
