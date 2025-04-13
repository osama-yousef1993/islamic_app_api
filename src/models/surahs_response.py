from pydantic import BaseModel

from typing import List


class SurahAyahs(BaseModel):
    number: int
    text: str
    numberInSurah: int
    juz: int
    manzil: int
    page: int
    ruku: int
    hizbQuarter: int
    sajda: str
    audio: str

    class Config:
        from_attributes = True


class SurahsResponse(BaseModel):
    surah_number: int
    surah_name: str
    surah_english_name: str
    surah_english_name_translation: str
    surah_revelation_type: str
    surah_ayahs_ar: List
    surah_ayahs_en: List

    class Config:
        from_attributes = True
