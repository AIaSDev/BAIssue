# issuecraft

A minimal FastAPI issue tracker demonstrating pragmatic Clean Architecture with SQLite, PostgreSQL, pytest, and Docker.

## Architecture

This project implements Clean Architecture with the following layers:

```
src/
├── entities/           # Core business entities (Issue)
├── use_cases/          # Business logic (CreateIssue, ListIssues, GetIssue)
├── interfaces/         
│   ├── controllers/    # FastAPI controllers
│   └── gateways/       # Repository interfaces
├── frameworks/         # FastAPI app, SQLAlchemy ORM
└── core/              # Configuration and database setup
```

## Features

- **Create, List, and Get Issues**: Simple CRUD operations for issue tracking
- **Clean Architecture**: Clear separation of concerns with dependency inversion
- **Dual Database Support**: 
  - SQLite for development and CI/integration tests
  - PostgreSQL for production via `DATABASE_URL` environment variable
- **Sync SQLAlchemy**: Straightforward synchronous ORM operations
- **Comprehensive Testing**: 
  - 10 unit tests for entities and use cases
  - 8 integration tests for API endpoints
- **Docker Support**: Production-ready containerization
- **CI/CD**: GitHub Actions workflow for building and uploading Docker images

## Quick Start

### Local Development

1. **Install dependencies**:
```bash
pip install -r requirements.txt
```

2. **Run the application**:
```bash
uvicorn src.frameworks.fastapi_app:app --reload
```

3. **Access the API**:
- API: http://localhost:8000
- Interactive docs: http://localhost:8000/docs
- Health check: http://localhost:8000/health

### Docker

1. **Build the image**:
```bash
docker build -t issuecraft .
```

2. **Run the container**:
```bash
docker run -p 8000:8000 issuecraft
```

3. **With PostgreSQL** (optional):
```bash
docker run -p 8000:8000 \
  -e DATABASE_URL=postgresql://user:pass@host:5432/dbname \
  issuecraft
```

## API Endpoints

### Create an Issue
```bash
curl -X POST http://localhost:8000/issues \
  -H "Content-Type: application/json" \
  -d '{"title":"Bug fix","description":"Fix login issue","status":"open"}'
```

### List All Issues
```bash
curl http://localhost:8000/issues
```

### Get Issue by ID
```bash
curl http://localhost:8000/issues/1
```

## Testing

Run all tests:
```bash
pytest
```

Run with coverage:
```bash
pytest --cov=src --cov-report=html
```

Run only unit tests:
```bash
pytest tests/unit
```

Run only integration tests:
```bash
pytest tests/integration
```

## Configuration

Configure via environment variables:

- `DATABASE_URL`: Database connection string (default: `sqlite:///./issues.db`)
  - SQLite: `sqlite:///./issues.db`
  - PostgreSQL: `postgresql://user:password@localhost:5432/dbname`

## Project Structure

```
issuecraft/
├── .github/
│   └── workflows/
│       └── docker-build.yml    # CI/CD workflow
├── src/
│   ├── entities/               # Business entities
│   │   └── issue.py           # Issue entity
│   ├── use_cases/             # Application business logic
│   │   ├── create_issue.py    # Create issue use case
│   │   ├── list_issues.py     # List issues use case
│   │   └── get_issue.py       # Get issue use case
│   ├── interfaces/
│   │   ├── controllers/       # API controllers
│   │   │   └── issue_controller.py
│   │   └── gateways/          # Repository interfaces
│   │       └── issue_repository.py
│   ├── frameworks/            # External frameworks
│   │   ├── fastapi_app.py     # FastAPI application
│   │   ├── models.py          # SQLAlchemy models
│   │   └── sqlalchemy_repository.py
│   └── core/                  # Core configuration
│       ├── config.py          # Configuration
│       └── database.py        # Database setup
├── tests/
│   ├── unit/                  # Unit tests
│   └── integration/           # Integration tests
├── Dockerfile                 # Docker configuration
├── requirements.txt           # Python dependencies
└── pytest.ini                # Pytest configuration
```

## Development

### Code Quality

The project follows these principles:

- **Clean Architecture**: Dependencies point inward
- **Separation of Concerns**: Each layer has a specific responsibility
- **Dependency Inversion**: High-level modules don't depend on low-level modules
- **Testability**: Business logic isolated from frameworks
- **Type Hints**: Python type annotations for better IDE support

### Adding New Features

1. **Add entity** in `src/entities/` if needed
2. **Create use case** in `src/use_cases/`
3. **Implement gateway** in `src/interfaces/gateways/` if needed
4. **Add controller** in `src/interfaces/controllers/`
5. **Register routes** in `src/frameworks/fastapi_app.py`
6. **Write tests** in `tests/unit/` and `tests/integration/`

## License

This project is provided as-is for educational and demonstration purposes.
