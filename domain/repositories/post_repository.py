from abc import ABC, abstractmethod
from typing import List
from domain.models.post import Post

class PostRepository(ABC):
    @abstractmethod
    def get_all(self) -> List[Post]: pass

    @abstractmethod
    def get_by_id(self, post_id: int) -> Post: pass

    @abstractmethod
    def create(self, post: Post) -> Post: pass