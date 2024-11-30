import requests

def find_recipes(ingredients):
    # Replace 'your_api_key' with your actual Spoonacular API key
    api_url = 'https://api.spoonacular.com/recipes/findByIngredients'
    params = {
        'ingredients': ','.join(ingredients),
        'apiKey': 'YOUR_ACTUAL_API_KEY',  # You must replace this
        'number': 5
    }
    
    try:
        response = requests.get(api_url, params=params)
        
        # Check if the request was successful
        response.raise_for_status()
        
        # Parse the JSON response
        recipes = response.json()
        
        # Check if recipes list is empty
        if not recipes:
            print("No recipes found with the given ingredients.")
            return []
        
        return recipes
    
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        print(f"Response content: {response.text}")
    except requests.exceptions.RequestException as req_err:
        print(f"Request error occurred: {req_err}")
    except ValueError as json_err:
        print(f"JSON parsing error: {json_err}")
    
    return []

def main():
    # Get ingredients from user
    ingredients_input = input("Enter ingredients you have (comma-separated): ").strip()
    ingredients = [ingredient.strip() for ingredient in ingredients_input.split(',')]
    
    # Find recipes
    recipes = find_recipes(ingredients)
    
    # Print recipes
    if recipes:
        print("\nHere are some recipes you can make:")
        for recipe in recipes:
            try:
                # Use get() method to safely access dictionary keys
                print(f"Title: {recipe.get('title', 'Unknown Title')}")
                print(f"Used Ingredient Count: {recipe.get('usedIngredientCount', 0)}")
                print(f"Missed Ingredient Count: {recipe.get('missedIngredientCount', 0)}")
                print(f"Image: {recipe.get('image', 'No image available')}")
                print("-" * 50)
            except Exception as e:
                print(f"Error processing recipe: {e}")
    else:
        print("No recipes found.")

if __name__ == '__main__':
    main()