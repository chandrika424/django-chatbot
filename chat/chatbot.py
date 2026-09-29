def get_bot_response(message):
    message = message.lower().strip()

    if message in ["hi", "hello", "hey"]:
        return "Hello! 👋 How can I help you today?"

    elif "what is python" in message:
        return "Python is a high-level programming language used for web development, automation, AI, and data science."

    elif "django" in message:
        return "Django is a Python web framework used to build secure and scalable web applications."

    elif "sql" in message:
        return "SQL is used to store, retrieve, update, and manage data in relational databases."

    elif "rest api" in message:
        return "A REST API allows applications to communicate using HTTP methods such as GET, POST, PUT, PATCH, and DELETE."

    elif "pytest" in message:
        return "Pytest is a Python testing framework used to write and execute automated tests."

    elif "your name" in message:
        return "My name is PyBot. I am your Python and Django assistant."

    elif message in ["bye", "goodbye", "exit", "quit"]:
        return "Goodbye! 👋 Have a great day."

    else:
        return "I don't have an answer for that yet. Try asking about Python, Django, SQL, REST API, or Pytest."