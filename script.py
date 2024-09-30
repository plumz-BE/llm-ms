from flask import Flask, request, jsonify
import openai
import os
import json
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Set your OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")  # Ensure you set this environment variable

@app.route('/author', methods=['POST'])
def get_authors():
    data = request.json
    book_title = data.get("title")
    
    if not book_title:
        return jsonify({"error": "Title is required"}), 400

    # Correct prompt format for ChatCompletion
    prompt = f"Who is the author of '{book_title}'? Provide response in JSON format with key 'author' and names of authors as array of strings. If the author is not found, return ['Anonymous']."

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",  # Correct the parameter to 'model'
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=50,
            n=1,
            stop=None,
            temperature=0
        )

        # Extract the response text from the API
        result = response.choices[0].message['content'].strip()

        try:
            # Try to parse the result as JSON
            author_info = json.loads(result)
            
            if 'author' in author_info and isinstance(author_info['author'], list) and author_info['author']:
                return jsonify(author_info)
            else:
                return jsonify({"author": ["Anonymous"]})
        except json.JSONDecodeError:
            return jsonify({"author": ["Anonymous"]})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/cover', methods=['POST'])
def get_cover_url():
    data = request.json
    book_title = data.get("title")
    
    if not book_title:
        return jsonify({"error": "Title is required"}), 400

    # Correct prompt format for ChatCompletion
    prompt = f"Give me url to get cover page  of '{book_title}'? Provide response in JSON format with key 'cover_image_url'. If the image url is not found, return 'https://res.cloudinary.com/dmx9uouli/image/upload/v1726302141/images_khb3oq.jpg' as value in json with key as 'cover_image_url'."

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",  # Correct the parameter to 'model'
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=200,
            n=1,
            stop=None,
            temperature=0
        )

        # Extract the response text from the API
        result = response.choices[0].message['content'].strip()

        try:
            # Try to parse the result as JSON
            cover_image_url = json.loads(result)
            
            if 'cover_image_url' in cover_image_url and cover_image_url['cover_image_url']:
                return jsonify(cover_image_url)
            else:
                return jsonify({"cover_image_url": "https://res.cloudinary.com/dmx9uouli/image/upload/v1726302141/images_khb3oq.jpg"})
        except json.JSONDecodeError:
            return jsonify({"cover_image_url": "https://res.cloudinary.com/dmx9uouli/image/upload/v1726302141/images_khb3oq.jpg"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/description', methods=['POST'])
def get_description():
    data = request.json
    book_title = data.get("title")
    
    if not book_title:
        return jsonify({"error": "Title is required"}), 400

    # Correct prompt format for ChatCompletion
    prompt = f"Give me short description of '{book_title}'? Provide response in JSON format with key 'description'. If the description is not found, return 'Description is not available.' as value in json with key as 'description'."

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",  # Correct the parameter to 'model'
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=200,
            n=1,
            stop=None,
            temperature=0
        )

        # Extract the response text from the API
        result = response.choices[0].message['content'].strip()

        try:
            # Try to parse the result as JSON
            description = json.loads(result)
            
            if 'description' in description and description['description']:
                return jsonify(description)
            else:
                return jsonify({"description": "Description not available"})
        except json.JSONDecodeError:
            return jsonify({"description": "Description not available"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/genre', methods=['POST'])
def get_genre():
    data = request.json
    book_title = data.get("title")
    
    if not book_title:
        return jsonify({"error": "Title is required"}), 400

    # Correct prompt format for ChatCompletion
    prompt = f"Give me genres of '{book_title}'? Provide response in JSON format with key 'genre' and genres of book as array of strings. If genres are not found, return [] as value in json with key as 'genre'."

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",  # Correct the parameter to 'model'
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=200,
            n=1,
            stop=None,
            temperature=0
        )

        # Extract the response text from the API
        result = response.choices[0].message['content'].strip()

        try:
            # Try to parse the result as JSON
            genre = json.loads(result)
            
            if 'genre' in genre and genre['genre']:
                return jsonify(genre)
            else:
                return jsonify({"genre": "Genre not available"})
        except json.JSONDecodeError:
            return jsonify({"genre": "Genre not available"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/isbn', methods=['POST'])
def get_isbn():
    data = request.json
    book_title = data.get("title")
    
    if not book_title:
        return jsonify({"error": "Title is required"}), 400

    # Correct prompt format for ChatCompletion
    prompt = f"Give me isbn of '{book_title}'. Provide response in JSON format with key 'isbn' in json format with keys isbn_10 and isbn_13 . If isbn are not found, return empty object."
    print(book_title)
    print(prompt)
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",  # Correct the parameter to 'model'
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=200,
            n=1,
            stop=None,
            temperature=0
        )
        print(response)
        # Extract the response text from the API
        result = response.choices[0].message['content'].strip()

        try:
            # Try to parse the result as JSON
            isbn = json.loads(result)
            print(isbn)
            if 'isbn' in isbn and isbn['isbn']:
                return jsonify(isbn)
            else:
                return jsonify({"isbn": "isbn not available"})
        except json.JSONDecodeError:
            return jsonify({"isbn": "isbn not available"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/book-suggestion', methods=['POST'])
def fetch_book_suggestion():
    data = request.json
    input_text = data.get("input")
    
    if not input_text:
        return jsonify({"error": "Input is required"}), 400

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {
                "role": "system",
                "content": "You are an expert in recommending books based on user inputs."
            },
            {
                "role": "user",
                "content": f"Based on the input provided, suggest a book and return the information in the following format:\n{{\n\"title\": \"<book title>\"}}\nInput: {input_text}"
            }
        ],
        temperature=0.7,  # Optional: adjust based on desired creativity
        max_tokens=100
    )

    reply = response['choices'][0]['message']['content']
    
    # Parse the response into the required format
    try:
        parsed_response = json.loads(reply)
        return jsonify(parsed_response), 200
    except json.JSONDecodeError:
        return jsonify({"error": "Failed to parse the response"}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 3000)), debug=os.getenv('DEBUG', 'False') == 'True')
