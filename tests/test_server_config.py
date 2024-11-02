from tempfile import NamedTemporaryFile
from time import sleep

from neowg import WgServerConfig


def test_server_config() -> None:
    config1 = WgServerConfig.new("127.0.0.1", "esnp3", 10)

    with NamedTemporaryFile("w") as fout:
        config1.dump(fout.name)

        config2 = WgServerConfig.from_file(fout.name)

    assert config1._server_ip == config2._server_ip
    assert config1._net_adapter == config2._net_adapter
    assert config1._keys.private_key == config2._keys.private_key
    assert config1._keys.pubkey == config2._keys.pubkey

    for cl1, cl2 in zip(config1.clients, config2.clients):
        assert cl1._server_pubkey == cl2._server_pubkey
        assert cl1._server_host == cl2._server_host
        assert cl1._ip == cl2._ip
        assert cl1._keys.pubkey == cl2._keys.pubkey
        assert cl1._keys.private_key == cl2._keys.private_key
