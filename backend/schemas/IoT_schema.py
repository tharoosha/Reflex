from pydantic import BaseModel
from datetime import datetime

class IoTInput(BaseModel):
    deviceId: str
    sensorType: str
    product: str
    remaining: int
    timestamp: datetime
