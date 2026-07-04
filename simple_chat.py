#!/usr/bin/env python3
"""
ollama-lite: 轻量级本地AI助手
一个不需要复杂配置的Ollama命令行客户端
"""

import requests
import json
import sys

# Ollama默认的API地址
OLLAMA_URL = "http://localhost:11434/api/generate"

def chat(prompt, model="llama3.2:3b"):
    """发送请求到Ollama并返回回复"""
    
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False  # 一次性返回结果，不流式输出
    }
    
    try:
        response = requests.post(OLLAMA_URL, json=payload)
        response.raise_for_status()
        
        result = response.json()
        return result.get("response", "（没有返回内容）")
        
    except requests.exceptions.ConnectionError:
        return "❌ 错误：无法连接到Ollama，请确保Ollama正在运行（运行 `ollama serve`）"
    except Exception as e:
        return f"❌ 错误：{str(e)}"

def main():
    """命令行交互主函数"""
    print("=" * 50)
    print("🤖 ollama-lite 本地AI助手")
    print(f"📦 当前模型: llama3.2:3b")
    print("💡 输入 'quit' 退出，输入 'help' 查看帮助")
    print("=" * 50)
    
    while True:
        try:
            # 获取用户输入
            user_input = input("\n👤 你: ").strip()
            
            if not user_input:
                continue
                
            if user_input.lower() in ['quit', 'exit', 'q']:
                print("👋 再见！")
                break
                
            if user_input.lower() == 'help':
                print("📖 直接输入问题即可，支持中文")
                print("🔧 命令: quit/exit/q 退出")
                continue
            
            # 发送请求并显示结果
            print("🤔 思考中...", end="", flush=True)
            response = chat(user_input)
            print("\r" + " " * 20 + "\r", end="")  # 清除"思考中"字样
            print(f"🤖 AI: {response}")
            
        except KeyboardInterrupt:
            print("\n👋 再见！")
            break
        except Exception as e:
            print(f"❌ 发生了意外错误: {e}")

if __name__ == "__main__":
    main()