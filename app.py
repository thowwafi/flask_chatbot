from flask import Flask
from flask import request, jsonify
import llama_index
from load_vector import loadVectorIndex
import os


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
    
    vectorIndex = loadVectorIndex("training/Store")
    query_engine = vectorIndex.as_query_engine()
    result = query_engine.query(question)

    response = {}
    response['status'] = 'Success'
    response['number'] = number
    response['answer'] = result.response
    
    return jsonify(response)


if __name__ == '__main__':
   app.run()
