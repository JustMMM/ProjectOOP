from domain.models.post import Post
from domain.repositories.post_repository import PostRepository

class CreatePostUseCase:
    def __init__(self, post_repo: PostRepository):
        self.post_repo = post_repo

    def execute(self, post: Post) -> Post:
        return self.post_repo.create(post)