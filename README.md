# Discord-PyPresence
This project allows you to create custom Discord Rich Presence activities using your own Discord Developer Applications and PyPresence, without needing bot permissions or OAuth scopes.


🚀 Discord Custom Activity System
PyPresence + Discord Developers

By Korman · CyberShellGame · Green Hair Media

This project allows you to create custom Discord Rich Presence activities using your own Discord Developer Applications and PyPresence, without needing bot permissions or OAuth scopes.

Your activities appear in Discord exactly like real games or apps:

“Jakiando con JakiKaliOS”
“Minion Control Panel CLI”
“Escuchando LoFi y haciendo Tareas”
“Play The Game Right Now!!!”

This system is used to display system states, projects, servers, or creative activities inside your Discord profile.

🧠 How it works

Discord allows Developer Applications to publish Rich Presence activities.

We create Discord Developer Apps that:

Have no permissions

Have no bot

Have no OAuth scopes

Only contain:

App name

App icon (logo)

Rich Presence enabled

These apps act as Activity IDs.

Your Python script connects locally to:

Discord Desktop App → Local IPC → Discord Servers → Your Profile


Web Discord does NOT work because Rich Presence requires the Desktop IPC socket.

⚙️ Requirements
Requirement	Status
Discord Desktop (Linux / Windows / Mac)	✅ REQUIRED
Discord logged into your account	✅ REQUIRED
"Display current activity" enabled	✅ REQUIRED
Python 3.8+	✅
PyPresence	✅
🔧 Installation

Install PyPresence:

pip install pypresence


Make sure Discord Desktop is running and logged in.

🔐 Discord Settings

Open Discord → Settings → Activity Privacy

Enable:

Display current activity as a status message

Otherwise nothing will show.

🧩 How Discord Apps are used

Each activity uses its own Discord Application created at:

https://discord.com/developers/applications

Each app contains:

Name (example: JakiKaliOS, Minions, Steam, LoFi)

Icon (shown in Rich Presence)

Rich Presence enabled

The only thing used from each App is:

CLIENT_ID

📡 Data Flow
Python Script
     ↓
Discord Desktop IPC
     ↓
Discord Local Client
     ↓
Discord Servers
     ↓
Your Discord Profile


Nothing is public, nothing is logged externally, no bots involved.

📂 Included Activities

All activities are free to use and included as standalone scripts.

🟦 JakiKaliOS Activity

cybershellgame.discord

Shows:

Jakiando con JakiKaliOS
https://cybershellgame.net

🟨 Debian 13 Activity

debian-discord

Shows:

Configurando Sistemas y Redes
Con Debian 13 Trixie Stable

🟥 La Rubia Mode

larubia-discord

Shows:

Dandole Duro a la Rubia
Con mi Poyuco a SuXumino

🟪 LoFi Mode

lofi-discord

Shows:

Esa chica tranquila escribiendo…
Escuchando LoFi y haciendo tareas

🟩 Minions Control

minions-discord

Shows:

Minion Control Panel CLI
Levantando Minions en Red

🟦 Steam / Game Portal

steam-discord

Shows:

Play The Game Right Now!!!
Delante del Portal de la Vida Virtual

▶️ Running an activity
python3 jaki-discord.py


(or any of the provided scripts)

It will instantly show on Discord.

To stop:

Ctrl + C

🧠 Why this is powerful

This allows you to:

Show what you are building

Promote your projects

Display system status

Brand your Discord profile

Create immersive cyberpunk / hacker / dev presence

With zero API tokens, zero bots, zero permissions.

🛡️ Security

This system:

Does NOT access Discord tokens

Does NOT use bots

Does NOT read messages

Does NOT require OAuth

It only publishes activity via local IPC.

📜 License

All scripts are released as free-use open-source.
Use, modify, remix, and extend them.

🧬 Made for

CyberShellGame
Green Hair Media
JakiKaliOS
Minions Network
MetaKor Universe
