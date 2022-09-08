# Tip Calculator You just finished eating at a restaurant, and received this bill: Cost of meal: $44.50 Restaurant tax: 6.75% Tip: 15%. You’ll apply the tip to the overall cost of the meal (including tax). First, declare a variable called meal and assign it the value 44.50.

meal = 44.50

# Let’s create a variable for the tax percentage. The tax on your receipt is 6.75%. You’ll have to divide 6.75 by 100 in order to get the decimal form of the percentage. Create the variable tax and set it equal to the decimal value of 6.75%.

tax = 6.75 / 100

# You received good service, so you’d like to leave a 15% tip on top of the cost of the meal, including tax. Before we compute the tip amount for your bill, let’s set a variable for the tip percentage. We need to get the decimal form of the tip, so we divide 15.0 by 100. Store this value in a variable called tip.

tip = 15.0 / 100

# We have the three variables we need to perform our calculation, and we know some arithmetic operators that can help us out. We saw in Lesson 1 that we can reassign variables. We could say: cash_in_wallet = 7 then later change our minds and say: cash_in_wallet = 0
# Reassign meal to the value of itself + itself * tax. We’re only calculating the cost of meal and tax here. We will add tip in the next step.

meal = meal + meal * tax

# Now that meal has the cost of the food plus tax, create a variable total that is equal to meal + meal * tip.

total = meal + meal * tip

#  Print out the value of total.

print total

# Congratulations! You have calculated the value of your bill!