# Loan Calculations
#### Video Demo: TO-BE-Supplied
#### Description:

* Author:   Michael Tague
* Location: Louisville, KY
* Date:     2023-10-01

This CS50P final project program performs loan calculations,

The program is invoked from command line:

    python project.py

The user is asked to answer three (or four) of the following related to an amortizing monthly paid loan.  E.g.:

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

The "Final Payment", the payment due in the last month of the loan will is typically less than the monthly loan payment due to dollar and cent rounding.

If any one of the four fields is not provided, it will be calculated.

Additionally, care is made to adjust any calculated value so that:

    1. The "Final Payment" will NEVER exceed the "Loan Payment".
    2. But, the "Final Paymnet" will be as close as possible to the "Loan Payment" amount.
       For example, the loan payment will be reduced as much as possible to to yeild a final payment
       as close as possible to the Loan Payment as long as it does not exceed the Loan Payment.
    3. In some cases, it may be necessary for the loan to end one more more months early so as to
       not exceed the Loan Payment in the final month.  The "Final Payment" will never exceed the "Loan Payment".



Any of the fields: Principal, Interest, Term, or Payment can be calculated from
the other three.   Each of these fields is calculated but also adjusted (to the
cent, month, or 100th of a percent) so that the final payment is ALWAYS no more
than the monthly loan payment, though as close as possible (within effects of rounding).

In some cases, due to rounding and other conditions, it is not possible to have the
final payment occur on the last month of the term, in that case, the final payment
line will look like this:

     Final Payment:  $708.16 on payment #359 (1 short of full term)






327 lines
5 imports
16 functions overall

