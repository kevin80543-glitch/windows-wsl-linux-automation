# Windows + WSL Linux Automation Integration (MIS Practice Project)

## 專案簡介

本專案模擬企業 MIS 在 Windows 環境下整合 Linux 自動化流程的實務情境。

使用者於 Windows 端觸發任務，實際處理流程透過 WSL 交由 Linux 執行，
並以 Python 進行資料處理與 API 串接，最終結果輸出回 Windows，
同時保留應用層與排程層 log 以確保可維運性。

本專案由個人獨立完成，涵蓋跨系統整合、排程設計與錯誤追蹤設計。

### 設計目的

在實務環境中，Windows 為主要使用者操作環境，
而 Linux 常作為自動化與後端處理平台。

本專案示範如何透過 WSL 作為橋接層，
建立可由使用者手動觸發，亦可由 cron 自動執行的整合流程，
提升系統彈性與維運效率。

## 專案結構

windows_launcher/
 └─ run_weather.bat         # Windows 端啟動腳本

linux/
 ├─ run_weather.sh          # Linux 統一入口腳本
 ├─ test_weather_api.py     # 資料處理主程式
 └─ requirements.txt

output_sample/
 ├─ weather_output_sample.csv
 └─ weather.log.example

## Output Structure

- Windows real output: C:\Users\<username>\Desktop\mis_output
- Sample files for GitHub demo: output_sample/

Windows (BAT)
    ↓
WSL (bash)
    ↓
Python (API / Data Processing)
    ↓
Windows Output Folder
    ↓
Log + Cron Automation

## Tech Stack

- Windows 10/11
- WSL (Ubuntu)
- Bash
- Python 3.x
- cron
- REST API

## How to Run

### Manual Execution (Windows)

1. Double-click `run_weather.bat`

### Cron Execution (WSL)

crontab -e

Example:
*/30 * * * * /home/user/windows_wsl_integration_project/linux/run_weather.sh >> cron_weather.log 2>&1

## Notes

- Real output files are generated under:
  C:\Users\<username>\Desktop\mis_output

- Only sample files are included in this repository for demonstration.

## Logging Design

- Application Log: weather.log
- Scheduler Log: cron_weather.log
- Windows Output: weather_output.csv
