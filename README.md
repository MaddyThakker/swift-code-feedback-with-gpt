# swift-code-feedback-with-gpt
Just a quick experiment to get feedback of my entire swift codebase with GPT.

This project integrates the ChatGPT API with a Swift codebase to provide feedback on the quality of the code. The API is used to generate responses based on the contents of each code file, which are saved in a file structure mirroring the original codebase. This allows for easy analysis of the feedback on a per-file basis.

Just run `pip3 install openai` and you should be all set.

Change these 3 things ——
1. openai.api_key = "your_openai_api_key"
2. root_directory = Path("path/to/your/swift/codebase")
3. chatgpt_response_directory = Path("path/to/chagpt/response")
