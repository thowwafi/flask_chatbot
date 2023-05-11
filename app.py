from flask import Flask
from flask import request, jsonify
import llama_index
from load_vector import loadVectorIndex
import os
import tiktoken
from createVectorIndex import model_name

app = Flask(__name__)
app.config["DEBUG"] = True


os.environ["OPENAI_API_KEY"] = "OPENAI_API_KEY"

@app.route('/')
def hello_world():
    print(app.root_path)
    return "Hello World"


@app.route('/api/chatbot/', methods=['POST'])
def chatbot():
    """
    @Body: 
    {
        "number": "+6280989999",
        "question": "apa itu deltacloud.id?"
    }
    """
    request_data = request.json
    number = request_data.get('number')
    question = request_data.get('question')
    
    vectorIndex = loadVectorIndex("Store")
    query_engine = vectorIndex.as_query_engine()
    result = query_engine.query(question)

    # Count token
    encoding = tiktoken.encoding_for_model(model_name)
    question_encoded_text = encoding.encode(question)
    question_token_count = len(question_encoded_text)

    answer_encoded_text = encoding.encode(result.response)
    answer_token_count = len(answer_encoded_text)

    response = {}
    response['status'] = 'Success'
    response['number'] = number
    response['answer'] = result.response
    response['question_token_count'] = question_token_count
    response['answer_token_count'] = answer_token_count
    
    return jsonify(response)


if __name__ == '__main__':
   app.run()
