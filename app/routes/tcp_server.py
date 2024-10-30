import asyncio
from asyncio import StreamReader, StreamWriter

from app.services.organize import Organize
from app.utils.parse_input import ParseInput
from app.utils.send_discord_message import SendDiscordMessage

tcp_data: list[str] = []

async def handle_tcp_connection(reader: StreamReader, writer: StreamWriter) -> None:
    """Função para tratar conexões TCP e receber dados."""
    addr = writer.get_extra_info('peername')
    print(f"Connection from {addr} has been established.")
    
    while True:
        data: bytes = await reader.read(100)
        if not data:
            print(f"Connection from {addr} closed.")
            break

        message: str = data.decode().strip()
        print(f"Received from {addr}: {message}")
        
        numbers = ParseInput().parse_input(message)

        if numbers is None:
            error_message = f"Invalid data format from {addr}: {message}"
            print(error_message)
            
            discord_sender = SendDiscordMessage()
            discord_sender.sendMessage(message=message, err="Invalid format for input numbers.")
            continue  

        ordered_list = Organize().bubble_sort(numbers)
        
        ordered_string = ', '.join(map(str, ordered_list))
        ordered_data = ordered_string.encode()

        writer.write(ordered_data)
        await writer.drain()
    
    writer.close()
    await writer.wait_closed()
    print(f"Closed connection from {addr}.")

async def start_tcp_server() -> None:
    """Inicializa o servidor TCP."""
    print("Starting TCP server...")
    server = await asyncio.start_server(handle_tcp_connection, "0.0.0.0", 8888)
    async with server:
        print("TCP Server running on port 8888...")
        try:
            await server.serve_forever()
        except Exception as e:
            print(f"Error occurred: {e}")
            discord_sender = SendDiscordMessage()
            discord_sender.sendMessage(message="Error occurred in the TCP server", err=str(e))

