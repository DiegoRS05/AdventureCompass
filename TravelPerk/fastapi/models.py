
from pydantic import BaseModel

class TravelData(BaseModel):
    departureDate: str
    returnDate: str
    departureCity: str
    arrivalCity: str
    
   
