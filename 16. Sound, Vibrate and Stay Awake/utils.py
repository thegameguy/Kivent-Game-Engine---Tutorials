from os import path
import __main__


def get_asset_path(*args):
	return path.join(path.dirname(__file__), *args)
