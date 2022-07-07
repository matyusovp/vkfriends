import logging
import os
from dotenv import load_dotenv
import requests
import sys

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

load_dotenv()
token = os.getenv('TOKEN')

VK_CONFIG = {
    "domain": "https://api.vk.com/method",
    "acceess_token": token,
    "version": "5.124",
}

def gather_process():
    logger.info("gather")
    print('Введите ID пользователя')
    user_id = int(input())
    domain = VK_CONFIG["domain"]
    access_token = VK_CONFIG["acceess_token"]
    v = VK_CONFIG["version"]
    fields = 'sex'
    query = f"{domain}/friends.get?access_token={access_token}&user_id={user_id}&fields={fields}&v={v}"
    response = requests.get(query)
    print('Файл сохранен в корневую директорию, как outputfile.json')
    with open('outputfile.json', 'wb') as outf:
        outf.write(response.content)



if __name__ == '__main__':

    logger.info("Work started")
    if sys.argv[1] == 'gather':
        gather_process()
    logger.info("work ended")
