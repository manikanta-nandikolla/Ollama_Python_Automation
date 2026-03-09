from ollama_client import ask_ollama

def summarize_email(email_text):
    prompt = f"""
    Summarize the following email in 3 bullet points:
    
    {email_text}
    """
    
    return ask_ollama(prompt)

def extract_tasks(email_text):
    prompt = f"""
    You are an assistant that analyzes emails.

    Summarize the following email in 3 short bullet points:

    Email:
    {email_text}
    """

    return ask_ollama(prompt)