color:
	for f in *py; do source-highlight -s python -i $$f -o $${f%py}html; done
