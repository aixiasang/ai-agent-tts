from openai import OpenAI

# Function to call LLM for text enhancement or processing
def call_llm(prompt):    
    # Replace with your API key or use environment variables
    client = OpenAI(api_key="YOUR_API_KEY_HERE")
    
    r = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}]
    )
    
    return r.choices[0].message.content
    
if __name__ == "__main__":
    prompt = "Enhance this text for dramatic reading: Hello world."
    print(call_llm(prompt))