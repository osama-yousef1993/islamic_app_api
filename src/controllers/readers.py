from fastapi import APIRouter, HTTPException, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
# from sqlalchemy import select
from src.models.readers_response import ReadersResponse
from src.database.models.readers import all_readers
from src.database.db import engine


router = APIRouter(prefix='/readers', tags=['Readers'])


@router.get('/', response_model=ReadersResponse)
async def get_readers() -> JSONResponse:
    stmt = all_readers.select()
    readers = list()
    with engine.begin() as conn:
        result = conn.execute(stmt).all()
        if not result:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail='No Surahs Details Found')
        for rowProxy in result:
            data = dict()
            data['identifier'] = rowProxy[0]
            data['language'] = rowProxy[1]
            data['name'] = rowProxy[2]
            data['arabic_name'] = rowProxy[3]
            data['english_name'] = rowProxy[4]
            data['format'] = rowProxy[5]
            data['type'] = rowProxy[6]
            data['surahs_sounds'] = rowProxy[7]
            readers.append(ReadersResponse(**dict(data)))
    return JSONResponse(status_code=status.HTTP_200_OK,
                        content=jsonable_encoder(readers))


@router.get('/get_reader_by_name/{name}', response_model=ReadersResponse)
async def get_reader_by_name(name: str) -> JSONResponse:
    stmt = all_readers.select().where(all_readers.c.name == name)
    with engine.begin() as conn:
        result = conn.execute(stmt).first()
        if not result:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail='No Surahs Details Found')
        data = dict()
        data['identifier'] = result[0]
        data['language'] = result[1]
        data['name'] = result[2]
        data['arabic_name'] = result[3]
        data['english_name'] = result[4]
        data['format'] = result[5]
        data['type'] = result[6]
        data['surahs_sounds'] = result[7]
        return JSONResponse(status_code=status.HTTP_200_OK,
                            content=jsonable_encoder(
                                ReadersResponse(**dict(data))))


@router.get('/get_reader_by_arabic_name/{name}',
            response_model=ReadersResponse)
async def get_reader_by_arabic_name(name: str) -> JSONResponse:
    stmt = all_readers.select().where(all_readers.c.arabic_name == name)
    with engine.begin() as conn:
        result = conn.execute(stmt).first()
        if not result:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail='No Surahs Details Found')
        data = dict()
        data['identifier'] = result[0]
        data['language'] = result[1]
        data['name'] = result[2]
        data['arabic_name'] = result[3]
        data['english_name'] = result[4]
        data['format'] = result[5]
        data['type'] = result[6]
        data['surahs_sounds'] = result[7]
        return JSONResponse(status_code=status.HTTP_200_OK,
                            content=jsonable_encoder(
                                ReadersResponse(**dict(data))))


@router.get('/get_reader_by_identifier/{identifier}',
            response_model=ReadersResponse)
async def get_reader_by_identifier(identifier: str) -> JSONResponse:
    stmt = all_readers.select().where(all_readers.c.identifier == identifier)
    with engine.begin() as conn:
        result = conn.execute(stmt).first()
        if not result:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail='No Surahs Details Found')

        data = dict()
        data['identifier'] = result[0]
        data['language'] = result[1]
        data['name'] = result[2]
        data['arabic_name'] = result[3]
        data['english_name'] = result[4]
        data['format'] = result[5]
        data['type'] = result[6]
        data['surahs_sounds'] = result[7]
        return JSONResponse(status_code=status.HTTP_200_OK,
                            content=jsonable_encoder(
                                ReadersResponse(**dict(data))))


@router.get('/get_reader_by_language/{language}',
            response_model=ReadersResponse)
async def get_reader_by_language(language: str) -> JSONResponse:
    stmt = all_readers.select().where(all_readers.c.language == language)
    readers = list()
    with engine.begin() as conn:
        result = conn.execute(stmt).all()
        if not result:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail='No Surahs Details Found')

        for rowProxy in result:
            data = dict()
            data['identifier'] = rowProxy[0]
            data['language'] = rowProxy[1]
            data['name'] = rowProxy[2]
            data['arabic_name'] = rowProxy[3]
            data['english_name'] = rowProxy[4]
            data['format'] = rowProxy[5]
            data['type'] = rowProxy[6]
            data['surahs_sounds'] = rowProxy[7]
            readers.append(ReadersResponse(**dict(data)))
        return JSONResponse(status_code=status.HTTP_200_OK,
                            content=jsonable_encoder(readers))


# uvicorn app:root --host 0.0.0.0 --port 80 --reload
