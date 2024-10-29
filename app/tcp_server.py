import asyncio
from asyncio import StreamReader, StreamWriter

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
        
        message: str = data.decode()
        tcp_data.append(message)
        print(f"Received from {addr}: {message}")

        writer.write(data)  
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
            SendDiscordMessage().sendMessage(message="Error occurred", err=e)
