from pydantic import BaseModel


# Class describes Bank Notes features
class BankNote(BaseModel):
    variance: float
    skewness: float
    curtosis: float
    entropy: float
