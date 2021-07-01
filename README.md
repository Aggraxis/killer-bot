# killer-bot
Discord Bot for serving up assassination contracts from a CSV file. You can probably edit it to serve up just about any kind of responses based on CSV input.... like a lunch bot or something. Use your imagination and be creative. This project has been updated to respond to a discord.py slash command. It's a lot cleaner than it used to be.

Put killer-bot.py, .env (rename dotenv.example), and targets.csv (tailor for how many lists you use, not included) in a folder and go nuts.

pip requirements.txt included for your convenience.

I have also included a sample systemd service file that I used to run the script automatically on reboot. Just edit the paths, user, and enable/start the service.

