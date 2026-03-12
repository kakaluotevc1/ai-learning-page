#!/usr/bin/env python3
"""
智谱AI文生图API调用示例
官网：https://open.bigmodel.cn
"""

from zhipuai import ZhipuAI
import os

# 设置API Key（从环境变量或手动设置）
API_KEY = os.environ.get("ZHIPU_API_KEY", "")  # 你的智谱API Key

def generate_image(prompt, output_file="output.png"):
    """调用智谱CogView-3文生图"""
    client = ZhipuAI(api_key=API_KEY)
    
    response = client.images.generations(
        model="cogview-3",  # 文生图模型
        prompt=prompt,
        size="1024x1024",   # 图片尺寸
        quality="standard",  # standard 或 hd
        response_format="url"  # url 或 base64
    )
    
    print(response)
    
    # 获取图片URL
    if response.data:
        image_url = response.data[0].url
        print(f"\n图片URL: {image_url}")
        return image_url
    return None


if __name__ == "__main__":
    if not API_KEY:
        print("请设置 ZHIPU_API_KEY 环境变量")
        print("或修改脚本中的 API_KEY 变量")
    else:
        prompt = input("请输入图片描述: ")
        generate_image(prompt)
