import logging
import asyncio

from src.bot import Webhook

if __name__ == '__main__':
    webhook = Webhook()
    try:
        logging.basicConfig(level=logging.INFO)
        asyncio.run(webhook.create())
    except KeyboardInterrupt:
        asyncio.run(webhook.delete())
