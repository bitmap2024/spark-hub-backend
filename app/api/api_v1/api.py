from fastapi import APIRouter

from app.api.api_v1.endpoints import auth, users, knowledge_bases, papers, messages, tags

api_router = APIRouter()

api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(knowledge_bases.router, prefix="/knowledge-bases", tags=["knowledge-bases"])
api_router.include_router(papers.router, prefix="/papers", tags=["papers"])
api_router.include_router(messages.router, prefix="/messages", tags=["messages"])
api_router.include_router(tags.router, prefix="/tags", tags=["tags"]) 