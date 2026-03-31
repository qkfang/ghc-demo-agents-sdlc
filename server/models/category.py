from typing import Optional
from . import db
from .base import BaseModel
from sqlalchemy.orm import validates, relationship

class Category(BaseModel):
    """Category model for grouping games."""

    __tablename__ = 'categories'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    description = db.Column(db.Text)
    
    # One-to-many relationship: one category has many games
    games = relationship("Game", back_populates="category")
    
    @validates('name')
    def validate_name(self, key: str, name: str) -> str:
        """Validate that the category name meets minimum length requirements."""
        return self.validate_string_length('Category name', name, min_length=2)
        
    @validates('description')
    def validate_description(self, key: str, description: Optional[str]) -> Optional[str]:
        """Validate that the description is either None or long enough to be meaningful."""
        return self.validate_string_length('Description', description, min_length=10, allow_none=True)
    
    def __repr__(self) -> str:
        """Provide a readable representation for debugging and logs."""
        return f'<Category {self.name}>'
        
    def to_dict(self) -> dict[str, int | str | None]:
        """Serialize the category and related metadata to a dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'game_count': len(self.games) if self.games else 0
        }
