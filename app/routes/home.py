from dotenv import load_dotenv
from fastapi import APIRouter
load_dotenv()

from app.utils.send_discord_message import SendDiscordMessage


router = APIRouter()

@router.get("/")
async def home() -> dict[str, str]:
    """Endpoint de verificação do servidor."""
    discord_message_sender = SendDiscordMessage()
    discord_message_sender.sendMessage(message="Servidor Funcionando")
    
    return {"message": "Server is running"}
