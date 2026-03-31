from typing import Any, Optional
from . import db
from .base import BaseModel
from sqlalchemy.orm import validates, relationship

class Game(BaseModel):
    """Game model representing a crowdfunded title."""

    __tablename__ = 'games'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    star_rating = db.Column(db.Float, nullable=True)
    
    # Foreign keys for one-to-many relationships
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=False)
    publisher_id = db.Column(db.Integer, db.ForeignKey('publishers.id'), nullable=False)
    
    # One-to-many relationships (many games belong to one category/publisher)
    category = relationship("Category", back_populates="games")
    publisher = relationship("Publisher", back_populates="games")
    
    @validates('title')
    def validate_name(self, key: str, name: str) -> str:
        """Validate that the game title meets minimum length requirements."""
        return self.validate_string_length('Game title', name, min_length=2)
    
    @validates('description')
    def validate_description(self, key: str, description: Optional[str]) -> Optional[str]:
        """Validate that the description is present and sufficiently detailed."""
        if description is not None:
            return self.validate_string_length('Description', description, min_length=10, allow_none=True)
        return description
    
    def __repr__(self) -> str:
        """Provide a readable representation for debugging and logs."""
        return f'<Game {self.title}, ID: {self.id}>'

    def to_dict(self) -> dict[str, Any]:
        """Serialize the game and its relationships for API responses."""
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'publisher': {'id': self.publisher.id, 'name': self.publisher.name} if self.publisher else None,
            'category': {'id': self.category.id, 'name': self.category.name} if self.category else None,
            'starRating': self.star_rating  # Changed from star_rating to starRating
        }
