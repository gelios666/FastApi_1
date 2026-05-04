from fastapi import FastAPI, Depends, HTTPException, Response
from sqlalchemy.orm import Session

from .database import SessionLocal, engine
from . import models, schemas, crud

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/advertisement", response_model=schemas.AdvertisementOut, status_code=201)
def create_ad(ad: schemas.AdvertisementCreate, db: Session = Depends(get_db)):
    return crud.create_ad(db, ad)


@app.get("/advertisement/{ad_id}", response_model=schemas.AdvertisementOut)
def get_ad(ad_id: int, db: Session = Depends(get_db)):
    ad = crud.get_ad(db, ad_id)
    if not ad:
        raise HTTPException(status_code=404, detail="Not found")
    return ad


@app.patch("/advertisement/{ad_id}", response_model=schemas.AdvertisementOut)
def update_ad(ad_id: int, ad_data: schemas.AdvertisementUpdate, db: Session = Depends(get_db)):
    ad = crud.update_ad(db, ad_id, ad_data)
    if not ad:
        raise HTTPException(status_code=404, detail="Not found")
    return ad


@app.delete("/advertisement/{ad_id}", status_code=204)
def delete_ad(ad_id: int, db: Session = Depends(get_db)):
    ad = crud.delete_ad(db, ad_id)
    if not ad:
        raise HTTPException(status_code=404, detail="Not found")
    return Response(status_code=204)


@app.get("/advertisement")
def search_ads(
    title: str = None,
    author: str = None,
    min_price: float = None,
    max_price: float = None,
    limit: int = 10,
    offset: int = 0,
    db: Session = Depends(get_db),
):
    return crud.search_ads(db, title, author, min_price, max_price, limit, offset)