@echo off
set TIMESTAMP=%date:~10,4%%date:~4,2%%date:~7,2%_%time:~0,2%%time:~3,2%%time:~6,2%
set REPORT_FILE=reports/html_reports/report_%TIMESTAMP%.html
pytest --html=%REPORT_FILE% --self-contained-html -v