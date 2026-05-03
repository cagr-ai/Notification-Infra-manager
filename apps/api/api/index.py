"""Vercel serverless entry: top-level ASGI ``app`` (see Vercel Python runtime docs)."""

from app.main import app

__all__ = ["app"]
