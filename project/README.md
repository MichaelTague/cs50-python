# Loan Calculations
#### Video Demo: TO-BE-Supplied
#### Description:

Author:   Michael Tague
Location: Louisville, KY
Date:     2023-10-01

This CS50P final project program performs loan calculations,

The program is invoked from command line:

    python project.py

The basic design is that the the user is asked to answer 3 or 4 of these questions,
pertaining to a ordinary monthly amortizing loan, auto, consumer, or mortgage.
E.g.:
            Principal Amount: 12000
          Interest per Annum: 9.5
    Term in Years and Months: 4 years, 6 months
      Monthly Payment Amount:

Whichever question is left blank will be calculated and the loan is summarized:

              Loan Principal: $12,000.00
              Loan Interest:  9.5%
              Loan Term:      4 Years, 6 Months
              Loan Payment:   $273.97
              Final Payment:  $273.47
              Total Interest: $2,793.88 (19% of payments)

Due to dollar and cent rounding, the the last payment ("Final Payment") is usually
a bit less than a full payment.

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
