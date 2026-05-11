import os
import json
from openai import OpenAI

# ===================== 【强制修复连接问题】=====================
os.environ["NO_PROXY"] = "127.0.0.1,localhost"
os.environ["HTTP_PROXY"] = ""
os.environ["HTTPS_PROXY"] = ""
# ==============================================================

client = OpenAI(
    base_url="http://127.0.0.1:11434/v1",
    api_key="dummy_key",  # 随便填
    timeout=120
)

schema = ['日期', '股票名称', '开盘价', '收盘价', '成交量']
examples_data = [
    {
        "content": "2023-01-10，股市震荡。股票强大科技A股今日开盘价100人民币，一度飙升至105人民币，随后回落至98人民币，最终以102人民币收盘，成交量达到520000。",
        "answers": {"日期":"2023-01-10","股票名称":"强大科技A股","开盘价":"100人民币","收盘价":"102人民币","成交量":"520000"}
    },
    {
        "content": "2024-05-16，股市利好。股票英伟达美股今日开盘价105美元，一度飙升至109美元，随后回落至100美元，最终以116美元收盘，成交量达到3560000。",
        "answers": {"日期":"2024-05-16","股票名称":"英伟达美股","开盘价":"105美元","收盘价":"116美元","成交量":"3560000"}
    }
]

questions = [
    "2025-06-16，股市利好。股票传智教育A股今日开盘价66人民币，一度飙升至70人民币，随后回落至65人民币，最终以68人民币收盘，成交量达到123000。",
    "2025-06-06，股市利好。股票黑马程序员A股今日开盘价200人民币，一度飙升至211人民币，随后回落至201人民币，最终以206人民币收盘。"
]

messages = [
    {"role": "system", "content": f"你帮我完成信息抽取，抽取{schema}，输出JSON字符串，不存在填原文未提及"}
]

for example in examples_data:
    messages.append({"role": "user", "content": example["content"]})
    messages.append({"role": "assistant", "content": json.dumps(example["answers"], ensure_ascii=False)})

# ===================== 【流式输出：防止崩溃】=====================
for q in questions:
    print("\n抽取结果：")
    try:
        response = client.chat.completions.create(
            model="qwen3:4b",
            messages=messages + [{"role": "user", "content": f"抽取：{q}"}],
            stream=True  # ✅ 关键！开启流式，模型不会崩
        )

        full_ans = ""
        for chunk in response:
            if chunk.choices[0].delta.content:
                content = chunk.choices[0].delta.content
                print(content, end="", flush=True)
                full_ans += content

    except Exception as e:
        print("错误：", e)