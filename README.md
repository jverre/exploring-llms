# LLM Exploration

The code in the repository is for illustration purposes only, it was written
as part of a regular investigation into LLMs.

It is comprised on two parts:

* UI: Streamlit app used to play around with different models
* Server: Backend server used to interact with many different model types

## Running the code
```
export COMET_API_KEY=<>
export OPENAI_API_KEY=<>

cd src

streamlit run ui.py
python start_server.py
```