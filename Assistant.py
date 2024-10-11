import pyttsx3
import speech_recognition as sr
import pywhatkit as kit
import requests

# Initialize the pyttsx3 engine for text-to-speech
engine = pyttsx3.init()

#API Key for news fetching
NEWS_API_KEY = "f8d670fdc71f46d49dbc5b24167f17fc"

# Initialize an empty task list
task_list = []

# Function to speak text using pyttsx3
def speak(text, speed=200):
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', speed)
    engine.setProperty('volume', 0.8)
    engine.say(text)
    engine.runAndWait()

# Function to listen for voice commands
def take_command(timeout_duration=3, pause_duration=1.0):
    recognizer = sr.Recognizer()
    recognizer.pause_threshold = pause_duration

    with sr.Microphone() as source:
        print("Listening...")
        try:
            audio = recognizer.listen(source, timeout=timeout_duration)
        except sr.WaitTimeoutError:
            print("No speech detected, timing out.")
            return "None"

        try:
            print("Recognizing...")
            query = recognizer.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand that.")
            return "None"
        except sr.RequestError:
            print("Request failed, please check your internet connection.")
            return "None"

        return query

# Function to fetch news headlines using the News API
def get_news():
    try:
        url = f"http://newsapi.org/v2/top-headlines?country=us&apiKey={NEWS_API_KEY}"
        response = requests.get(url)
        news_data = response.json()
        
        headlines = []
        for article in news_data['articles'][:5]:
            headlines.append(article['title'])
        
        return headlines
    except Exception as e:
        print(f"Error fetching news: {e}")
        return ["Sorry, I couldn't fetch the news."]

# Function to play music on YouTube
def play_youtube_music(search_query):
    try:
        kit.playonyt(search_query)
        speak(f"Playing {search_query} on YouTube.")
    except Exception as e:
        print(f"Error playing music: {e}")
        speak("Sorry, I couldn't play the music.")

# Function to add a task
def add_task(task):
    task_list.append(task)
    speak(f"Task '{task}' has been added to your task list.")

# Function to view tasks
def view_tasks():
    if task_list:
        speak("Here are your tasks:")
        for idx, task in enumerate(task_list, 1):
            speak(f"Task {idx}: {task}")
    else:
        speak("Your task list is empty.")

# Function to delete a task
def delete_task(task_number):
    try:
        task_index = int(task_number) - 1
        if 0 <= task_index < len(task_list):
            removed_task = task_list.pop(task_index)
            speak(f"Task '{removed_task}' has been removed from your task list.")
        else:
            speak("Invalid task number. Please try again.")
    except ValueError:
        speak("Please provide a valid task number.")

# Main function to run the AI assistant
def jarvis():
    speak("Hello. How can I assist you today?", speed=200)

    while True:
        query = take_command().lower()

        if 'play' in query or 'music' in query:
            song_name = query.replace('play', '').replace('music', '').strip()
            if song_name:
                play_youtube_music(song_name)
            else:
                speak("Please specify the name of the song.")
        
        elif 'news' in query:
            speak("Fetching the latest news headlines.")
            headlines = get_news()
            for idx, headline in enumerate(headlines, 1):
                print(f"News {idx}: {headline}")
                speak(f"News {idx}: {headline}")

        elif 'add task' in query:
            task = query.replace('add task', '').strip()
            if task:
                add_task(task)
            else:
                speak("Please specify the task you want to add.")

        elif 'view tasks' in query:
            view_tasks()

        elif 'delete task' in query:
            task_number = query.replace('delete task', '').strip()
            if task_number:
                delete_task(task_number)
            else:
                speak("Please specify the task number you want to delete.")

        elif 'exit' in query or 'stop' in query:
            speak("Goodbye!")
            break

        else:
            speak("I'm sorry, I didn't understand that. Can you please repeat?")

# Example usage: Start the assistant
if __name__ == "__main__":
    jarvis()