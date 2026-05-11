from openai import OpenAI

# 1.获取client对象
client = OpenAI(
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)

# 2.调用模型
response = client.chat.completions.create(
    model="qwen3.6-plus",
    messages=[
        {"role": "system", "content": "你是一个很好的python编程专家,回答详细"},
        {"role": "assistant", "content": "好的，我是一个python编程专家"},
        {"role": "user", "content": "打印一到十"}
    ],
    stream=True
)
# 3.处理结果
# print(response.choices[0].message.content)
for chunk in response:
    if chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content,end=' ',flush=True) # 每一段以空格分割，立即刷新缓冲区