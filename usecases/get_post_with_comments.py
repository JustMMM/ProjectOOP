from domain.repositories.post_repository import PostRepository
from domain.repositories.comment_repository import CommentRepository
from domain.models.post import Post
from domain.models.comment import Comment
from typing import Tuple

class GetPostWithCommentsUseCase:
    def __init__(self, post_repo: PostRepository, comment_repo: CommentRepository):
        self.post_repo = post_repo
        self.comment_repo = comment_repo

    def execute(self, post_id: int) -> Tuple[Post, list[Comment]]:
        post = self.post_repo.get_by_id(post_id)
        comments = self.comment_repo.get_all_by_post_id(post_id)
        return post, comments