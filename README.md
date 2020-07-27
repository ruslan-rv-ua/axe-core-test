# axe-core-test

Run axe-core accessibility tests with Selenium

## Install

	python -m pip install git+https://github.com/ruslan-rv-ua/axe-core-test.git@master
	python -m pip install -e git+https://github.com/ruslan-rv-ua/axe-core-test@master#egg=axe_core_test

## Quickstart

```python
from axe_core_test import Axe

axe_tester = Axe()
axe_raw_result = axe_tester('https://www.google.com')
print(axe_raw_result)
```


## Get default webdriver

```python
from axe_core_test import Webdriver

webdriver = Webdriver()
# ...
webdriver.quit()
#
# or use context manager
#
with Webdriver() as driver:
```
		# ...
	
## Run test

```python
from axe_core_test import Axe, Webdriver

urls = ['https://www.google.com', 'github.com']
results = []
axe = Axe(context={}, options={})
with Webdriver() as webdriver:
	for url in urls:
		webdriver.get(url)
		results.append(axe.run(webdriver))
```

