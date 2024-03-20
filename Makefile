default:
	python3 setup.py bdist_wheel
	pip3 install --user --force-reinstall --disable-pip-version-check dist/*whl




clean:
	rm -rf build/ dist/ mytest.egg-info/ mytest/my_cython_class.cpp
	pip3 uninstall --yes mytest

