from logger import logger

def analyze_titles(results):
    successes = [r for r in results if r["status"] == "success"]
    errors = len([r for r in results if r["status"] == "error"])

    total_len = sum(len(r["title"]) for r in successes)
    avg_len = total_len / len(successes) if successes else 0

    report = {
        "total": len(results),
        "success": len(successes),
        "failed": errors,
        "average_title_length": round(avg_len, 2),
        "top_titles": [r["title"] for r in successes[:3]]
    }

    logger.info("分析完成")
    return report