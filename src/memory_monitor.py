import psutil


def bytes_to_gb(bytes_value):
    """바이트를 GB로 변환합니다."""
    return round(bytes_value / (1024 ** 3), 2)


def get_memory_info():
    """메모리 사용량을 반환합니다."""
    memory = psutil.virtual_memory()
    return {
        'total_gb': bytes_to_gb(memory.total),
        'used_gb': bytes_to_gb(memory.used),
        'percent': memory.percent
    }
