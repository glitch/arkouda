import pytest
import os
from util.test.util import start_arkouda_server, stop_arkouda_server


class ArkoudaServerFixture:
    verbose = True if os.getenv('ARKOUDA_VERBOSE') == 'True' else False
    port = int(os.getenv('ARKOUDA_SERVER_PORT', 5556))
    server = os.getenv('ARKOUDA_SERVER_HOST', 'localhost')
    full_stack_mode = True if os.getenv('ARKOUDA_FULL_STACK_TEST') == 'True' else False
    timeout = int(os.getenv('ARKOUDA_CLIENT_TIMEOUT', 5))

    @staticmethod
    def start(num_locales=1, verbose=False, log=False, port=5556, host="localhost", with_auth=False):
        """
        Start the Arkouda server and wait for it to start running. Connection info
        is written to `get_arkouda_server_info_file()`.

        :param int num_locales: the number of arkouda_server locales
        :param bool verbose: indicates whether to start the arkouda_server in verbose mode
        :param bool log: indicates whether to start arkouda_server with logging enabled
        :param int port: the desired arkouda_server port, defaults to 5555
        :param str host: the desired arkouda_server host, defaults to None
        :param bool with_auth: whether to start arkouda_server with --authenticate flag, default is False
        :return: tuple containing server host, port, and process
        :rtype: ServerInfo(host, port, process)
        """
        print("Calling ArkoudaServerFixture.start")
        return start_arkouda_server(num_locales, verbose, log, port, host, with_auth)

    @staticmethod
    def stop():
        """
        Shutdown the Arkouda server.

        :return: None
        """
        print("Calling ArkoudaServerFixture.stop")
        stop_arkouda_server()


@pytest.fixture(scope="function", params=[False, True])
def get_server(request):
    print(f"running with {request.param}")
    server = ArkoudaServerFixture()

    # ServerInfo(host, port, process) namedtuple
    info = server.start(with_auth=request.param)
    if info.token:
        print(f"token:{info.token}")
    print(f"len(info): {len(info)}")
    print(f"host:{info.host}, port:{info.port}, process:{info.process}")
    yield info



def test_init_with_auth(get_server):
    print("test_int_with_auth called")
    print(get_server)
    pass
