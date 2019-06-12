README.md: head.md smartfind.py test.py Makefile
	ipython --no-confirm-exit < test.py | sed -n -e '/from/,$$p' | cat head.md - > $@
