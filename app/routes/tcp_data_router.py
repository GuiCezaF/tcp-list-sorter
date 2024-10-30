from fastapi import APIRouter
from app.routes.tcp_server import tcp_data

router = APIRouter()

@router.get("/tcp-data")
async def get_tcp_data() -> dict[str, list[str]]:
    """Retorna os dados recebidos via TCP"""
    return {"tcp_data": tcp_data}
