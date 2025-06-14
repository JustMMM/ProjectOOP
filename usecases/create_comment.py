from domain.models.comment import Comment
from domain.repositories.comment_repository import CommentRepository

class CreateCommentUseCase:
    def __init__(self, comment_repo: CommentRepository):
        self.comment_repo = comment_repo

    def execute(self, comment: Comment) -> Comment:
        return self.comment_repo.create(comment)