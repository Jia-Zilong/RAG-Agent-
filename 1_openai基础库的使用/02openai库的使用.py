from openai import OpenAI

# 1.获取client对象
client = OpenAI(
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)

# 2.调用模型
response = client.chat.completions.create(
    model="qwen3.6-plus",
    messages=[
        {"role": "system", "content": "你是一个很好的python编程专家,只回答最简单的内容，不要废话！"},
        {"role": "assistant", "content": "好的，我是一个python编程专家"},
        {"role": "user", "content": "讲解列表的基础知识"}
    ]
)
# 3.处理结果
print(response.choices[0].message.content)