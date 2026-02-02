import os
import time
from colorama import Fore, Style, init
from cpu_monitor import get_cpu_info
from memory_monitor import get_memory_info
from disk_monitor import get_disk_info
from network_monitor import get_network_info

# colorama 초기화
init(autoreset=True)


def clear_screen():
    """화면을 지웁니다."""
    os.system('cls' if os.name == 'nt' else 'clear')


def get_color(percent):
    """사용률에 따라 색상을 반환합니다."""
    if percent < 50:
        return Fore.GREEN  # 녹색: 정상
    elif percent < 80:
        return Fore.YELLOW  # 노란색: 주의
    else:
        return Fore.RED  # 빨간색: 경고


def create_progress_bar(percent, length=10):
    """진행바를 생성합니다."""
    filled = int(length * percent / 100)
    bar = '#' * filled + '-' * (length - filled)
    color = get_color(percent)
    return f"{color}[{bar}]{Style.RESET_ALL}"


def display_info(cpu, memory, disk, network):
    """모든 모니터링 정보를 화면에 표시합니다."""
    print("=" * 40)
    print("  시스템 모니터링".center(40))
    print("=" * 40)

    # CPU 정보 (색상 적용)
    cpu_color = get_color(cpu['percent'])
    print(f"CPU: {cpu_color}{cpu['percent']:.1f}%{Style.RESET_ALL} {create_progress_bar(cpu['percent'])}")

    # 메모리 정보 (색상 적용)
    mem_color = get_color(memory['percent'])
    print(f"메모리: {mem_color}{memory['used_gb']}GB / {memory['total_gb']}GB ({memory['percent']:.1f}%){Style.RESET_ALL}")

    # 디스크 정보 (색상 적용)
    disk_color = get_color(disk['percent'])
    print(f"디스크: {disk_color}{disk['used_gb']}GB / {disk['total_gb']}GB ({disk['percent']:.1f}%){Style.RESET_ALL}")

    # 네트워크 정보
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
