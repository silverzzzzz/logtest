from logging import getLogger

#以下はパッケージ、分割ファイルにも記載
#どこのファイルのログか特定
logger = getLogger('simple')

def say_hello():
    print("Hellow World!")
    logger.info('sayhelloを実行しました')
