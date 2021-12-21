# PyTest_POC

# To Install
`pip3 install -r requirements.txt`

# To Run
To run all tests: 
`pytest --browser=chrome`

To run all tests on Saucelabs, you'll need to set a source for your Sauce credentials. Run this in your terminal:
`source ~/.bash_profile`

Now, when you run a program it will have the updated username and access key. IMPORTANT you need to do this with any new project file you create, and also any time you update your bash profile.
`pytest  --browser=chrome --host=saucelabs`

When you run on Saucelabs, you can pass in the following parameters: 
`--browser
--browserversion
--platform (IOS or Windows)`

To run only one test, you specify the test file directly, then add a ::test_name, like this: 
`
pytest tasks/test_four.py::test_asdict`

# Helpful Test Run Options
`-v  or -verbose` to get more informative results. Need to add if you want to see each test name and pass/fail as opposed a list of symbols representing each test result.

`-k <expression>` only runs tests/classes which match the given substring expression

`--maxfail=<num>`  exit after first num failures or errors

`--lf or  --last-failed` rerun only the tests that failed

`--ff or --failed-first` run all tests but run the last failures first

`--collect-only` will show you what tests will be run with the given options and configuration but won't run the tests

`-m <markexpr>` can run test by marker (You mark a test using a decorator, example: "@pytest.mark.smoke_test")

`-l/ -showlocals ` prints out the local variables in a test if the test fails

`-x` stops the tests session with the first failure

`--pdb ` starts an interactive debugging session at the point of failure

`--tb=<style>` modified the way tracebacks for failures are output
* `no tasks ` removes the traceback entirely. Just lists tests and if they passed or failed.
* `line tasks`  lists tests and if they passed or failed, but also the line they failed on.
* `short tasks`  is a more condensed version of the full traceback.
* `long tasks`  is the most informative traceback possible.

`-durations=<n> ` reports the slowest N number of tests/setups/tear downs after the tests run. If you pass in 0, it will report everything in order from slowest to fastest

`--setup-show`  lists the fixtures that ran in the setup and teardown

### These can be chained like this: 
`pytest -v --lf -x --pdb` This will run in verbose mode, re-run only the tests that failed, stop the session on the first failure, and open an interactive debugger.

### Skipping Tests
To skip a test, add the following marker:
`@pytest.mark.skip(reason="no way of currently testing this")`

Can also use skipif
`@pytest.mark.skipif(sys.version_info < (3, 7), reason="requires python3.7 or higher")`

# Site Under Test
https://the-internet.herokuapp.com/

# Tutorial Code Based On Here
https://training.saucelabs.com/seleniumpython/index.html

