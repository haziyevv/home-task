import os
import json
from openai import OpenAI
from .prompts import task2_gpt_assistant_prompt, task2_gpt_user_prompt
from .tools import count_words

# Define all available tools
AVAILABLE_TOOLS = {
    "count_words": {
        "function": count_words,
        "description": "Use this function to check if text meets word limits. Always use this function when word count needs to be verified.",
        "parameters": {
            "type": "object",
            "properties": {
                "text": {
                    "type": "string",
                    "description": "The text to count words in"
                }
            },
            "required": ["text"]
        }
    }
}

def execute_function(function_name, function_args):
    """Execute a function by name with given arguments."""
    if function_name not in AVAILABLE_TOOLS:
        raise ValueError(f"Unknown function: {function_name}")
    
    function = AVAILABLE_TOOLS[function_name]["function"]
    # Parse the function arguments from string if needed
    if isinstance(function_args, str):
        function_args = json.loads(function_args)
    
    return function(**function_args)

def get_llm_response(client, messages, functions):
    """Get response from LLM and handle function calling."""
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=messages,
        functions=functions,
        function_call="auto",
        temperature=0.01,
        max_tokens=300,
        n=1,
        response_format={"type": "json_object"}
    )

    # Handle function calling if needed
    if response.choices[0].message.function_call:
        function_call = response.choices[0].message.function_call
        function_name = function_call.name
        function_args = function_call.arguments

        # Execute the function
        result = execute_function(function_name, function_args)

        # Add the function result to messages and get final response
        messages.extend([
            {"role": "assistant", "content": None, "function_call": function_call},
            {"role": "function", "name": function_name, "content": str(result)}
        ])

        return get_llm_response(client, messages, functions)
    
    return response.choices[0].message.content

def follow_instructions(template, input_text):
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    # Convert tools to OpenAI function format
    functions = [
        {
            "name": name,
            "description": tool["description"],
            "parameters": tool["parameters"]
        }
        for name, tool in AVAILABLE_TOOLS.items()
    ]

    messages = [
        {"role": "system", "content": task2_gpt_assistant_prompt},
        {"role": "user", "content": task2_gpt_user_prompt.format(input_text, template)}
    ]

    result = get_llm_response(client, messages, functions)
    return result