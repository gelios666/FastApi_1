from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional


class AdvertisementCreate(BaseModel):
    title: str
    description: Optional[str]
    price: float = Field(..., gt=0)
    author: str


class AdvertisementUpdate(BaseModel):
    title: Optional[str]
    description: Optional[str]
    price: Optional[float] = Field(None, gt=0)


class AdvertisementOut(BaseModel):
    id: int
    title: str
    description: Optional[str]
    price: float
    author: str
    created_at: datetime

    class Config:
        from_attributes = True