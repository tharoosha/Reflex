from pydantic import BaseModel
from datetime import datetime

class IoTInput(BaseModel):
    deviceId: str
    sensorType: str
    product_type: str
    remaining: int
    unit:str
    timestamp: datetime
