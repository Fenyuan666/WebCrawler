# WebCrawler 🕷️

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Active-brightgreen.svg)](https://github.com/yourusername/WebCrawler)

一个高性能、多进程的Python网络爬虫框架，专为并发抓取网页标题而设计。支持内存监控、错误处理和数据分析功能。
https://github.com/Fenyuan666/WebCrawler.git
## ✨ 功能特性

- 🚀 **多进程并发**: 使用Python多进程绕过GIL限制，提高爬取效率
- 📊 **内存监控**: 实时监控内存使用情况，防止内存泄漏
- 🔍 **智能解析**: 使用BeautifulSoup4进行HTML解析，支持中文编码
- 📝 **详细日志**: 完整的日志记录系统，便于调试和监控
- 📈 **数据分析**: 自动分析爬取结果，生成统计报告
- ⚡ **错误处理**: 完善的异常处理机制，确保程序稳定运行
- 🎯 **配置灵活**: 支持自定义并发数、超时时间等参数

## 🛠️ 技术栈

- **Python 3.7+**
- **requests**: HTTP请求库
- **BeautifulSoup4**: HTML解析库
- **multiprocessing**: 多进程支持
- **tracemalloc**: 内存监控

## 📦 安装

### 环境要求

- Python 3.7 或更高版本
- pip 包管理器

### 安装步骤

1. **克隆项目**
   ```bash
   git clone https://github.com/Fenyuan666/WebCrawler.git
   cd WebCrawler
   ```

2. **创建虚拟环境** (推荐)
   ```bash
   python -m venv myenv
   
   # Windows
   myenv\Scripts\activate
   
   # macOS/Linux
   source myenv/bin/activate
   ```

3. **安装依赖**
   ```bash
   pip install -r requirements.txt
   ```

## 🚀 使用方法

### 基本使用

1. **配置目标URL**
   
   编辑 `config.py` 文件，设置要爬取的URL列表：
   ```python
   URLS = [
       "https://www.baidu.com",
       "https://www.google.com",
       "https://www.github.com",
       # 添加更多URL...
   ]
   ```

2. **运行爬虫**
   ```bash
   python main.py
   ```

### 配置选项

在 `config.py` 中可以调整以下参数：

| 参数 | 默认值 | 说明 |
|------|--------|------|
| `NUM_PROCESSES` | 4 | 并发进程数 |
| `TIMEOUT` | 5 | 请求超时时间（秒） |
| `LOG_LEVEL` | "INFO" | 日志级别 |

### 输出示例

```
2024-01-01 12:00:00 [INFO] __main__: 启动爬虫，目标数: 2
2024-01-01 12:00:00 [INFO] __main__: 内存监控开始
2024-01-01 12:00:01 [INFO] crawler: 开始抓取: https://www.baidu.com
2024-01-01 12:00:01 [INFO] crawler: 成功抓取 https://www.baidu.com -> 百度一下，你就知道
2024-01-01 12:00:02 [INFO] analyzer: 分析完成
2024-01-01 12:00:02 [INFO] __main__: 📊 报告:
  total: 2
  success: 2
  failed: 0
  average_title_length: 8.5
  top_titles: ['百度一下，你就知道', 'Google']
```

## 📁 项目结构

```
WebCrawler/
├── main.py              # 主程序入口
├── crawler.py           # 爬虫核心模块
├── analyzer.py          # 数据分析模块
├── monitor.py           # 内存监控模块
├── logger.py            # 日志配置模块
├── config.py            # 配置文件
├── requirements.txt     # 依赖包列表
├── README.md           # 项目说明文档
├── LICENSE             # 许可证文件
└── .gitignore          # Git忽略文件
```

## 🔧 模块说明

### `main.py`
- 程序入口点
- 协调各个模块的工作
- 管理多进程池

### `crawler.py`
- 核心爬虫功能
- HTTP请求处理
- HTML解析和标题提取
- 错误处理机制

### `analyzer.py`
- 数据分析功能
- 统计成功率、失败率
- 计算平均标题长度
- 生成分析报告

### `monitor.py`
- 内存使用监控
- 性能分析
- 资源使用统计

### `logger.py`
- 日志系统配置
- 统一的日志格式
- 可配置的日志级别

### `config.py`
- 项目配置参数
- URL列表管理
- 系统参数设置

## 🎯 高级用法

### 自定义爬虫逻辑

你可以扩展 `crawler.py` 中的 `fetch_title` 函数来实现自定义的爬取逻辑：

```python
def fetch_title(url):
    # 自定义爬取逻辑
    response = requests.get(url, timeout=config.TIMEOUT)
    # 添加自定义处理...
    return result
```

### 添加新的分析功能

在 `analyzer.py` 中添加新的分析函数：

```python
def custom_analysis(results):
    # 自定义分析逻辑
    return analysis_result
```

### 扩展监控功能

可以修改 `monitor.py` 来添加更多监控指标：

```python
class ExtendedMonitor(MemoryMonitor):
    def __exit__(self, *args):
        # 添加CPU使用率监控
        # 添加网络使用监控
        super().__exit__(*args)
```

## 🐛 故障排除

### 常见问题

1. **编码问题**
   - 确保目标网站使用UTF-8编码
   - 检查 `response.encoding` 设置

2. **超时错误**
   - 增加 `TIMEOUT` 值
   - 检查网络连接

3. **内存使用过高**
   - 减少 `NUM_PROCESSES` 数量
   - 检查是否有内存泄漏

4. **请求被拒绝**
   - 添加请求头模拟浏览器
   - 增加请求间隔时间

### 调试技巧

1. **启用详细日志**
   ```python
   LOG_LEVEL = "DEBUG"
   ```

2. **单进程测试**
   ```python
   NUM_PROCESSES = 1
   ```

3. **检查网络连接**
   ```bash
   ping target-website.com
   ```

## 🤝 贡献指南

我们欢迎所有形式的贡献！

### 如何贡献

1. Fork 本项目
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启 Pull Request

### 开发环境设置

1. 安装开发依赖
   ```bash
   pip install -r requirements.txt
   pip install pytest black flake8
   ```

2. 运行测试
   ```bash
   pytest tests/
   ```

3. 代码格式化
   ```bash
   black .
   flake8 .
   ```

## 📄 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情。

## 🙏 致谢

- [requests](https://requests.readthedocs.io/) - HTTP库
- [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/) - HTML解析库
- [Python multiprocessing](https://docs.python.org/3/library/multiprocessing.html) - 多进程支持

## 📞 联系方式

- 项目主页: [https://github.com/yourusername/WebCrawler](https://github.com/yourusername/WebCrawler)
- 问题反馈: [Issues](https://github.com/yourusername/WebCrawler/issues)
- 邮箱: your.email@example.com

---

⭐ 如果这个项目对你有帮助，请给我们一个星标！
