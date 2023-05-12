# Flask Chatbot
###### Description:
> Construct a chatbot by giving internal data. As we are feeding our own data and creating a knowledge base, all the responses will be based on our data.

## Installation

1. Clone this repository:
    ```bash
    git clone
    ```
2. Create Python Virtual Environment:
    ```bash
    python3 -m venv venv
    ```
3. Activate Virtual Environment:
    Linux
    ```bash
    source venv/bin/activate
    ```
    Windows
    ```bash
    venv\Scripts\activate
    ```
4. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
5. Run the app:
    ```bash
    flask --app app run
    ```
6. Open the app in your browser: http://localhost:5000


## Create new vector index
1. Upload your txt files to the folder `Source/`
2. Activate the virtual environment
    ```bash
    source venv/bin/activate
    ```
3. Run the script
    ```bash
    python createVectorIndex.py Source
    ```
4. The new vector index will be created in the folder `Store/`
5. Restart the app to use the new vector index
    - if the app is running in a terminal, press `Ctrl+C` to stop the app
    - run the app again
        ```bash
        flask --app app run
        ```


## Update .env file
1. Create a new file `.env` in the root directory
2. Add the following lines to the file
    ```bash
    OPENAI_API_KEY="..."
    MODEL_NAME="text-ada-001"
    ```
    - Add your OpenAI API key in the place of `...`. 
    - You can get your API key from [here](https://platform.openai.com/account/api-keys).
    - List of available models can be found [here](https://platform.openai.com/docs/models/gpt-3).
    - The default model is `text-ada-001` which is the best model for text completion, usually the fastest model in the GPT-3 series, and lowest cost.
    - The model can be changed to any other model from the list.
