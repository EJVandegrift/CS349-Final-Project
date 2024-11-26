from openai import OpenAI
import os
from typing import Optional
from api_key import openai_key

def get_gpt4_response(prompt: str, api_key: Optional[str] = None) -> str:
    """
    Get a response from GPT-4 based on the given prompt.
    
    Args:
        prompt (str): The prompt to send to GPT-4
        api_key (str, optional): OpenAI API key. If not provided, will look for OPENAI_API_KEY environment variable
        
    Returns:
        str: The generated response
        
    Raises:
        ValueError: If no API key is provided or found
        Exception: If the API call fails
    """
    # Set up the API key
    if not api_key and not os.getenv("OPENAI_API_KEY"):
        raise ValueError("No API key provided. Either pass it as an argument or set OPENAI_API_KEY environment variable")
    
    # Initialize the client
    client = OpenAI(api_key=api_key or os.getenv("OPENAI_API_KEY"))
    
    try:
        # Create the chat completion
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=1000
        )
        
        # Extract and return the response text
        return response.choices[0].message.content
        
    except Exception as e:
        raise Exception(f"Error getting response from GPT-4: {str(e)}")

# Example usage
if __name__ == "__main__":
    # You can set your API key here or use an environment variable
    API_KEY = openai_key
    
    # Example prompt
    prompt = """You are a database assistant. I need detailed information about a romance movie based on the following attributes. Please return the information in CSV format. If any information is not available, leave the cell as 'NA'. Here's the required format:
            Headers: Lead Actor/Actress 1 Gender (Male/Female), Lead Actor/Actress 2 Gender (Male/Female), Writer's Gender (Male/Female), Director's Gender (Male/Female), Lead Actor 1 Age, Lead Actor 2 Age, Passes Bechdel Test (Yes/No), MPAA Rating

            Notes for specific features:
                - Age difference: Take the absolute value of the lead actors difference (single value). Additionally, for animated movies,
                                  use the age difference of the lead animated characters rather than the voice actors.

            

            Output the information as a single row in CSV format and only enter values if you are certain they are correct.
            
            Do this for the movie "La La Land (2016)"
            """
    
    try:
        response = get_gpt4_response(prompt, API_KEY)
        print("GPT-4 Response:")
        print(response)
    except Exception as e:
        print(f"Error: {str(e)}")