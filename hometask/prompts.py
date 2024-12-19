task2_gpt_assistant_prompt = """ You are a helpful assistant designed to output JSON and your purpose is to decide if the given text follows the instructions in the template correctly.
When you need to verify word counts or check text length limitations, please use the provided count_words function.
Do not try to count words manually. Always use the function when word limits need to be checked.
"""
task2_gpt_user_prompt = """I will give you a text and a template and you will decide if it follows the instructions in the template correctly.
Please return the result in the following format, do not include any explanations:
{{
"result": "True" or "False"
"explanation": "explanation of the result"
}}
Utilize your expertise to generate the most pertinent information.
Text: {}
Template: {}
result:
"""

task3_gpt_assistant_prompt = """ You are a helpful assistant designed to output JSON and your purpose is to follow the instructions and add, edit or delete the given text. """
task3_gpt_user_prompt = """I will give you a text and the target part of the text and instructions.
Please return the updated text in the following format, do not include any explanations:
{{
"updated_text": "updated text"
}}
Utilize your expertise to generate the most pertinent information.
Text: {}
Target part of the text: {}
Instructions: {}
updated_text:
"""