# 🧠 Mental Health Chatbot (LangChain + Chroma + Groq + Streamlit)

A supportive, empathetic RAG chatbot using LangChain, ChromaDB, Groq LLMs, and Streamlit.

<img width="1919" height="1029" alt="image" src="https://github.com/user-attachments/assets/e8309cbb-9563-4901-9c6b-00514aff72cb" />

<img width="1919" height="1031" alt="image" src="https://github.com/user-attachments/assets/6a1f9d78-b35b-4754-b5bf-3eed9092cae0" />

  
*Example of chatbot output in the Streamlit app*


## Prerequisites
- Python 3.10+
- A Groq API key (get one at `https://console.groq.com`)

# Setup
```bash
# 1) Create and activate a virtualenv (Windows PowerShell)
python -m venv .venv
. .venv/Scripts/Activate.ps1

# 2) Install dependencies
pip install -r requirements.txt

# 3) Configure environment
copy .env.example .env
# Edit .env and set GROQ_API_KEY

# 4) (Optional) Ingest any local docs placed in ./data
python ingest.py

# 5) Run the Streamlit app
streamlit run streamlit_app.py
```

````markdown
## Usage
1. Set your **Groq API key** as an environment variable:
   ```bash
   export GROQ_API_KEY="your_api_key_here"
````

(On Windows PowerShell, use: `setx GROQ_API_KEY "your_api_key_here"`)

2. Start the chatbot:

   ```bash
   streamlit run app.py
   ```

3. Open the provided local URL in your browser and start chatting.

   * Responses are **RAG-augmented** and streamed in real time.


## Notes
- This app is not a substitute for professional mental health care.
- In emergencies, contact local emergency services or a crisis hotline.

