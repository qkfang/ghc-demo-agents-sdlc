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
    def validate_name(self, key, name):
        """Validate that the publisher name meets the minimum length requirement."""
        return self.validate_string_length('Publisher name', name, min_length=2)

    @validates('description')
    def validate_description(self, key, description):
        """Validate that the publisher description meets the minimum length requirement."""
        return self.validate_string_length('Description', description, min_length=10, allow_none=True)

    def __repr__(self):
        """Return a string representation of the Publisher instance."""
        return f'<Publisher {self.name}>'

    def to_dict(self):
        """Return a dictionary representation of the Publisher instance."""
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'game_count': len(self.games) if self.games else 0
        }