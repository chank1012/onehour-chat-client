import websocket

"""
이건 클라이언트입니다
"""

import websocket

try:
    import thread
except ImportError:
    import _thread as thread



def on_message(ws, message):
    print(message)


def on_error(ws, error):
    print(error)


def on_close(ws):
    print("### closed ###")


def on_open(ws):
    def run(*args):
        while True:
            x = input('메세지를 입력하세요 : ')
            ws.send(x)
        ws.close()
        print("thread terminating...")

    thread.start_new_thread(run, ())


if __name__ == "__main__":
    websocket.enableTrace(True)
    nickname = input('닉네임을 입력해 주세요 : ')
    address = "ws://localhost:8000/chat?nickname=" + nickname
    print('채팅서버 ' + address + ' 에 접속합니다')
    ws = websocket.WebSocketApp(address,
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    ws.on_open = on_open
    ws.run_forever()
