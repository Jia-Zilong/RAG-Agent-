# langchain_ollama
from langchain_ollama import OllamaLLM
import os

os.environ["NO_PROXY"] = "127.0.0.1,localhost"
os.environ["HTTP_PROXY"] = ""
os.environ["HTTPS_PROXY"] = ""

model = OllamaLLM(model="qwen3:4b")

res = model.invoke(input="你是谁呀能做什么？")

print(res)
