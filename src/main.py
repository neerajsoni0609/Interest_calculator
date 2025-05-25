import calculate_interest_rate
import calculate_fd_interest_by_date
import sys

def execute_operation():
    options = '''Please select the appropriate option:
1. Calculate Interest rate by providing dates
2. Calculate Interest rate by providing days
3. Calculate Maturity amount by providing dates
4. Calculate Maturity amount by providing days
5. Exit
Please enter the option: '''

    option = int(input(options))
    match option:
        case 1:
            calculate_interest_rate.Rate().calculate_rate_by_date()

        case 2:
            calculate_interest_rate.Rate().calculate_rate_by_days()

        case 3:
            calculate_fd_interest_by_date.Interest().calculate_amount_by_date()

        case 4:
            calculate_fd_interest_by_date.Interest().calculate_amount_by_days()
        
        case 5:
            sys.exit(0)

        case _:
            print("Incorrect option selected, exiting")
            sys.exit(1)

if __name__ == "__main__":
    execute_operation()