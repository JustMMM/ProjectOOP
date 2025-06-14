from dataclasses import dataclass

@dataclass
class Comment:
    id: int
    content: str
    user_id: int
    post_id: int