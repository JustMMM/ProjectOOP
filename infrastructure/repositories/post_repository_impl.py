from domain.models.post import Post
from domain.repositories.post_repository import PostRepository
from infrastructure.database.orm import PostORM
from sqlalchemy.orm import Session
from typing import List

class SQLAlchemyPostRepository(PostRepository):
    def __init__(self, session: Session):
        self.session = session

    def get_all(self) -> List[Post]:
        return [Post(id=p.id, title=p.title, content=p.content, user_id=p.user_id) for p in self.session.query(PostORM).all()]

    def get_by_id(self, post_id: int) -> Post:
        p = self.session.query(PostORM).get(post_id)
        return Post(id=p.id, title=p.title, content=p.content, user_id=p.user_id)

    def create(self, post: Post) -> Post:
        p = PostORM(title=post.title, content=post.content, user_id=post.user_id)
        self.session.add(p)
        self.session.commit()
        return Post(id=p.id, title=p.title, content=p.content, user_id=p.user_id)