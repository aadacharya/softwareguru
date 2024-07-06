import google.generativeai as genai
import json
import re


gemini_api = "AIzaSyAOkfM18620EIDaa2bsUZSvoMuAmk_J6zg"  # mine

genai.configure(api_key=gemini_api)
model = genai.GenerativeModel("gemini-pro")


def get_categories_from_prompt(user_prompt, max_retries=3):
    def fetch_categories(prompt, attempts):
        if attempts == 0:
            return {"categories": ["AI"]}  # Fallback response

        try:
            prompt_text = f"""This is a prompt from my user: "{user_prompt}", please give me exactly 5 categories related to the tools that the user is looking for.\n 
            1. Each categories need to be of two words.
            2. Give me output in json string. The key should be "categories" and the value should be a list of categories. 
            3. Exclude extra characters like /n * - ** " '
            """
            response = model.generate_content(prompt_text)
            response_text = json.loads(response.text)

            # Check if response has the correct format
            if (
                "categories" in response_text
                and isinstance(response_text["categories"], list)
                and all(isinstance(item, str) for item in response_text["categories"])
            ):
                return response_text
            else:
                return fetch_categories(prompt, attempts - 1)  # Retry

        except Exception as e:
            return fetch_categories(prompt, attempts - 1)  # Retry on error

    return fetch_categories(user_prompt, max_retries)
