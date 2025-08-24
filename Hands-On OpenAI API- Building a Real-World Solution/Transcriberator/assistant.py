import os
import time
from openai import OpenAI


def display_main_menu():
    print("=================================")
    print("[Assistant]")
    prompt = input("Enter your prompt: ")
    print("=================================")
    handle_prompt(prompt)

def handle_prompt(prompt):
    if prompt == "exit" or prompt == "quit":
        print("Exiting...")
        exit(0)

    client.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content=prompt
    )

    run = client.beta.threads.runs.create(
        thread_id=thread.id,
        assistant_id=assistant.id
    )

    still_running = True
    while still_running:
        latest_run = client.beta.threads.runs.retrieve(
            thread_id=thread.id,
            run_id=run.id
        )
        still_running = latest_run.status != "completed"
        if still_running:
            print("Run status:", run.status)
            time.sleep(2)
        
    messages = client.beta.threads.messages.list(
        thread_id=thread.id
    )
    print(messages.data[0].content)


if __name__ == '__main__':
    key = os.getenv("OPENAI_API_KEY")
    client = OpenAI(api_key=key)

    assistant = client.beta.assistants.create(
        name="Test Assistant",
        description="This is a test assistant.",
        instructions="You are a helpful assistant that responds in a structured json format.",
        model="gpt-3.5-turbo-1106",
        tools=[{"type": "code_interpreter"}],
        response_format={"type": "json_object"}
    )

    thread = client.beta.threads.create()

    while True:
        display_main_menu()