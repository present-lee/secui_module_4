import psutil


def get_cpu_info():
    """CPU 사용률과 코어 수를 반환합니다."""
    cpu_percent = psutil.cpu_percent(interval=1)
    cpu_count = psutil.cpu_count()
    return {
        'percent': cpu_percent,
        'count': cpu_count
    }
