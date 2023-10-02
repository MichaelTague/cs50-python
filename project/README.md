# Loan Calculations
#### Video Demo: TO-BE-Supplied
#### Description:

* Author:   Michael Tague
* Location: Louisville, KY
* Date:     2023-10-01

This CS50 Python final project program performs loan calculations,

The program is invoked from command line:

    python project.py

The user is asked to answer three (or four) of the following related to an amortizing monthly paid loan.  Example:

            Principal Amount: 12000
          Interest per Annum: 9.5
    Term in Years and Months: 4 years, 6 months
      Monthly Payment Amount:

Whichever question is left blank will be calculated and the loan summarized:

              Loan Principal: $12,000.00
              Loan Interest:  9.5%
              Loan Term:      4 Years, 6 Months
              Loan Payment:   $273.97
              Final Payment:  $273.47
              Total Interest: $2,793.88 (19% of payments)

The "Final Payment", the payment due in the last month of the loan, is typically less than the monthly loan payment due to dollar and cent rounding as the loan is paid.

If any one of the four fields is not provided, it will be calculated.

Additionally, care is made to adjust any calculated value so that:

    1. The "Final Payment" will NEVER exceed the "Loan Payment".
    2. But, the "Final Paymnet" will be as close as possible to the "Loan Payment" amount.
       For example, the "Loan Payment" will be reduced as much as possible to yeild a "Final Payment"
       as close as possible to the "Loan Payment", but not in excess of it.
    3. In some cases, it may be necessary for the loan to end early by one or more months.
       This is always prefered over having the "Final Payment" exceed the "Loan Payment".

This adjustment is made for any calculated field: Principal, Interest, Term, or Payment.

If a "Final Payment" will end early, it is displayed like this:

     Final Payment:  $708.16 on payment #359 (1 short of full term)

If all four questions are supplied, no calculation (or adjustment) is performed, only the "Final Payment" is determined.

If as a result, the "Final Payment" exceeds the "Loan Payment", it is considered a balloon payment and will be presented like this:

      Final Payment:  $3,167.96 (a balloon payment which included $2,139.96 of remaining principal)

After the loan summary, the user is asked if they want an "Amortization Table (Y/N)", if yes, one is provided, e.g.:

    #        Payment         Interest        Reduction        Principal
    0    -----------      -----------      -----------         3,000.00
    1         507.32            12.50           494.82         2,505.18
    2         507.32            10.44           496.88         2,008.30
    3         507.32             8.37           498.95         1,509.35
    4         507.32             6.29           501.03         1,008.32
    5         507.32             4.20           503.12           505.20
    6         507.31             2.11           505.20             0.00

The program then exits.

Input errors for negative values, or number conversion errors, etc., are shown in red.

#### Technical Details

* 5 imports: re, sys, math, decimal, and scipy
* 16 functions overall
* 327 lines long
* Decimal arithmetic is used throughout to avoid rounding issues
* scipy is used for it's numerical calculation using Newton's Method (optimize)

The formula used to determine the calculated values is based upon this:

    payment = principal * interest / (1 - (1 + interest)**(-term))

This can easily be algebracially rearranged for payment, principal, and term, but not interest.  The formula cannot be solved for interest, so instead, interest is determined by guessing the interest rate, using the payment formula, and then adjusting that guess using Newton's Method as provided in the scipy optimize function.  In typically 3-5 guesses, the interest can be determined to several digits of accuracy.

The interest thus determined, is then subject to adjustment, up or down in 0.01% increments using the final_payment function to find the optimal rate.

All calculated values, interest as well as principal, term, and payment use a similar adjustment method, up or down, in the least significant digit of each value to get the best value.

##### Key Functions
- The main function asks the four questions, calls "calc_(principal interest term payment)" for any unanswered question and then calls "print_loan" to summaarize the loan.  It then asks the user about the amortization table and prints that if desired.

- calc_principal, calc_interest, calc_term, and calc_payment calculate their respective values based upon the other three provided parameters.  Each also adjusts the answer up or down in the least significant digit of its value as described above.

- adjust_principal, adjust_interest, and adjust_payment are called by their respective "calc" functions to make final adjustments of the values.  adjust_term is not needed as it uses final_payment directly to make its adjustment.
