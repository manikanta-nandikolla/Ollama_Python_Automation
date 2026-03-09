from meeting_ai import analyze_meeting
from notifier import send_notification


def check_meeting():

    meeting_notes = """
    Discussed AI automation assistant project.
    Backend will use FastAPI.
    Frontend will use React.
    Deadline next Monday.
    """

    result = analyze_meeting(meeting_notes)

    send_notification(
        "🧠 Meeting Analysis",
        result[:200]
    )