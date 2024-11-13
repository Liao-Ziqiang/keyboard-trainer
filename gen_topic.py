import os
from openai import OpenAI
import random

# Create a client instance
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

# Define system message content
system_content = (
    "你是一个专栏作家，请你根据这个话题写一个200~300词左右的英文文本，"
    "对这个话题进行详细地讨论，仅连续的一段话，不要分段，使用英文，"
    "不要标题，不要返回任何和正文无关的其他多余内容。"
)

# Read the topics from the file
with open('./topic.txt', 'r', encoding='utf-8') as file:
    topics = file.readlines()
    random.shuffle(topics)

# Open the output file
with open('output.txt', 'w', encoding='utf-8') as output_file:
    # Iterate over each topic
    for index, topic in enumerate(topics):
        topic = topic.strip()  # Remove any leading/trailing whitespace

        # Create a chat completion
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": topic,
                }, 
                {
                    "role": "system",
                    "content": system_content,
                }
            ],
            model="gpt-4o-mini",
        )

        # Write the response to the output file with a newline
        output_file.write(chat_completion.choices[0].message.content + '\n')

        # Print progress
        print(f"Processed topic {index + 1}/{len(topics)}")