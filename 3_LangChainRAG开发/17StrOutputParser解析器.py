from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_community.chat_models.tongyi import ChatTongyi

parser = StrOutputParser() # 把AIMessage类型转化为str
model = ChatTongyi(model="qwen3-max") # 模型输入要求：PromptValue或字符串或序列（BaseMessage、list、tuple、str、dict）
prompt = PromptTemplate.from_template(
    "我邻居姓：{lastname}，刚生了{gender}，请起名，仅告知我名字无需其它内容。"
)

chain = prompt | model | parser | model | parser

res: str = chain.invoke({"lastname": "张", "gender": "女儿"})
print(res)
print(type(res))

# 注意上下两种写法，下面返回的是AIMessage
chain = prompt | model | parser | model

res = chain.invoke({"lastname": "张", "gender": "女儿"})
print(res.content)
print(type(res))