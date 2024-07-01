import google.generativeai as genai
import json
import re



gemini_api = "AIzaSyAOkfM18620EIDaa2bsUZSvoMuAmk_J6zg"  # mine

genai.configure(api_key=gemini_api)
model = genai.GenerativeModel("gemini-pro")

def get_categories_from_prompt(user_prompt):
    try:
        prompt = f""" This is a prompt from my user: "{user_prompt}", please give me exactly 5 categories related to the tools that the user is looking for.\n 
        1. Each categories need to be of two words.
        2. Give me output in json string. The key should be "categories" and the value should be a list of categories. 
        3. Exclude extra characers like /n * - ** " '
        """

        response = model.generate_content(prompt)
        response_text = json.loads(response.text)
        return response_text
    except:
        return [{"categoires":["AI"]}]

# import redis

# r = redis.Redis(
#     host="redis-10023.c301.ap-south-1-1.ec2.redns.redis-cloud.com:10023",
#     port=10023,
#     password="BGE5tfCDbDjt2FjXC7KTrAsLGoupBqLq",
# )

# def cache_search_data(
#     search_id, data, ttl=43200
# ):  # cache gets stored for 12 hours in this ttl
#     """
#     Cache search data by search_id with a TTL (Time To Live).

#     Args:
#     - search_id (str): The unique identifier for the search.
#     - data (dict): The search data to cache.
#     - ttl (int): Time to live in seconds. Default is 12 hours (43200 seconds).

#     Returns:
#     - bool: True if the operation was successful, False otherwise.
#     """
#     try:
#         # Convert the data to a JSON string
#         json_data = json.dumps(data)
#         # Store the data in Redis with the search_id as the key and set TTL
#         r.setex(search_id, ttl, json_data)
#         return True
#     except Exception as e:
#         print(f"Error caching search data: {e}")
#         return False


# def get_cached_search_data(search_id):
#     """
#     Get cached search data by search_id.

#     Args:
#     - search_id (str): The unique identifier for the search.

#     Returns:
#     - dict: The cached search data, or None if not found or an error occurs.
#     """
#     try:
#         # Retrieve the data from Redis
#         json_data = r.get(search_id)
#         if json_data is None:
#             return None
#         # Convert the JSON string back to a dictionary
#         data = json.loads(json_data)
#         return data
#     except Exception as e:
#         print(f"Error retrieving cached search data: {e}")
#         return None


# # Example usage:
# search_id = "example_search_id"
# search_data = {"query": "example query", "results": ["result1", "result2"]}

# # Cache the search data
# if cache_search_data(search_id, search_data):
#     print("Search data cached successfully.")

# # Retrieve the cached search data
# cached_data = get_cached_search_data(search_id)
# if cached_data:
#     print("Cached search data retrieved:", cached_data)
# else:
#     print("No cached data found for this search_id.")
