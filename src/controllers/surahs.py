from fastapi import APIRouter, HTTPException, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
# from fastapi_cache.decorator import cache
from src.models.surahs_response import (SurahsResponse, SurahAyahs)
from src.database.models.surahs import surahs_details
from src.database.db import engine


router = APIRouter(prefix='/surahs', tags=['Surahs'])


@router.get('/', response_model=SurahsResponse)
# @cache(namespace="test", expire=10)
async def get_surahs_details() -> JSONResponse:
    stmt = surahs_details.select()
    surahs = list()
    with engine.begin() as conn:
        result = conn.execute(stmt).all()
        if not result:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail='No Surahs Details Found')
        for rowProxy in result:
            data = dict()
            data['surah_number'] = rowProxy[0]
            data['surah_name'] = rowProxy[1]
            data['surah_english_name'] = rowProxy[2]
            data['surah_english_name_translation'] = rowProxy[3]
            data['surah_revelation_type'] = rowProxy[4]
            data['surah_ayahs_ar'] = rowProxy[5]
            data['surah_ayahs_en'] = rowProxy[6]
            surahs.append(data)

    return JSONResponse(status_code=status.HTTP_200_OK,
                        content=jsonable_encoder(SurahsResponse(**dict(i)) for i in surahs))


@router.get('/get_surah/{surah_number}', response_model=SurahsResponse)
async def get_surah_details(surah_number: int) -> JSONResponse:
    stmt = surahs_details.select().where(
        surahs_details.c.surah_number == surah_number)
    with engine.begin() as conn:
        result = conn.execute(stmt).first()
        if not result:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail='No Surahs Details Found')
        data = dict()
        data['surah_number'] = result[0]
        data['surah_name'] = result[1]
        data['surah_english_name'] = result[2]
        data['surah_english_name_translation'] = result[3]
        data['surah_revelation_type'] = result[4]
        data['surah_ayahs_ar'] = map_process(result[5])
        data['surah_ayahs_en'] = map_process(result[6])
        return JSONResponse(status_code=status.HTTP_200_OK,
                            content=jsonable_encoder(
                                SurahsResponse(**dict(data))))


@router.get('/get_surah_name/{surah_name}', response_model=SurahsResponse)
async def get_surah_by_name(surah_name: str) -> JSONResponse:
    stmt = surahs_details.select().where(
        surahs_details.c.surah_name == surah_name)
    with engine.begin() as conn:
        result = conn.execute(stmt).first()
        if not result:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail='No Surahs Details Found')
        print(result)
        data = dict()
        data['surah_number'] = result[0]
        data['surah_name'] = result[1]
        data['surah_english_name'] = result[2]
        data['surah_english_name_translation'] = result[3]
        data['surah_revelation_type'] = result[4]
        data['surah_ayahs_ar'] = map_process(result[5])
        data['surah_ayahs_en'] = map_process(result[6])
        return JSONResponse(status_code=status.HTTP_200_OK,
                            content=jsonable_encoder(
                                SurahsResponse(**dict(data))))


@router.get('/get_surah_english_name/{surah_english_name}',
            response_model=SurahsResponse)
async def get_surah_by_en_name(surah_english_name: str) -> JSONResponse:
    stmt = surahs_details.select().where(
        surahs_details.c.surah_english_name == surah_english_name)
    with engine.begin() as conn:
        result = conn.execute(stmt).first()
        if not result:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail='No Surahs Details Found')
        print(result)
        data = dict()
        data['surah_number'] = result[0]
        data['surah_name'] = result[1]
        data['surah_english_name'] = result[2]
        data['surah_english_name_translation'] = result[3]
        data['surah_revelation_type'] = result[4]
        data['surah_ayahs_ar'] = map_process(result[5])
        data['surah_ayahs_en'] = map_process(result[6])
        return JSONResponse(status_code=status.HTTP_200_OK,
                            content=jsonable_encoder(
                                SurahsResponse(**dict(data))))


def map_process(data):
    ayahs_list = list()
    for i in range(len(data)):
        ar_dict = dict()
        ayahs_ar = data[i]
        ar_dict['number'] = ayahs_ar['number']
        ar_dict['text'] = ayahs_ar['text']
        ar_dict['numberInSurah'] = ayahs_ar['numberInSurah']
        ar_dict['juz'] = ayahs_ar['juz']
        ar_dict['manzil'] = ayahs_ar['manzil']
        ar_dict['page'] = ayahs_ar['page']
        ar_dict['ruku'] = ayahs_ar['ruku']
        ar_dict['hizbQuarter'] = ayahs_ar['hizbQuarter']
        # ar_dict['sajda'] = ayahs_ar['sajda']
        ar_dict['sajda'] = ayahs_ar['sajda']
        ar_dict['audio'] = ayahs_ar['audio']
        ayahs_list.append(SurahAyahs(**dict(ar_dict)))
    return ayahs_list
# uvicorn app:root --host 0.0.0.0 --port 80 --reload
