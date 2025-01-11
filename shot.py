import pygame
from circleshape import CircleShape

class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.velocity = pygame.Vector2(0, 1)

    def draw(self, screen):
        pygame.draw.circle(screen, 0xffffff, self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

def count_nested_levels(nested_documents, target_document_id, level=1):
    for doc_id in nested_documents.keys():
        if doc_id == target_document_id:
            return level
        elif isinstance(nested_documents[doc_id], dict):
            n_level = count_nested_levels(
            nested_documents[doc_id], target_document_id, level + 1
            )
            if n_level == -1:
                continue
            else:
                return n_level
    return -1
