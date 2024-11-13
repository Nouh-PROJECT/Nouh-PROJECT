from flask import Flask, render_template,jsonify,request
from flask_cors import CORS
import requests,openai,os
from dotenv.main import load_dotenv
from langchain.llms import OpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
from langchain.memory import ConversationSummaryBufferMemory

load_dotenv()

OPENAI_API_KEY=os.environ.get('OPENAI_API_KEY')

llm = OpenAI(temperature=0, openai_api_key=OPENAI_API_KEY, model_name="gpt-3.5-turbo")
memory = ConversationSummaryBufferMemory(llm=llm, max_token_limit=100)
app = Flask(__name__, template_folder="../templates")

CORS(app)

@app.route('/')
def index():
    return render_template('chatbot/index.html')

@app.route('/chatbot', methods=['POST'])
def get_data():
    data = request.get_json()
    text=data.get('data')
    user_input = text
    try:
        conversation = ConversationChain(llm=llm,memory=memory)
        output = conversation.predict(input=user_input)
        memory.save_context({"input": user_input}, {"output": output})
        return jsonify({"response":True,"message":output})
    except Exception as e:
        print(e)
        error_message = f'Error: {str(e)}'
        return jsonify({"message":error_message,"response":False})
    
if __name__ == '__main__':
    app.run()
