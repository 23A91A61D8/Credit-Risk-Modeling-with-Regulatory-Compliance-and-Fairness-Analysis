# Data Dictionary – Engineered Features

## credit_amount_per_month
Credit amount divided by loan duration.
Captures repayment burden per month.

## credit_amount_per_age
Credit amount normalized by applicant age.
Reduces scale bias across age groups.

## age_duration_interaction
Interaction between age and loan duration.
Captures combined repayment risk.

## job_credit_interaction
Interaction between employment status and credit amount.
Reflects income stability vs loan size.

## log_credit_amount
Log-transformed credit amount.
Reduces skewness in monetary values.

## sqrt_duration
Square root transformation of loan duration.
Stabilizes variance.

## saving_account_score
Ordinal encoding of saving account status.
Represents financial reserves.

## checking_account_score
Ordinal encoding of checking account balance.
Indicates liquidity strength.

## high_credit_flag
Binary indicator for above-median credit amount.
Flags high exposure loans.

## long_duration_flag
Binary indicator for above-median loan duration.
Flags long-term repayment risk.
