import os
from dotenv import load_dotenv
from openai import OpenAI

# Load .env file
load_dotenv()

# Get API key from environment
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise Exception("OPENAI_API_KEY not found in .env file!")

# Initialize OpenAI client
client = OpenAI(api_key=api_key)

# Read task from file
def read_task(filepath):
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"File not found: {filepath}")
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()

# Make a call to OpenAI with prompt to summarize the task
def summarize_task(task):
    prompt = f"""
    Summarize the following task clearly and concisely in 2-3 bullet points:

    {task}
    """

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",  # use gpt-4 only if you have access
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    task_text = read_task("task.txt")
    summary = summarize_task(task_text)

    print("\n Task Summary: \n")
    print("_" * 30)
    print(summary)
