#Prompt Evaluator
A command-line tool that sends prompts to the OpenAI API, displays the response, collects a quality score, and saves all results to a JSON file for future reference.
Why I built it
As an AI Engineer, I needed a simple way to track prompt performance over time. This tool allows me to test prompts, score the responses, and build a structured evaluation history — which is essential for A/B testing and prompt optimization workflows.

#Technologies

Python 3
OpenAI API
python-dotenv

#How to run

Clone the repository
Create a .env file with your OPENAI_API_KEY
Install dependencies: pip install openai python-dotenv
Run: python prompt_evaluator.py
