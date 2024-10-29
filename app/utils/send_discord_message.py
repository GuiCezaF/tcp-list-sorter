import os
import requests as req

class SendDiscordMessage:
    Url = os.getenv("DISCORD_WEBHOOK")

    def sendMessage(self, message: str, err: str = None) -> None:
        try:
            errMessage: str = f"Message: {message}\n```Error: {err}```"

            data: dict = {
                "username": "James",
                "content": errMessage
            }

            response = req.post(self.Url, data=data)
            response.raise_for_status() 

        except req.exceptions.RequestException as e:
            raise RuntimeError(f"Failed to send message to Discord: {str(e)}") from e

        except Exception as e:
            raise RuntimeError(f"An unexpected error occurred: {str(e)}") from e
