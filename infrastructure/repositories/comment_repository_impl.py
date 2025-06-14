from domain.models.comment import Comment
from domain.repositories.comment_repository import CommentRepository
from infrastructure.database.orm import CommentORM
from sqlalchemy.orm import Session
from typing import List

class SQLAlchemyCommentRepository(CommentRepository):
    def __init__(self, session: Session):
        self.session = session

    def get_all_by_post_id(self, post_id: int) -> List[Comment]:
        return [Comment(id=c.id, content=c.content, user_id=c.user_id, post_id=c.post_id) for c in self.session.query(CommentORM).filter_by(post_id=post_id).all()]

    def create(self, comment: Comment) -> Comment:
        c = CommentORM(content=comment.content, user_id=comment.user_id, post_id=comment.post_id)
        self.session.add(c)
        self.session.commit()
        return Comment(id=c.id, content=c.content, user_id=c.user_id, post_id=c.post_id)