# LangChain Tests

Just kicking the tires of LangChain: https://python.langchain.com/docs/introduction/

To get this up and running, you'll need accounts with OpenAI and LangChain. First create a ".env" file, containing the following:

```
LANGSMITH_TRACING=true
LANGSMITH_ENDPOINT="https://api.smith.langchain.com"
LANGSMITH_API_KEY="${YOUR_LANGSMITH_API_KEY}"
LANGSMITH_PROJECT="${YOUR_LANGSMITH_PROJECT_NAME}"
OPENAI_API_KEY=${YOUR_OPENAI_API_KEY}
```

Then run the following shell commands:

```bash
python -m venv .venv/
source .venv/bin/activate.bash
pip install langchain
pip install langchain-openai
pip install dotenv
python langchain_test_1.py
```

And there you go! Adding more tests later.
