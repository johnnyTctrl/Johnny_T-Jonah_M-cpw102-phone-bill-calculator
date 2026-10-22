# Engineering Design

**Team members:** Johnny T Jonah M

Plan how your code will meet the product requirements. Keep answers brief.

## Inputs
 Data_used - float(amount of GB used).
 base_plam_cost - float(monthly plan price).

*List each input and its Python data type. Note the input assumptions.*

## Processing and decisions
The program checks if the customer used more than 10 GB. if they did, it subtracts
10 from their useage and than multiplies the extra 10 GB by 2$. it adds that amount to the base plan cost.

a nested if statement will check wether the extra useage is moderate
*What calculations and conversions are needed? How will you organize the decisions, including the nested decision?*

## Output

*What will the program display for each usage category?*
The program displays the total monthly bill.
- within limit: tells the customer they stayed within 10 GB.
- moderate: shows they went 1-5 GB over.
- high: shows they went more than 5 GB over.
## Function design
function name: is_over_limit(data_used) returns True if data useage is greater than 10
GB and False otherwise. The program uses their result to decide wether extra charges need to be caculated.
*Give your data-allowance-checking function's name, parameters, and returned result. How will the program use that result?*

