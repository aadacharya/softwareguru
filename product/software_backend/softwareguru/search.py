import google.generativeai as genai
import json
import re

gemini_api = "AIzaSyAOkfM18620EIDaa2bsUZSvoMuAmk_J6zg"  # mine

genai.configure(api_key=gemini_api)
model = genai.GenerativeModel("gemini-pro")


# - *


def get_categories_from_prompt(user_prompt):
    try:
        prompt = f""" This is a prompt from my user: "{user_prompt}", please give me exactly 5 categories related to the tools that the user is looking for.\n 
        1. Each categories need to be of two words.
        2. Give me output in json string. The key should be "categories" and the value should be a list of categories. 
        3. Exclude extra characers like /n * - ** " '
        """
        # 2. Output example: a, b, c i.e. separated by commas.

        response = model.generate_content(prompt)

        response_text = json.loads(response.text)
        print("response_text", response_text)

        # categories = response_text["categories"]

        return response_text

        # assuming we get the categories

        try:
            # response_text = response_text.replace("\n", ",")
            # categories_list = response_text.split(",")

            # # Use a regular expression to remove leading numbers, dashes, asterisks, and surrounding whitespace
            # categories_list = [
            #     re.sub(r"^\s*[\d\w\-\*\.]+\s*", "", category).strip()
            #     for category in categories_list
            # ]

            # categories_list_filtered = [
            #     category for category in categories_list if category
            # ]

            return categories_list_filtered
        except:
            # return response_text
            return []

    except:
        return []
