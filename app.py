from flask import Flask, request, jsonify
from transformers import pipeline

app = Flask(__name__)
summarizer = pipeline("summarization")

@app.route('/summarize', methods=['POST'])
async def summarize():
    try:
        data = request.get_json()
        text = data['text']

        # Use an asynchronous function for concurrent requests
        summary = await generate_legal_summary(text)

        return jsonify({'summary': summary})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

async def generate_legal_summary(text):
    # Use an asynchronous function for concurrent requests
    loop = app.loop
    return await loop.run_in_executor(None, summarizer, text)

if __name__ == '__main__':
    app.run(debug=True)
