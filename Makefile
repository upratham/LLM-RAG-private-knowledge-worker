.PHONY: help install test clean build run setup lint format

help:
	@echo "RAG LLM - Available Commands"
	@echo "============================"
	@echo "make install     - Install dependencies"
	@echo "make setup       - Run setup script"
	@echo "make test        - Run tests"
	@echo "make test-unit   - Run unit tests only"
	@echo "make test-int    - Run integration tests only"
	@echo "make lint        - Run linters"
	@echo "make format      - Format code"
	@echo "make clean       - Clean build artifacts"
	@echo "make build       - Build knowledge base"
	@echo "make run         - Run query interface"
	@echo "make docker      - Build Docker image"
	@echo "make docker-run  - Run in Docker"

install:
	pip install -r requirements.txt

setup:
	./setup.sh

test:
	python -m pytest tests/ -v

test-unit:
	python -m pytest tests/unit/ -v

test-int:
	python -m pytest tests/integration/ -v

test-cov:
	python -m pytest --cov=src tests/ --cov-report=html

lint:
	flake8 src/ tests/ --max-line-length=120 || true
	mypy src/ || true

format:
	black src/ tests/ examples/ --line-length=120 || true

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete 2>/dev/null || true
	find . -type f -name "*.pyo" -delete 2>/dev/null || true
	find . -type d -name "*.egg-info" -exec rm -rf {} + 2>/dev/null || true
	rm -rf build/ dist/ .pytest_cache/ .coverage htmlcov/ 2>/dev/null || true

build:
	python src/main.py build data/documents

query:
	@echo "Usage: make query Q='Your question here'"
	@if [ -z "$(Q)" ]; then \
		echo "Error: Please provide a query using Q='your question'"; \
	else \
		python src/main.py query "$(Q)"; \
	fi

run:
	python src/main.py

docker:
	docker build -t rag-llm .

docker-run:
	docker-compose up

docker-stop:
	docker-compose down
