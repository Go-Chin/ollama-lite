# ollama-lite 🚀

> 给低配电脑的本地AI助手 - 不需要OpenClaw，轻量简洁

## 这是什么？

一个**只有50行代码**的Python脚本，让你能在命令行里和本地大模型聊天。

为什么做这个？因为我折腾OpenClaw的时候发现配置太复杂了，电脑还跑不动。所以就写了个极简版本——够用就行。

## 它能做什么？

- ✅ 在命令行里和AI对话
- ✅ 支持中文输入
- ✅ 自动连接本地的Ollama
- ✅ 轻量级，不占内存

## 需要什么？

- Python 3.6+
- Ollama（[下载地址](https://ollama.com)）
- 一个能跑的模型（推荐 `llama3.2:3b`）

## 怎么用？

### 1. 安装依赖

```bash
pip install requests

## 常见问题

### Q: 输入 `python simple_chat.py` 报错"命令不存在"怎么办？

试试下面任意一种方式：
- `py simple_chat.py`（Windows推荐）
- `python3 simple_chat.py`（Mac/Linux）
- 或者在VSCode里直接按F5运行

### Q: 我想双击就能运行？

Windows用户双击 `run.bat` 即可。
Mac/Linux用户在终端执行 `./run.sh`。

## Windows用户注意事项

### 如果双击 `run.bat` 提示"无法在电脑上运行"

这是因为Windows SmartScreen拦截了批处理文件，请尝试以下方法：

**方法A（推荐）**：右键 `run.bat` → 选择"以管理员身份运行"

**方法B**：使用PowerShell脚本 `run.ps1`（右键 → 使用PowerShell运行）

**方法C**：直接在VSCode中打开项目，按 `F5` 运行

> 💡 提示：如果还是不行，请在命令行（cmd）中手动执行：
> ```
> cd 你的项目目录
> py simple_chat.py
> ```
