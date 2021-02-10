import pekobot
import config
from os import path

pekobot.init(config)

bot = pekobot.get_bot()

plugin_dic = {
    "echo": 1,
}
if __name__ == '__main__':
    pekobot.init(config)
    for eve in plugin_dic:
        if plugin_dic[eve] == 1:
            pekobot.load_plugins(path.join(path.dirname(__file__), eve), eve)
    pekobot.run()
