import json
import os
from .prompts import task3_gpt_assistant_prompt, task3_gpt_user_prompt
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def implement_feedback(text, target, instruction):
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": task3_gpt_assistant_prompt},
            {"role": "user", "content": task3_gpt_user_prompt.format(text, target, instruction)}
        ],
        response_format={"type": "json_object"},
        n=1,
        temperature=0.01
    )
    return json.loads(response.choices[0].message.content)

