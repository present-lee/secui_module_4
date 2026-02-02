import os
import time
from cpu_monitor import get_cpu_info
from memory_monitor import get_memory_info
from disk_monitor import get_disk_info
from network_monitor import get_network_info


def clear_screen():
    """화면을 지웁니다."""
    os.system('cls' if os.name == 'nt' else 'clear')


def create_progress_bar(percent, length=10):
    """진행바를 생성합니다."""
    filled = int(length * percent / 100)
    bar = '#' * filled + '-' * (length - filled)
    return f"[{bar}]"


def display_info(cpu, memory, disk, network):
    """모든 모니터링 정보를 화면에 표시합니다."""
    print("=" * 40)
    print("  시스템 모니터링".center(40))
    print("=" * 40)
    print(f"CPU: {cpu['percent']:.1f}% {create_progress_bar(cpu['percent'])}")
    print(f"메모리: {memory['used_gb']}GB / {memory['total_gb']}GB ({memory['percent']:.1f}%)")
    print(f"디스크: {disk['used_gb']}GB / {disk['total_gb']}GB ({disk['percent']:.1f}%)")
    print(f"네트워크: UP {network['sent_gb']}GB / DN {network['recv_gb']}GB")
    print("=" * 40)
    print("Ctrl+C 로 종료".center(40))
    print("=" * 40)


def main():
    """메인 루프"""
    try:
        while True:
            clear_screen()

            # 각 모니터링 정보 수집
            cpu = get_cpu_info()
            memory = get_memory_info()
            disk = get_disk_info()
            network = get_network_info()

            # 화면에 표시
            display_info(cpu, memory, disk, network)

            # 1초 대기
            time.sleep(1)

    except KeyboardInterrupt:
        print("\n모니터링을 종료합니다.")


if __name__ == "__main__":
    main()
