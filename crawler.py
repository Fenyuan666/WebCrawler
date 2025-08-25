import requests
from bs4 import BeautifulSoup
import config
from logger import logger

def fetch_title(url):
    try:
        logger.info(f"开始抓取: {url}")
        response = requests.get(url, timeout=config.TIMEOUT)
        
        # 关键修复：强制设置编码为 UTF-8（解决中文乱码）
        response.encoding = 'utf-8'  # 百度等网站使用 UTF-8 编码
        response.raise_for_status()  # 检查请求是否成功

        # 解析 HTML 提取标题
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.title.string if soup.title else "No Title"

        logger.info(f"成功抓取 {url} -> {title}")
        return {
            "url": url,
            "title": title.strip(),
            "status": "success"
        }
    except Exception as e:
        logger.error(f"抓取失败 {url}: {e}")
        return {
            "url": url,
            "title": None,
            "status": "error",
            "error": str(e)
        }
    