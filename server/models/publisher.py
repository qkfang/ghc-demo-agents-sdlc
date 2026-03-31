from typing import Optional
from . import db
from .base import BaseModel
from sqlalchemy.orm import validates, relationship

class Publisher(BaseModel):
    """Publisher model describing companies submitting games."""

    __tablename__ = 'publishers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    description = db.Column(db.Text)
    
    # One-to-many relationship: one publisher has many games
    games = relationship("Game", back_populates="publisher")

    @validates('name')
    def validate_name(self, key: str, name: str) -> str:
        """Validate that the publisher name meets minimum length requirements."""
        return self.validate_string_length('Publisher name', name, min_length=2)

    @validates('description')
    def validate_description(self, key: str, description: Optional[str]) -> Optional[str]:
        """Validate that the description is either None or long enough to be meaningful."""
        return self.validate_string_length('Description', description, min_length=10, allow_none=True)

    def __repr__(self) -> str:
        """Provide a readable representation for debugging and logs."""
        return f'<Publisher {self.name}>'

    def to_dict(self) -> dict[str, int | str | None]:
        """Serialize the publisher and related metadata to a dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'game_count': len(self.games) if self.games else 0
        }
