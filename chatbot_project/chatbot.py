def get_bot_response(message):

    message = message.lower().strip()

    if "hello" in message or "hi" in message:
        return "Hello! How can I help you?"

    elif "python" in message:
        return (
            "Python is a high-level programming language used "
            "for web development, automation, AI, and data science."
        )

    elif "django" in message:
        return (
            "Django is a Python web framework used to build "
            "secure and scalable web applications."
        )

    elif "sql" in message:
        return (
            "SQL is used to store, retrieve, and manage data "
            "in relational databases."
        )

    elif "your name" in message:
        return "I am PyBot, your customer support assistant."

    elif "bye" in message:
        return "Goodbye! Have a great day."

    else:
        return (
            "Sorry, I don't have an answer for that question. "
            "Please try asking about Python, Django, or SQL."
        )