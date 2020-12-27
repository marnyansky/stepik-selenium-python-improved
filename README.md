Improvements:
+ basket > cart (sticking to English grammar)
+ selected methods/functions are modified to return 'self' - instance of a class provided as argument
	optimization of related tests syntax (page.smth().smth().smth()...)
+ all comments are in English now
+ all tests moved to package 'tests'

Fixed issues (related to repository 'stepik-selenium-python-final-project'):
+ ~50% plugins from requirements.txt updated (to new versions)
+ locators.py optimized

Known issues:
+ WebDriverWait methods don't accept tuples as an argument,
so it is impossible to store "WebDriverWait" locators inside locators.py