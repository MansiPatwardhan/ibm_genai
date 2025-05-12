# linkedin post generator
This tool will analyze posts of a LinkedIn influencer and help them create the new posts based on the writing style in their old posts

# set up
1. To get started we first need to get an API_KEY from here: https://console.groq.com/keys. Inside .env update the value of GROQ_API_KEY with the API_KEY you created.
2. To get started, first install the dependencies:
     pip install -r requirements.txt
        streamlit==1.35.0
        langchain==0.2.14
        langchain-core==0.2.39
        langchain-community==0.2.12
        langchain_groq==0.1.9
        pandas==2.0.2
3. streamlit run main.py
