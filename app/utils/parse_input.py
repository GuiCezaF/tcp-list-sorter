from typing import Optional
from app.utils.send_discord_message import SendDiscordMessage

class ParseInput:
    def parse_input(self, data: str) -> Optional[list[float]]:
        """Função para converter string recebida em uma lista de floats."""
        try:
            data = data.strip()
            if data.startswith("[") and data.endswith("]"):
                data = data[1:-1]
            numbers = list(map(float, data.split(',')))
            return numbers
        except ValueError as e:
            discord_sender = SendDiscordMessage()
            discord_sender.sendMessage(message=data, err=str(e))
            return None
