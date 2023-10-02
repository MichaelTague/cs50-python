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

The "Final Payment", the payment due in the last month of the loan, is typically less than the monthly loan payment due to dollar and cent rounding.

If any one of the four fields is not provided, it will be calculated.

Additionally, care is made to adjust any calculated value so that:

    1. The "Final Payment" will NEVER exceed the "Loan Payment".
    2. But, the "Final Paymnet" will be as close as possible to the "Loan Payment" amount.
       For example, the "Loan Payment" will be reduced as much as possible to to yeild a "Final Payment"
       as close as possible to the "Loan Payment", but not in excess of it.
    3. In some cases, it may be necessary for the loan to end early by one or more months.
       This is always prefered over having the "Final Payment" exceed the "Loan Payment".

If a "Final Payment" will end early, it looks like this:

     Final Payment:  $708.16 on payment #359 (1 short of full term)






327 lines
5 imports
16 functions overall

