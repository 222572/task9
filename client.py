import asyncio

async def tcp_echo_client(message):
    reader, writer = await asyncio.open_connection('127.0.0.1', 8888)

    print(f'Send: {message}')
    writer.write(message.encode())
    await writer.drain()

    data = await reader.read(100)
    print(f'Received: {data.decode()}')

    print('Closing the connection')
    writer.close()
    await writer.wait_closed()

if __name__ == '__main__':
    message = "Hello, echo server!"
    asyncio.run(tcp_echo_client(message))
