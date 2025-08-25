import multiprocessing as mp
from multiprocessing import Pool
import config
from logger import logger
from crawler import fetch_title
from analyzer import analyze_titles
from monitor import MemoryMonitor

def main():
    urls = config.URLS
    logger.info(f"启动爬虫，目标数: {len(urls)}")

    # 使用多进程绕过 GIL
    with MemoryMonitor():  # 监控内存
        with Pool(config.NUM_PROCESSES) as pool:
            results = pool.map(fetch_title, urls)

    # 分析结果
    report = analyze_titles(results)
    logger.info("📊 报告:")
    for k, v in report.items():
        print(f"  {k}: {v}")

if __name__ == '__main__':
    main()