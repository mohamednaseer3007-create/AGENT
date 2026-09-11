Code structure :

                | APP (backend)
                    |__init__.py
                    |gmail 
                      |gmail_gen.py
                      |gmail_write.py
                      |__init__.py
                    |youtube
                      |__init__.py
                      |player.py
                    |templates (frontend)
                      | index.html
                    | requirements.txt (packages)
                    | README.md
                    |wsgi.py
Config the app :

Build Command : pip install -r requirements.txt
start command : gunicorn app:app
env variables : GEMINI_KEY, CLIENT_EMAIL
# Nova AI Agent

A multi-functional AI agent built with Flask that combines email generation and YouTube music capabilities. Nova AI Agent processes voice commands to generate professional emails using Google's Gemini API and create YouTube music URLs.

## Features

- Gmail AI Agent
  - Converts voice commands into professional emails
  - Powered by Google Gemini API for intelligent email composition
  - Automatically generates email subjects and bodies
  - Provides direct Gmail compose URLs for quick access
  - Validates email commands and extracts recipient information

- YouTube Music Player
  - Converts song queries into YouTube video URLs
  - Simple voice command interface for music playback
  - Quick access to search results

## Project Structure


