import psutil


def bytes_to_gb(bytes_value):
    """바이트를 GB로 변환합니다."""
    return round(bytes_value / (1024 ** 3), 2)


def get_disk_info():
    """디스크 사용량을 반환합니다."""
    disk = psutil.disk_usage('/')
    return {
        'total_gb': bytes_to_gb(disk.total),
        'used_gb': bytes_to_gb(disk.used),
        'percent': disk.percent
    }
