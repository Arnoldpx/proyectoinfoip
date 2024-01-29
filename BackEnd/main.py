from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class IPAddress(BaseModel):
    ip: str

@app.post("/process_ip")
def process_ip(ip_data: IPAddress):
    try:
        # Aquí puedes realizar cualquier lógica que necesites con la dirección IP
        # En este ejemplo, simplemente la devolvemos como parte de la respuesta.
        processed_ip = {"processed_ip": ip_data.ip}
        return processed_ip
    except Exception as e:
        # Manejo de excepciones si es necesario
        raise HTTPException(status_code=500, detail="Error processing IP")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
