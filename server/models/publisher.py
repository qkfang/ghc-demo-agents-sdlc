from typing import Any, Dict, Optional
from . import db
from .base import BaseModel
from sqlalchemy.orm import validates, relationship

class Publisher(BaseModel):
    __tablename__ = 'publishers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    description = db.Column(db.Text)
    
    # One-to-many relationship: one publisher has many games
    games = relationship("Game", back_populates="publisher")

    @validates('name')
    def validate_name(self, key: str, name: str) -> str:
        """Validate the publisher name length."""
        return self.validate_string_length('Publisher name', name, min_length=2)

    @validates('description')
    def validate_description(self, key: str, description: Optional[str]) -> Optional[str]:
        """Validate the publisher description length, allowing None."""
        return self.validate_string_length('Description', description, min_length=10, allow_none=True)

    def __repr__(self) -> str:
        """Return a readable representation of the publisher."""
        return f'<Publisher {self.name}>'

    def to_dict(self) -> Dict[str, Any]:
        """Convert the publisher instance into a serializable dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'game_count': len(self.games) if self.games else 0
        }
