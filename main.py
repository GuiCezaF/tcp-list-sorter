import asyncio
from fastapi import FastAPI
from app.routes import home
from app.routes.tcp_data_router import router as tcp_data_router
from app.routes.tcp_server import start_tcp_server

app = FastAPI()

app.include_router(tcp_data_router)
app.include_router(home.router)


tcp_server_task = None

@app.on_event("startup")
async def startup_event():
    """Executa ações ao iniciar a aplicação."""
    global tcp_server_task
    tcp_server_task = asyncio.create_task(start_tcp_server())

@app.on_event("shutdown")
async def shutdown_event() -> None:
    """Executa ações ao desligar a aplicação."""
    print("Shutting down TCP server...")
    if tcp_server_task:
        tcp_server_task.cancel()
        try:
            await tcp_server_task  
        except asyncio.CancelledError:
            print("TCP Server stopped.")


