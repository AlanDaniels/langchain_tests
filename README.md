# LangChain Tests

Just kicking the tires of LangChain: https://python.langchain.com/docs/introduction/

To get this up and running, you'll need an account with OpenAI. First create a ".env" file, containing your OPENAI_API_KEY. Then run the following shell commands:

```bash
python -m venv .venv/
source .venv/bin/activate.bash
pip install langchain
pip install langchain_openai
pip install dotenv
python langchain_test_1.py
```

And there you go! Adding more tests later.
