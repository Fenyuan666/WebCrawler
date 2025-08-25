import tracemalloc
from logger import logger

class MemoryMonitor:
    def __enter__(self):
        tracemalloc.start()
        self.snapshot1 = tracemalloc.take_snapshot()
        logger.info("内存监控开始")
        return self

    def __exit__(self, *args):
        snapshot2 = tracemalloc.take_snapshot()
        top_stats = snapshot2.compare_to(self.snapshot1, 'lineno')

        logger.info("内存占用前5名:")
        for stat in top_stats[:5]:
            print(f"  {stat}")

        tracemalloc.stop()