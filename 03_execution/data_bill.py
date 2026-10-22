def main():
    data_used = float(input("Enter data used (GB): "))
    base_plan_cost = float(input("Enter base plan cost: "))

    print(data_used)
    print(base_plan_cost)
    
    data_limit = 10
    overage_rate = 2
    
    extra_data = 0
    total_bill = base_plan_cost

    if data_used > data_limit:
     print("You are over your data limit.")
    else:
     print("You are within your data limit.")

    if data_used > data_limit:
        extra_data = data_used - data_limit
        total_bill += extra_data * overage_rate

    print(f"Total bill: ${total_bill:.2f}")

if __name__ == "__main__":
        
    main()