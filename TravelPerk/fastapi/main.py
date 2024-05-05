from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from models import TravelData
from funciones import travelWith,returnWith,howmanyDays,activities


app = FastAPI()
#Cors
origins=[
    "*",
    "http://localhost:5173"
    "http://localhost:8000"
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)


#Peticiones
@app.get("/")
async def root():
    return{
        "message": "My app"
    }

@app.post("/api/v1/")
def receive_travel_data(travel_data: TravelData):
    # Aquí recibimos los datos
    print("Received travel data:")
    print(travel_data)
    # Devuelve una respuesta HTTP con los datos formateados como JSON
    response_data = {
        "message": "Travel data received successfully",
        "data": travel_data,
        "list_go": travelWith(travel_data),
        "list_comeback": returnWith(travel_data),
        "list_days": howmanyDays(travel_data),
        "list_activities": activities(travel_data)
    }
    return response_data

# Manejo de excepciones HTTP personalizado
@app.exception_handler(HTTPException)
async def http_exception_handler(exc):
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": exc.detail}
    )

#FUNCION PARA EVENTOS POR LUGARES

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)



