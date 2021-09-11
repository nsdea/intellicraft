# IntelliCraft
Python AI Plays Minecraft!

# Installation
## Dependencies
Install dependencies using `pip install -r requirements.txt` in the root dir of this project (right here). You should also install:
- `pip install opencv-python`

## Server

1. Set up a Minecraft server (version **1.9 or higher**, can be vanilla or modified server!)
2. Edit your `server.properties` file to the following settings:
   ```
   enable-rcon=true
   rcon.password=your_rcon_password_here
   rcon.port=your_rcon_port_default_is_25575_here
   broadcast-rcon-to-ops=false
   ```

3. You're done! Start your Minecraft server and Twitch livestream and enjoy the pain.

## Linux
On Linux, you have to run pretty much everything using **sudo** (`sudo <command_here>`)!
You need to run:
- `sudo apt-get install scrot`
  
## Minecraft
You need to join the server with the IP "localhost" if you set up one.

### Controls
For the mouse controls to work, you need to do the following:
- Options...
- Controls...
- Mouse Settings...
- Raw input: **OFF**

Huge thanks to https://stackoverflow.com/a/58043888 for information on that!