from openai import OpenAI

# 1. 获取client对象，OpenAI类对象
client = OpenAI(
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)

# 2. 调用模型
response = client.chat.completions.create(
    model="qwen3-max",
    messages=[
        {"role": "system", "content": "你是AI助理，回答很简洁"},
        {"role": "user", "content": "小明有2条宠物狗"},
        {"role": "assistant", "content": "好的"},
        {"role": "user", "content": "小红有3只宠物猫"},
        {"role": "assistant", "content": "好的"},
        {"role": "user", "content": "总共有几个宠物？"}
    ],
    stream=True     # 开启了流式输出的功能
)

# 3. 处理结果
# print(response.choices[0].message.content)
for chunk in response:
    '''
    1.response（响应对象）
        是什么：
        开启 stream=True 后，client.chat.completions.create() 返回的不是普通字典 / 字符串，而是一个流式迭代器（生成器）。
        格式：
        不是列表、不是字典，是一个可以用 for 循环遍历的 “数据流”。
        作用：
        模型每生成一点文字，就通过 response 传过来一点，不会等全部生成完。
    2. chunk（数据片段）是什么：循环中每一次接收到的一小段数据（流式输出的最小单位）。
    '''
    print(
        chunk.choices[0].delta.content,
        end=" ",        # 每一段之间以空格分隔
        flush=True      # 立刻刷新缓冲区
    )
