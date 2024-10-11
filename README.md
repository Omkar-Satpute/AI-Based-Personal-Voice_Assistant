# AI-Based Personal Assistant

This is a simple AI voice assistant built using Python libraries such as `pyttsx3`, `speech_recognition`, `pywhatkit`, and `requests`. The assistant can perform tasks like playing music, fetching news headlines, managing a task list, and recognizing voice commands.

## Features
- **Play music**: Search for and play music on YouTube using `pywhatkit`.
- **Fetch news**: Get the latest news headlines using the News API.
- **Task management**: Add, view, and delete tasks in a task list.
- **Voice recognition**: Recognize user commands using `speech_recognition`.
- **Text-to-speech**: Speak back responses using `pyttsx3`.

## Installation

### Prerequisites
Make sure you have the following Python libraries installed:

```bash
pip install pyttsx3
pip install SpeechRecognition
pip install pywhatkit
pip install requests
```

### Additional Dependencies
- You may need to install additional audio dependencies for `SpeechRecognition`, depending on your platform.
  - For Linux: `sudo apt-get install portaudio19-dev python3-pyaudio`
  - For MacOS: `brew install portaudio`
  
### API Key for News
You will need an API key for the [News API](https://newsapi.org/). Replace the `NEWS_API_KEY` variable in the code with your own API key.

```python
NEWS_API_KEY = "your_api_key_here"
```

## Usage

1. **Clone the repository or download the code**.
2. **Run the script** using Python:

```bash
python Assistant.py
```

3. The assistant will greet you and start listening for commands.

## Voice Commands

You can control the assistant using voice commands. Here are some example commands:
- **Play Music**: 
  - Say "Play [song name]" or "Music [song name]" to play music on YouTube.
  
- **Get News**: 
  - Say "Get news" or "What's the news?" to hear the latest news headlines.

- **Manage Tasks**:
  - Say "Add task [task name]" to add a task to your list.
  - Say "View tasks" to hear the current tasks in your list.
  - Say "Delete task [task number]" to remove a task from your list.

- **Exit**:
  - Say "Exit" or "Stop" to quit the assistant.

## Example Commands
- "Play Shape of You"
- "Get news"
- "Add task Finish the report"
- "View tasks"
- "Delete task 1"
- "Exit"

## Notes
- Ensure you have an active internet connection to fetch news or play music.
- For optimal voice recognition, speak clearly and use the microphone in a quiet environment.

## License
This project is licensed under the MIT License.

--- 

This `README.md` will help guide users to install, configure, and use the voice assistant effectively.
