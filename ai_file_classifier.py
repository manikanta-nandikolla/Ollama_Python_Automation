from ollama_client import ask_ollama

def classify_file(file_name):
    
    prompt = """
    You are a file organizer assistant.
    
    Categorize the following file into one of these folders:
    Work, Finance, Personal, Media, Other
    
    File name:{file_name}
    
    Return only the folder name
    """
    
    category = ask_ollama(prompt)
    
    return category.strip()