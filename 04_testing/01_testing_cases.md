# Test Cases

Run each case separately. Determine the expected results by hand before running your program.

From the repository folder, run:

```text
python 03_execution/data_bill.py
```

Check the usage message, overage amount when applicable, and total bill. Paste each terminal run as evidence, then mark Pass or Fail and explain why.

## Case 1: At the data limit

- Data used (GB): 10
- Base plan cost: 40

**Expected results:**
the customer is within their 10 GB data limit. There are no extra charges
**Evidence (paste your terminal run):**

```text

```

**Pass / Fail and why:**
Enter data used (GB): 10
Enter base plan cost: 40
10.0
40.0
You are within your data limit.
Total bill: $40.00 

PASS there was no extra charge

Case 2: At 5 GB over the limit

- Data used (GB): 15
- Base plan cost: 40

**Expected results:**
The customer used 5 GB over limit, which is moderate useage.
**Evidence (paste your terminal run):**

```text

```

**Pass / Fail and why:**
Enter data used (GB): 15
Enter base plan cost: 40
15.0
40.0
You are over your data limit.
Total bill: $50.00 

Fail the program correctly calculates $50.00 but does not display the 5 GB overage or 
identify it as moderate useage

## Case 3: Above 5 GB over the limit

- Data used (GB): 15.5
- Base plan cost: 50

**Expected results:**
the customer is 5.5 GB over the limit,m which is high useage 
**Evidence (paste your terminal run):**

```text

```

**Pass / Fail and why:**
Enter data used (GB): 15.5
Enter base plan cost: 50
15.5
50.0
You are over your data limit.
Total bill: $61.00

The test passes if the program displays $61.00, identifies high useage, and shows the 5.5 GB
overage. Otherwise, it fails thr complete requirments.

If a case fails, fix the program and add evidence of the rerun below that case.
