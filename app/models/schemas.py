from pydantic import BaseModel


class LoanRequest(BaseModel):
    principal: float
    annual_rate: float
    months: int