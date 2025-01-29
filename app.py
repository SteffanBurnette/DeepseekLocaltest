#DeepSeek-R1-Distill-Qwen-1.5B
#TERMINAL COMMAND (to run model locally): ollama run deepseek-r1:1.5b
#Testing an on edge reasoning NLP model
#Note: Make sure ollama is running in the background 

from langchain_ollama import ChatOllama
import json 

llm = ChatOllama(model="deepseek-r1:1.5b", temperature = 0)
llm_json_mode = ChatOllama(model="deepseek-r1:1.5b", temperature = 0, format = "json")

msg = llm.invoke("What is the capital of france?")

print(msg.content)

#Relativly fast response on a macbook with a 
#Intel(R) Core(TM) i5-1038NG7 CPU @ 2.00GHz, 2001 Mhz,
# 4 Core(s), 8 Logical Processor(s)

p = """
Your goal is to generate targeted web search query.
The query will gather information related to a specific topic.
Topic: Cats

Return your query as a JSON object:
{{
"query":"string",
"aspect":"string",
"rationale":"string"
}}
"""

msg2 = llm_json_mode.invoke(p)
query = json.loads(msg2.content)
print(query)

msg3 = llm.invoke("Give me a summary of scaling laws for RL models.")
print(msg3.content)
#Note: The <think> tokens that are generated was apart of the training process
#2: Alot of prethinking is ommitted from the response