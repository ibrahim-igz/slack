import os
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from slack_sdk import WebClient





client = WebClient(token='xoxb-3608320528308-4318604258004-387PvNm523lagDBpipZFmEZb')
# Initializes your app with your bot token and socket mode handler
app = App(token='xoxb-3608320528308-4318604258004-387PvNm523lagDBpipZFmEZb')
tasks_report = []


# Listens to incoming messages that contain "hello"
@app.command("/test")
def handle_command(body, ack, client, logger):
    logger.info(body)
    ack()
    ch_id = body.get('channel_id')
    print(ch_id)
    text = body['text']
    print(f"i am the text: {text}")

    client.chat_postMessage(channel=ch_id, text=text)


if __name__ == "__main__":
    # os.environ["SLACK_APP_TOKEN"] app level token in basic

    SocketModeHandler(app,
                      'xapp-1-A049NNLDXKK-4410322620869-564294162255057e633a12d316f877f04ebd2900decbd798a83f885b778f690a').start()
