from sqlalchemy.orm import Session
from . import models, schemas

def create_ad(db: Session, ad: schemas.AdvertisementCreate):
    db_ad = models.Advertisement(**ad.dict())
    db.add(db_ad)
    db.commit()
    db.refresh(db_ad)
    return db_ad

def get_ad(db: Session, ad_id: int):
    return db.query(models.Advertisement).filter(models.Advertisement.id == ad_id).first()

def update_ad(db: Session, ad_id: int, ad_data: schemas.AdvertisementUpdate):
    ad = get_ad(db, ad_id)
    if not ad:
        return None

    for key, value in ad_data.dict(exclude_unset=True).items():
        setattr(ad, key, value)

    db.commit()
    db.refresh(ad)
    return ad

def delete_ad(db: Session, ad_id: int):
    ad = get_ad(db, ad_id)
    if not ad:
        return None

    db.delete(ad)
    db.commit()
    return ad

def search_ads(db: Session, title: str = None, author: str = None):
    query = db.query(models.Advertisement)

    if title:
        query = query.filter(models.Advertisement.title.ilike(f"%{title}%"))
    if author:
        query = query.filter(models.Advertisement.author.ilike(f"%{author}%"))

    return query.all()