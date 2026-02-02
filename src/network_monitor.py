import psutil


def bytes_to_gb(bytes_value):
    """바이트를 GB로 변환합니다."""
    return round(bytes_value / (1024 ** 3), 2)


def get_network_info():
    """네트워크 송수신 바이트를 반환합니다."""
    network = psutil.net_io_counters()
    return {
        'sent_gb': bytes_to_gb(network.bytes_sent),
        'recv_gb': bytes_to_gb(network.bytes_recv)
    }
