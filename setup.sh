rm -r dist/*

python3 setup.py sdist bdist_wheel

pip install twine

twine upload dist/*
