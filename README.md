# CSGOEmpireTask

### Task 1

This is our main product and the landing page https://csgoempire.com/roulette
How would you approach the testing of roulette? Describe the tests that you would do and the things you'd pay attention to.

Add your solutions to a repo and share the link to it with us below.

### 8 similar cases:

#### 1. Positive E2E test:

1.1 Logged into the user account.

1.2 Topped up the balance.

1.3 Checked that the balance was updated correctly.

1.4 Selected a game.

1.5 Entered the stake amount in the designated field.

1.6 Chose the bet category.

1.7 Verified that the bet was accepted correctly.

1.8 After settlement, confirmed that the balance was updated correctly.

1.9 Logged out of the user account.

#### 2.Boundary Values Check:

2.1 Set Maximum Amount:

1. Set the maximum stake amount.

2. Confirm that the stake was successfully accepted.

3. After settlement, verify if the balance has been updated correctly.

2.2 Set Minimum Amount:

1. Set the minimum stake amount.

2. Confirm that the stake was successfully accepted.

3. After settlement, verify if the balance has been updated correctly.

#### 3. Attempting to Place a Bet with 0 Amount or a Negative Number:

3.1 Place a bet with 0 amount:
1. Specify the stake amount as 0.

2. Check if the bet was rejected as expected.

3. Ensure that the balance remains unchanged.

3.2 Place a bet with a negative number:

1. Specify the stake amount as a negative number.

2. Check if the bet was rejected as expected.

3. Ensure that the balance remains unchanged.

#### 4. Attempting to Place a Bet When the Roulette is Already in Progress and Bets Should Not be Accepted:

4.1 Start the roulette.
1. Ensure that the roulette is active.

2. Initiate the spinning process.

4.2 Attempt to place a bet after the roulette has started:

1. Try to place a bet.

2. Check if the bet was rejected as expected.

3. Ensure that the system did not accept the bet after the roulette started.

#### 5. Checking profit limits in the game: Determining the maximum bet amount for each category:
1. Determine the maximum possible winning amount for each betting category.
2. Ensure that the system prevents placing bets that could lead to exceeding the established profit limits.

#### 6. Checking balance after a winning or losing bet:

After a winning bet:
1. Place a bet that is expected to result in a win.
2. After the draw, verify if the balance has increased by the corresponding winning amount.

After a losing bet:
1. Place a bet that is expected to result in a loss.
2. After the draw, verify if the balance has decreased by the losing amount.


#### 7. Verification of displaying only the hashed server seed for the user:

Verification of displaying only the hashed server seed:
1. Request information about the server seed for the current bet.
2. Ensure that the user only sees the hashed version of the server seed, not its actual value.

Updating the nonce value:
1. Place a bet.
2. Ensure that the nonce value for the next bet has been updated.

Updating the server seed value:
1. Place a bet
2. Refresh server seed
3. Place bet
4. Ensure that the nonce for the next bet has also been "1" in accordance with the new server seed

#### 8. Verification of nonce value and balance update when playing the same game in different windows of the same browser and different browsers:

Same browser windows:
1. Open the game in two different tabs of the same browser.
2. Place a bet in one window and check for the update of the nonce value.
3. Immediately after, place another bet in the other window and confirm the update of the nonce value.
4. Ensure that the balance is updated correctly after each bet in different windows.

Different browsers:
1. Open the game in two different browsers.
2. Place a bet in one browser and check for the update of the nonce value.
3. Immediately after, place another bet in the other browser and confirm the update of the nonce value.
4. Ensure that the balance is updated correctly after each bet in different browsers.

### Task 2

Again, this is our main product and the landing page https://csgoempire.com/roulette

Please write some automated test for roulette. Creating an account and signing in is not required. You are free to choose the tool and the programming language that you prefer.

Add your solutions to a repo and share the link to it with us below.


#### Answer:

My test is designed to verify the functionality of clearing the value from the "amount" field using the "Clear" button. However, the tests are failing due to a blockage on your side, requiring session data and user agents for successful execution.
You can run my test by Docker.

### Task 3

Give a brief rationale for why you approached this assessment the way you did. If you had more time, would you do anything differently? Why or why not?

### Answer

All 8 cases provide comprehensive coverage of key scenarios and edge cases, which is a good approach for testing roulette. These tests ensure checking key functionalities such as bets, balance, input validation, as well as updating server seed and nonce values.

The use of different browsers and windows adds complexity and ensures the system works correctly in various usage scenarios.

The tests offer an opportunity to identify issues with data input, balance updates, and also provide security checks since user agents and session data are crucial aspects in bypassing bot protection.

Additional Notes:

If I had more time, I would consider implementing reporting to more thoroughly track test results and quickly detect issues. Additionally, I might have added more test cases related to different usage scenarios that could impact roulette functionality.

However, overall, the provided tests serve as a good starting point to ensure the reliability and correctness of the roulette functionality.