# Airgapped Python ohne Installation von pypi etc

## 1. auf Entwicklungssystem: wheels runterladen
pip download -r requirements.txt -d wheel_dir
tar -czf tool.bundle.tar.gz ./tool


## auf Server

tar -xzf tool.bundle.tar.gz
python -m venv .venv
source .venv/bin/activate (linux)
.venv\Scripts\activate (windows)
pip install -r .\requirements.txt --no-index --find-links wheel_dir