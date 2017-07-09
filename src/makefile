build:
	test  -d ../venv || virtualenv -p python3 ../venv;
	../venv/bin/pip3 install -r requirements.txt;
	npm install;	
	mkdir -p common/static/libs/sb-admin-2 && cp -r node_modules/startbootstrap-sb-admin-2/dist/* common/static/libs/sb-admin-2/;
	mkdir -p common/static/libs/bootstrap && cp -r node_modules/bootstrap/dist/* common/static/libs/bootstrap/;
	mkdir -p common/static/libs/datatables.net && cp -r node_modules/datatables.net/js/ common/static/libs/datatables.net/;
	mkdir -p common/static/libs/datatables.net-bs && cp -r node_modules/datatables.net-bs/js/ common/static/libs/datatables.net-bs/;
	cp -r node_modules/datatables.net-bs/css/ common/static/libs/datatables.net-bs/;
	mkdir -p common/static/libs/datatables.net-responsive && cp -r node_modules/datatables.net-responsive/js/ common/static/libs/datatables.net-responsive/;
	mkdir -p common/static/libs/datatables.net-responsive-bs && cp -r node_modules/datatables.net-responsive-bs/js/ common/static/libs/datatables.net-responsive-bs/;
	cp -r node_modules/datatables.net-responsive-bs/css/ common/static/libs/datatables.net-responsive-bs/;
	mkdir -p common/static/libs/font-awesome && cp -r node_modules/font-awesome/css/ common/static/libs/font-awesome/;
	cp -r node_modules/font-awesome/fonts/ common/static/libs/font-awesome/;
	mkdir -p common/static/libs/jquery && cp -r node_modules/jquery/dist/* common/static/libs/jquery/;
	mkdir -p common/static/libs/metismenu && cp -r node_modules/metismenu/dist/* common/static/libs/metismenu/;
	mkdir -p common/static/libs/bootstrap-checkbox && cp -r node_modules/bootstrap-checkbox/dist/* common/static/libs/bootstrap-checkbox/;
	mkdir -p common/static/libs/bootstrap-datepicker && cp -r node_modules/bootstrap-datepicker/dist/* common/static/libs/bootstrap-datepicker/;
	mkdir -p common/static/libs/chosen-js && cp -r node_modules/chosen-js/* common/static/libs/chosen-js/;

