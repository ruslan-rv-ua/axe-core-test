from .webdriver import WebDriver

_DEFAULT_SCRIPT_PATH = Path(__file__).parent
_DEFAULT_SCRIPT_FILE = 'axe.min.js'
_DEFAULT_SCRIPT = _DEFAULT_SCRIPT_PATH / _DEFAULT_SCRIPT_FILE


__all__ = ['Axe']


class Axe:
    def __init__(self, *, script_path=_DEFAULT_SCRIPT, context=None, options=None, logger=None):
        '''
                :param context: which page part(s) to analyze and/or what to exclude.
                :param options: dictionary of aXe options.
        '''
        self._script_path = script_path
        self._context = context
        self._options = options
        self._logger = logger or self._get_logger()

        self._script = set._load_script()
        self._axe_command = self._make_axe_command()

    def _get_logger(self):
        FORMAT = "[{levelname}] <{funcName}():{lineno}> {message}"
        logFormatter = logging.Formatter(FORMAT, style='{')
        logger = logging.getLogger('axe-core')
        consoleHandler = logging.StreamHandler()
        consoleHandler.setFormatter(logFormatter)
        logger.addHandler(consoleHandler)
        logger.setLevel(logging.INFO)
        return logger

    def _load_script(self):
        with open(self._script_path, 'r') as f:
            script = f.read()
        self.logger.debug(f'Script loaded from: "{self._script_path}"')
        return script

    def _make_axe_command(self):
        context = self._context
        options = self._options

        template = 'var callback = arguments[arguments.length - 1];' + \
            'axe.run({args}).then(results => callback(results))'

        args_list = []

        # If context is passed, add to args
        if context:
            args_list.append(repr(context))

        # If options is passed, add to args
        if options:
            args_list.append(str(options))

        # Add comma delimiter only if both parameters are passed
        args = ','.join(args_list)
        command = template.format(args=args)

        return command

    def inject(self, webdriver):
        """Recursively inject aXe into all iframes and the top level document.
        """
        webdriver.execute_script(self._script)

    def execute(self, webdriver):
        """Run axe against the current page.
        """
        response = webdriver.execute_async_script(self._command)
        return response

    def run(self, webdriver):
        """Inject and execute
        """
        self.inject(webdriver)
        axe_raw_result = self.execute(webdriver)
        return axe_raw_result

    def __call__(self, url, webdriver=None):
        if webdriver is None:
            with WebDriver() as webdriver:
                webdriver.get(url)
                axe_raw_result = self.run(webdriver)
        else:
            webdriver.get(url)  
            axe_raw_result = self.run(webdriver)
        return axe_raw_result

    def __repr__(self):
        return f"Axe(context={self._context}, options={self._options})"
