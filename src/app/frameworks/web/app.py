"""Main FastAPI application with route registration."""
from fastapi import FastAPI

from app.core.config import Config
from app.interfaces.controllers.issue_controller import IssueController


def create_app(init_db: bool = True) -> FastAPI:
    """Create and configure the FastAPI application."""
    # Create FastAPI app
    app = FastAPI(
        title=Config.API_TITLE,
        version=Config.API_VERSION,
        description=Config.API_DESCRIPTION
    )
    
    # Register routes
    app.post("/issues")(IssueController.create_issue)
    app.get("/issues")(IssueController.list_issues)
    app.get("/issues/{issue_id}")(IssueController.get_issue)
    
    @app.get("/health")
    def health_check():
        """Health check endpoint."""
        return {"status": "healthy"}
    
    # Initialize database tables if requested
    if init_db:
        from app.core.database import init_db as _init_db
        _init_db()
    
    return app


# Create the app instance
app = create_app()
