# Step 1: Create your prompts

system_prompt = "You are a roleplaying games coach. Always be very short and concise in your replies. Use contents from:"
user_prompt = """
    I want to play an evil character, who is not actually a bad person. is that possible? i would want them to be a ranger. Any ideas?
"""

# Step 2: Make the messages list

messages = [
    {"role": "system", "content": system_prompt + web_content},
    {"role": "user", "content": user_prompt}
] 

# openai.chat.completions.create(model="gpt-5-nano", messages=messages)
# Step 3: Call OpenAI
response = openai.chat.completions.create(
    model="gpt-5-nano",
    messages=messages
)

# return response.choices[0].message.content
# Step 4: print the result
print(response.choices[0].message.content)