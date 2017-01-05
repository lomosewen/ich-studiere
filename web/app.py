#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Entry of the Web application.

* TODO:


# Contact : Zuo Xiang
# Email   : xianglinks@gmail.com
"""

import asyncio
import logging
from logging.config import dictConfig

from aiohttp import web

logger = logging.getLogger(__name__)


def index(request):
    """Handle request for index page.

    :param request
    """
    return web.Response(body='<h1>Homepage</h1>'.encode('utf-8'),
                        content_type='text/html')


@asyncio.coroutine
def init(loop, ip_addr, port):
    """Init the web server.

    :param loop: Event loop used for processing HTTP requests
    :param ip_addr (str): ip address of server
    :param port (int): port number
    """
    web_app = web.Application(loop=loop)
    web_app.router.add_route('GET', '/', index)
    server = yield from loop.create_server(web_app.make_handler(), ip_addr, port)
    logger.info('Web server started at %s:%d' % (ip_addr, port))
    return server


def main():
    """main function

    """
    ip_addr = '127.0.0.1'
    port = 9999
    loop = asyncio.get_event_loop()
    loop.run_until_complete(init(loop, ip_addr, port))
    try:
        loop.run_forever()
    except KeyboardInterrupt:
        logger.info('KeyboardInterrupt detected, exit..')
        loop.close()

if __name__ == "__main__":
    ##############################
    #  Settings for root logger  #
    ##############################
    LOGGING_CONFIG = dict(
        version=1,
        disable_existing_loggers=False,
        formatters={
            'basic': {'format':
                      '%(asctime)s %(name)-12s %(levelname)-8s %(message)s'}
        },
        handlers={
            'console': {'class': 'logging.StreamHandler',
                        'formatter': 'basic',
                        'level': logging.DEBUG}
        },
        root={
            'handlers': ['console'],
            'level': logging.DEBUG,
        },
    )
    dictConfig(LOGGING_CONFIG)

    main()
