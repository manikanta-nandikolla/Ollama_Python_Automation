from ollama_client import ask_ollama

def analyze_meeting(notes):
    
    prompt = f"""
    You are an AI meeting assistant.

    Analyze the meeting notes and extract:

    Summary:
    Action Items:
    Important Decisions:

    Meeting notes:
    {notes}
    """
    
    return ask_ollama(prompt)