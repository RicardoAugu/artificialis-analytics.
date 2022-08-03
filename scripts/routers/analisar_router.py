from fastapi import APIRouter, Depends, status, HTTPException
from service.analisar_servise import AnalisarService

router = APIRouter()

service = AnalisarService()

@router.post("/analisar")
def analisar():
    return service.analisar()