from hparams import create_hparams

def test_hparams_config():
    hparams = create_hparams(config_path='tests/data/config.yaml')
    assert len(hparams.symbols) == 148
    assert hparams.n_symbols == 148