## Description
This project is to run three test cases as outlined in the file.

```
Application URL: http://jupiter.cloud.planittesting.com

Test case 1:
1. From the home page go to contact page
2. Click submit button
3. Verify error messages
4. Populate mandatory fields
5. Validate errors are gone

Test case 2:
1. From the home page go to contact page
2. Populate mandatory fields
3. Click submit button
4. Validate successfulsubmission message
Note: Run this test 5 times to ensure 100% pass rate

Test case 3:
1. Buy 2 Stuffed Frog, 5 Fluffy Bunny, 3 Valentine Bear
2. Go to the cart page
3. Verify the subtotal for each product is correct
4. Verify the price for each product
5. Verify that total = sum(sub totals)
```

## Techonologies Used:
```
Python
Selenium
Pytest Framework
Allure Report
```
### Prerequisites
```
selenium==4.25.0
pytest==8.3.3
webdriver-manager==4.0.2
pytest-html
allure-pytest==2.13.5

```


## Pytest
```
* Option1: Run test on both Chrome and Firefox:
pytest --browser=chrome,firefox tests/ --alluredir allure-results
* Option2: only chrome: 
pytest --browser=chrome tests/ --alluredir allure-results
* Option3: only firefox: 
pytest --browser=firefox tests/ --alluredir allure-results
```
## Reports
```
allure serve ./allure-results
```

## if allure command is not found in terminal: 
```
npm install -g allure-commandline --save-dev
```
