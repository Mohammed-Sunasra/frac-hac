export LC_ALL=en_US.UTF-8
export LANG=en_US.UTF-8

run:
	cd ./app && python ./app.py

deps:
	cd ./app/static && yarn
	cd ./app/static && node ./node_modules/webpack/bin/webpack.js
