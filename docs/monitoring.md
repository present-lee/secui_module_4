# 실시간 시스템 모니터링

Python 기반의 간단한 실시간 시스템 리소스 모니터링 도구입니다.

## 개요

저장 기능 없이 실시간으로 시스템 리소스 사용량을 표시하는 경량 모니터링 시스템입니다.

## 모니터링 항목

### 1. CPU 사용률
- 전체 CPU 사용률
- 코어별 CPU 사용률
- CPU 빈도 정보

### 2. Memory 사용량
- 전체 메모리 용량
- 사용 중인 메모리
- 사용 가능한 메모리
- 메모리 사용률(%)

### 3. Disk 사용량
- 디스크 전체 용량
- 사용 중인 용량
- 남은 용량
- 디스크 사용률(%)
- 읽기/쓰기 속도

### 4. Network 사용량
- 송신 바이트
- 수신 바이트
- 네트워크 인터페이스별 정보
- 초당 전송 속도

## 기술 스택

### 필수 라이브러리
```bash
pip install psutil
```

### 선택적 라이브러리 (UI 향상)
```bash
# 터미널 UI
pip install rich

# 또는 간단한 CLI
pip install colorama
```

## 프로젝트 구조

```
module_04/
├── docs/
│   └── monitoring.md
├── src/
│   ├── monitor.py          # 메인 모니터링 로직
│   ├── cpu_monitor.py      # CPU 모니터링
│   ├── memory_monitor.py   # Memory 모니터링
│   ├── disk_monitor.py     # Disk 모니터링
│   └── network_monitor.py  # Network 모니터링
├── requirements.txt
└── README.md
```

## 주요 기능

### 실시간 업데이트
- 1초 간격으로 시스템 리소스 정보 갱신
- 터미널 화면 클리어 후 최신 정보 표시

### 간단한 UI
- 텍스트 기반 UI
- 컬러 코딩으로 상태 표시
  - 녹색: 정상 (사용률 < 50%)
  - 노란색: 주의 (사용률 50-80%)
  - 빨간색: 경고 (사용률 > 80%)

### 진행 바 표시
- 각 리소스의 사용률을 시각적 진행 바로 표시

## 구현 예시

### 기본 모니터 구조
```python
import psutil
import time

def get_cpu_usage():
    return psutil.cpu_percent(interval=1)

def get_memory_info():
    mem = psutil.virtual_memory()
    return {
        'total': mem.total,
        'used': mem.used,
        'percent': mem.percent
    }

def get_disk_info():
    disk = psutil.disk_usage('/')
    return {
        'total': disk.total,
        'used': disk.used,
        'percent': disk.percent
    }

def get_network_info():
    net = psutil.net_io_counters()
    return {
        'sent': net.bytes_sent,
        'recv': net.bytes_recv
    }
```

### 실시간 모니터링 루프
```python
def monitor_loop():
    while True:
        # 화면 클리어
        clear_screen()

        # 정보 수집
        cpu = get_cpu_usage()
        memory = get_memory_info()
        disk = get_disk_info()
        network = get_network_info()

        # 정보 표시
        display_info(cpu, memory, disk, network)

        # 1초 대기
        time.sleep(1)
```

## 실행 방법

### 기본 실행
```bash
python src/monitor.py
```

### 옵션
```bash
# 업데이트 간격 설정 (초)
python src/monitor.py --interval 2

# 특정 리소스만 모니터링
python src/monitor.py --only cpu,memory
```

## 종료 방법

`Ctrl + C` 키로 프로그램 종료

## 확장 가능한 기능 (향후)

- [ ] 임계값 알림 기능
- [ ] 로그 파일 출력 옵션
- [ ] 웹 대시보드 인터페이스
- [ ] 원격 서버 모니터링
- [ ] 프로세스별 리소스 사용량
- [ ] GPU 모니터링 (NVIDIA GPU)
- [ ] 알림/경고 시스템

## 참고 자료

- [psutil 공식 문서](https://psutil.readthedocs.io/)
- [Python 실시간 모니터링 베스트 프랙티스](https://docs.python.org/3/library/time.html)

## 라이선스

MIT License

## 기여

버그 리포트나 기능 제안은 Issue를 통해 제출해주세요.
