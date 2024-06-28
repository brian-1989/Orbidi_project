from datetime import datetime, timedelta
from fastapi import HTTPException, status
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from sqlalchemy.sql import text


def get_recomendations_from_db(db: Session):
    try:
        last_thirty_days = datetime.now() - timedelta(days=30)
        query = text(f"""
            with location_category as (
                select l.id as location_id, c.id as category_id, c.place_name
                from public.locations l
                inner join public.categories c on l.id = c.id
            ), reviewed as (
                select lcr.location_id, lcr.category_id, lcr.last_reviewed
                from public.location_category_reviewed lcr
                where lcr.last_reviewed >= date('{last_thirty_days}')
            )
            select location_category.place_name, reviewed.last_reviewed
            from location_category
            full outer join reviewed on
            location_category.location_id = reviewed.location_id and
            location_category.category_id = reviewed.category_id
            order by reviewed.last_reviewed desc
            limit 10
        """)
        results = db.execute(query).fetchall()
        return [
            {
                "place_name": recomendations[0],
                "last_reviewed": recomendations[1]
            }
            for recomendations in results
        ]
    except Exception as error:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=jsonable_encoder(str(error)))
