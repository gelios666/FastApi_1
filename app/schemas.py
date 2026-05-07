from pydantic import BaseModel, Field, constr
from datetime import datetime
from typing import Optional


class AdvertisementCreate(BaseModel):
    title: constr(min_length=1)
    description: Optional[str] = None
    price: float = Field(..., gt=0)
    author: constr(min_length=1)


class AdvertisementUpdate(BaseModel):
    title: Optional[constr(min_length=1)] = None
    description: Optional[str] = None
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