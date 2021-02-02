import logging.config
import yaml
import hello
import os

#loggerのレベル
#logging.basicConfig(filename=os.path.abspath('system.log'),level=logging.INFO)
logging.config.dictConfig(yaml.safe_load(open("logging.yaml").read()))

#以下はパッケージ、分割ファイルにも記載
#どこのファイルのログか特定
logger = logging.getLogger(__name__)


##
#ログテスト
##
logger.info('処理を開始')

print("処理を開始")

#hello.pyの読み込み
hello.say_hello()


