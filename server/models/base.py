# filepath: server/models/base.py
from typing import Optional
from . import db

class BaseModel(db.Model):
    """Abstract base model providing common validation utilities."""

    __abstract__ = True
    
    @staticmethod
    def validate_string_length(
        field_name: str,
        value: Optional[str],
        min_length: int = 2,
        allow_none: bool = False
    ) -> Optional[str]:
        """Validate that a string has at least the minimum length when required."""
        if value is None:
            if allow_none:
                return value
            else:
                raise ValueError(f"{field_name} cannot be empty")
        
        if not isinstance(value, str):
            raise ValueError(f"{field_name} must be a string")
            
        if len(value.strip()) < min_length:
            raise ValueError(f"{field_name} must be at least {min_length} characters")
            
        return value
