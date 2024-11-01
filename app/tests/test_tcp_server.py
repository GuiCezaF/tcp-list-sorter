import asyncio
import pytest
from unittest.mock import patch, AsyncMock
from app.server.tcp_server import start_tcp_server, handle_tcp_connection

@pytest.mark.asyncio
@patch('app.server.tcp_server.asyncio.start_server', new_callable=AsyncMock)
async def test_start_tcp_server(mock_start_server):
    # Arrange
    mock_server = AsyncMock()
    mock_start_server.return_value = mock_server

    # Act
    await start_tcp_server()

    # Assert
    mock_start_server.assert_called_once_with(handle_tcp_connection, "0.0.0.0", 8888)
    mock_server.serve_forever.assert_awaited_once()


@pytest.mark.asyncio
@patch('app.server.tcp_server.asyncio.start_server', new_callable=AsyncMock)
async def test_start_tcp_server_error(mock_start_server):
    # Arrange
    mock_server = AsyncMock()
    mock_start_server.return_value = mock_server
    mock_server.serve_forever.side_effect = Exception("Simulated server error")

    # Act
    await start_tcp_server()

