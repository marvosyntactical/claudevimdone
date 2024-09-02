import vim
import os
import anthropic
from anthropic import Anthropic

anthropic_api_key = os.getenv("ANTHROPIC_API_KEY")

curr_dir = f"{__file__[:len(__file__)-__file__[::-1].find('/')]}"

# print("Claude Vim Done v0.1 loaded.")

if anthropic_api_key is None:
    anthropic_filename = curr_dir+ ".anthropic_api_key"
    try:
        with open(anthropic_filename, "r") as api_file:
            anthropic_api_key = api_file.read()[:-1]
    except FileNotFoundError as FNFE:
        print(f"Anthropic Key must be provided at ")
        raise FNFE


client = Anthropic(api_key=anthropic_api_key)

def get_completion(prompt):
    try:
        response = client.messages.create(
            model="claude-3-5-sonnet-20240620",
            max_tokens=2048,
            system="Here you help me with code completion in my personal little vim plugin, written mostly by you. Provide concise, relevant completions.",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
    except anthropic.InternalServerError as ISE:
        return "<Anthropic Server Overloaded, try again later>"
    return response.content[0].text


def generate_completion():
    global last_completion_info

    file_name = vim.eval("expand('%:t')")

    buffer = vim.current.buffer
    start_row, start_col = vim.current.window.cursor

    # Get file content and insert cursor indicator
    file_content = []
    for i, line in enumerate(buffer):
        if i + 1 == start_row:
            file_content.append(line[:start_col] + "█" + line[start_col:])
        else:
            file_content.append(line)
    file_content = "\n".join(file_content)

    prompt = f"""
    Here's the content of the file {file_name} (█ indicates the cursor position):

    {file_content}

    Please provide a completion starting from the cursor position (█).

    If e.g. there's a comment just before the cursor describing what I want (maybe something completely different than a code completion), take that into account!
    Use all relevant context, be smart.

    IMPORTANT:
    Your completion is inserted DIRECTLY AT THE CURSOR POSITION FROM THE FIRST TOKEN YOU PRODUCE ONWARDS!
    That means you should IMMEDIATELY BEGIN WITH THE CODE CONTINUATION, and NEVER preface it with something like "Here's a completion for your fibonacci function:" or anything like that. Everything you output is DIRECTLY inserted into the code from the cursor position onward, so do not use triple backticks for code and talk normally around it, but just directly output code and put comments as comments in the relevant language (.e.g # if you're presented with python code, // if you're presented with C++ code)
    """

    completion = get_completion(prompt)
    completion_lines = completion.split('\n')

    # Store original content for undo
    original_lines = buffer[start_row-1:]
    last_completion_info = {
        'start_row': start_row,
        'start_col': start_col,
        'original_lines': original_lines,
        'completion_lines': completion_lines
    }

    # Apply completion
    for i, line in enumerate(completion_lines):
        if i == 0:
            buffer[start_row-1] = buffer[start_row-1][:start_col] + line
        else:
            if start_row + i - 1 < len(buffer):
                buffer[start_row + i - 1] = line
            else:
                buffer.append(line)

def undo_completion():
    global last_completion_info

    if last_completion_info is None:
        print("No completion to undo.")
        return

    buffer = vim.current.buffer
    start_row = last_completion_info['start_row']
    start_col = last_completion_info['start_col']
    original_lines = last_completion_info['original_lines']

    # Restore original content
    buffer[start_row-1:] = original_lines

    # Reset cursor position
    vim.current.window.cursor = (start_row, start_col)

    # Clear the last_completion_info
    last_completion_info = None

    print("Completion undone.")


