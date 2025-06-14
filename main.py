from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from typing import List

from domain.models.user import User
from domain.models.post import Post
from domain.models.comment import Comment

from usecases.create_post import CreatePostUseCase
from usecases.create_comment import CreateCommentUseCase
from usecases.get_post_with_comments import GetPostWithCommentsUseCase

from infrastructure.database.sqlite_factory import SQLiteSessionFactory
from infrastructure.repositories.user_repository_impl import SQLAlchemyUserRepository
from infrastructure.repositories.post_repository_impl import SQLAlchemyPostRepository
from infrastructure.repositories.comment_repository_impl import SQLAlchemyCommentRepository

from infrastructure.database.orm import Base

import uvicorn

app = FastAPI()
db_url = "sqlite:///./blog.db"
session_factory = SQLiteSessionFactory(db_url)
Base.metadata.create_all(bind=session_factory.engine)

# Pydantic models
class UserIn(BaseModel):
    username: str
    email: str

class UserOut(UserIn):
    id: int

class PostIn(BaseModel):
    title: str
    content: str
    user_id: int

class PostOut(PostIn):
    id: int

class CommentIn(BaseModel):
    content: str
    user_id: int
    post_id: int

class CommentOut(CommentIn):
    id: int

class PostWithComments(BaseModel):
    post: PostOut
    comments: List[CommentOut]

# Dependency

def get_session():
    session = session_factory.create_session()
    try:
        yield session
    finally:
        session.close()

@app.post("/users", response_model=UserOut)
def create_user(user: UserIn, session=Depends(get_session)):
    repo = SQLAlchemyUserRepository(session)
    u = User(id=0, username=user.username, email=user.email)
    return repo.create(u)

@app.post("/posts", response_model=PostOut)
def create_post(post: PostIn, session=Depends(get_session)):
    repo = SQLAlchemyPostRepository(session)
    usecase = CreatePostUseCase(repo)
    p = Post(id=0, title=post.title, content=post.content, user_id=post.user_id)
    return usecase.execute(p)

@app.post("/comments", response_model=CommentOut)
def create_comment(comment: CommentIn, session=Depends(get_session)):
    repo = SQLAlchemyCommentRepository(session)
    usecase = CreateCommentUseCase(repo)
    c = Comment(id=0, content=comment.content, user_id=comment.user_id, post_id=comment.post_id)
    return usecase.execute(c)


@app.get("/posts/{post_id}", response_model=PostWithComments)
def get_post_with_comments(post_id: int, session=Depends(get_session)):
    post_repo = SQLAlchemyPostRepository(session)
    comment_repo = SQLAlchemyCommentRepository(session)
    usecase = GetPostWithCommentsUseCase(post_repo, comment_repo)

    post, comments = usecase.execute(post_id)

    post_out = PostOut(
        id=post.id,
        title=post.title,
        content=post.content,
        user_id=post.user_id
    )

    comments_out = [
        CommentOut(
            id=c.id,
            content=c.content,
            user_id=c.user_id,
            post_id=c.post_id
        )
        for c in comments
    ]

    return PostWithComments(post=post_out, comments=comments_out)


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)