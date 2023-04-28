import openai
import os
from pathlib import Path

openai.api_key = "your_openai_api_key"

def split_text(text, max_length):
    sections = []
    start = 0
    while start < len(text):
        end = min(start + max_length, len(text))
        sections.append(text[start:end])
        start = end
    return sections

def create_response_directory_structure(original_path, response_root):
    response_path = response_root / original_path.relative_to(root_directory)
    response_path.mkdir(parents=True, exist_ok=True)
    return response_path


def process_file(filepath, response_root):
    responses = []
    with open(filepath, 'r') as file:
        content = file.read()
        sections = split_text(content, 2048)  # assuming max_length is 2048
        for section in sections:
            response = openai.Completion.create(
                engine="text-davinci-002",
                prompt=section,
                max_tokens=150,
                n=1,
                stop=None,
                temperature=0.5,
            )
            responses.append(response.choices[0].text.strip())

    response_directory = create_response_directory_structure(filepath, response_root)
    response_file = response_directory / (filepath.name + "_chatgpt_response.txt")
    with open(response_file, 'w') as f:
        for response in responses:
            f.write(response)
            f.write("\n\n")

def traverse_codebase(directory, response_root):
    for entry in os.scandir(directory):
        if entry.is_file() and entry.name.endswith('.swift'):
            process_file(entry.path, response_root)
        elif entry.is_dir():
            traverse_codebase(entry.path, response_root)

if __name__ == '__main__':
    root_directory = Path("path/to/your/swift/codebase")
    chatgpt_response_directory = Path("path/to/chagpt/response")

    traverse_codebase(root_directory, chatgpt_response_directory)
