---

# GUBot WhatsApp Assistant

GUBot is an automated chatbot designed to interact with users on WhatsApp Web. It scans incoming messages, identifies keywords, and responds with predefined answers. 

## Project Files:

1. **Answers.txt**: This contains a list of possible answers that GUBot can send to the user. Each answer is associated with a number for easy referencing.
2. **KeywordAlgorithm.py**: An older version of the keyword scanning and response mechanism.
3. **Keywords.txt**: This contains a list of keywords that GUBot can recognize. Each set of keywords is associated with a number that corresponds to an answer in `Answers.txt`.
4. **main.py**: The main script where GUBot operates. It integrates with the web version of WhatsApp and automates the process of reading and responding to messages.

## How it Works:

1. The bot scans the latest incoming message on WhatsApp Web.
2. If the message is of type text, the bot searches for any of the predefined keywords in the message.
3. Once a keyword is identified, the bot maps it to the appropriate response from `Answers.txt`.
4. The bot sends the corresponding response back to the user.

## Prerequisites:

- Python
- Selenium
- ChromeDriverManager
- Chrome Browser

## Setup:

1. Ensure you have the required libraries installed:
```bash
pip install selenium webdriver_manager
```

2. Create a `Keywords.txt` and `Answers.txt` file in the root directory.
3. Make sure you have Chrome browser installed.
4. Run the `main.py` script.

## Using the Bot:

1. After running the `main.py`, it will open a browser window for WhatsApp Web. 
2. Scan the QR code using the WhatsApp mobile application to log in.
3. The bot will automatically detect new chats that have a new message and reply based on the keyword.

**Note**: Ensure that the browser session doesn't timeout or face disconnection issues for continuous operation of the bot.

## Potential Improvements:

- Error handling can be enhanced for better bot recovery.
- Implementing more AI-based functionalities can make the bot smarter.
- Usage of a database instead of text files for scalable keyword-answer relationships.

## Known Issues:

1. If the incoming message isn't of type text, the bot will inform the user to send only text messages.
2. The bot may face issues if there are rapid consecutive messages as it needs time to process each message.

