# Loan Calculations
#### Video Demo: TO-BE-Supplied
#### Description:

This CS50P final project program performs loan calculations,

The basic design is that the the user is asked to answer 3 or 4 of these questions,
e.g.:
            Principal Amount: 12000
          Interest per Annum: 9.5
    Term in Years and Months: 4 years, 6 months
      Monthly Payment Amount:

If one question is left blank, that field will be calculated and the loan will be
summarized:

     Loan Principal: $12,000.00
     Loan Interest:  9.5%
     Loan Term:      4 Years, 6 Months
     Loan Payment:   $273.97
     Final Payment:  $273.47
     Total Interest: $2,793.88 (19% of payments)

Due to dollar and cent rounding, the the last payment ("Final Payment") is usually
a bit less than a full payment.

Any of the fields: Principal, Interest, Term, or Payment can be calculated from
the other three.   Each of these fields is calculated but also adjusted so that
the final payment is ALWAYS no more than the monthly loan payment, though as close
as possible (within effects of rounding).

In some cases, due to rounding, it is not possible to have the final payment occur
on the last month of the term, is that case, the final payment line might look like
this:




327 lines
5 imports
16 functions overall

