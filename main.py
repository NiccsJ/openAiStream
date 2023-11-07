import os
import json
from dotenv import load_dotenv
load_dotenv()

from flask import Flask, Response
from openai import OpenAI
app = Flask(__name__)

client = OpenAI(api_key=os.getenv("openAiApiKey"))

@app.route("/steam", methods=["GET"])
def generate_streaming_response():
    # try:
            messages = [
            {
                "role": "system",
                "content": "You are a helpful assistant who always responds in detail and in beautiful markdown format.",
            },
            {"role": "user", "content": "Hello!"},
            ]
            model="gpt-3.5-turbo"

            response = client.chat.completions.create(
                model=model,
                messages=messages,
                stream=True,  # Enable streaming from OpenAI
            )
            print(response)
            # return Response(response, content_type="text/event-stream")
            return Response(json.dumps({"hello": "hi"}))
    # except Exception as e:
    #     print(f'Some error occurred in code: {e}')
    #     return Response(json.dumps({"hello": "bye"}))


if __name__ == "__main__":
    app.run(debug=True)
