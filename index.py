#!/usr/bin/python
# encoding: utf-8

# Workflow3 supports Alfred 3's new features. The `Workflow` class
# is also compatible with Alfred 2.
from workflow import Workflow3

from util.translation import fanyi
from util.log import log
from util.encode import encode
import sys

# 支持的方法
FUNC = {
    "fanyi": fanyi,
    "encode": encode
}


def main(wf):
    cmd, args = wf.args[0].encode('utf-8'), wf.args[1:]
    for idx, arg in enumerate(args):
        args[idx] = arg.encode('utf-8')
    log(args)
    try:
        rst = FUNC[cmd](args, wf)
    except Exception as e:
        wf.add_item(title = "Coding Tools Err: {0}".format(e), valid = False)
    else:
        #直接显示
        if rst:
            wf.add_item(title = '{}: {}'.format(cmd, args), subtitle = rst,
                        arg = rst, valid = True)
    wf.send_feedback()


if __name__ == '__main__':
    wf = Workflow3()
    sys.exit(wf.run(main))