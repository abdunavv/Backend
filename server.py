from flask import Flask, request, jsonify
from langchain_cohere import CohereEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_mongodb import MongoDBAtlasVectorSearch
from langchain.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from pymongo import MongoClient
from dotenv import load_dotenv
import os
import asyncio  # Ensure you have this if using async

from query import f  # Ensure that f() is an asynchronous function

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)

@app.route('/api/rag', methods=['POST'])
def hello_world():
    data = request.json

    job_description = data.get('job_description', None)

    if not job_description:
        return jsonify({"error": "No job description provided"}), 400

    try:
        # Assuming 'f' is an async function
        result =  f(job_description)

        # Return the result as JSON
        return jsonify({"result": result})
    except Exception as e:
        print(f"An error occurred: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Get the port from the environment variable PORT or use default 5000
    port = int(os.environ.get('PORT', 5000))
    
    # Start the Flask application, bind to 0.0.0.0 to make it externally accessible
    app.run(debug=True, host='0.0.0.0', port=port)
