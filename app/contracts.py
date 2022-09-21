from pydantic import BaseModel


class Item(BaseModel):
    """Contract for item."""

    name: str
    description: str or None = None
    price: float
    tax: float or None = None
