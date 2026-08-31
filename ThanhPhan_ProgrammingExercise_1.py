# Function to get the amount of tickets the buyer wants to purchase
def ticket_request(tickets_remaining):
    # While loop to get valid input
    while True:
        # Try loop to go until valid input
        try:
            # Asks the buyer the amount they want
            amount = int(input("How many tickets would you like (maximum of 4)? "))
            # Checks if quantity is less than 1
            if amount < 1:
                # Prints error message
                print('Please enter a valid quantity.')
            # Checks if quantity is more than 4
            elif amount > 4:
                # Prints error message
                print('Only a maximum of four tickets can be purchased.')
            # Checks if quantity is more than amount of tickets remaining
            elif amount > tickets_remaining:
                # Prints the amount left
                print(f'There are only {tickets_remaining} tickets remaining.')
            # When amount passes validation
            else:
                # Returns the valid amount
                return amount
        # Catches errors that is not a whole number
        except ValueError:
            # Prints error message
            print('Invalid input. Please enter a whole number.')

# Main function for purchase
def main():
    # Starting amount of tickets
    total_tickets = 20
    # Accumulator for buyers
    total_buyers = 0

    # Welcoming message
    print('Welcome to the pre-sale for cinema tickets.')
    # Assigns inventory to remaining tickets variable
    tickets_remaining = total_tickets

    # While loop as long as tickets remain
    while tickets_remaining > 0:
        # Prints the amount of tickets remaining
        print(f'The amount of tickets remaining is {tickets_remaining}.')
        # Asks the user if they'd like to purchase tickets
        buy = input('Would you like to buy tickets (yes/no)? ')

        # If buyer answers "yes"
        if buy == 'yes':
            # Calls ticket_request function for valid input
            tickets_bought = ticket_request(tickets_remaining)
            # Subtracts the tickets bought from inventory
            tickets_remaining -= tickets_bought
            # Adds one buyer to accumulator
            total_buyers += 1

            # Tells user how many tickets they bought
            print(f'You have purchased {tickets_bought} tickets.\n')
            # Says how many tickets are remaining after purchase
            print(f'Total tickets remaining: {tickets_remaining}')
        # If buyer says "no"
        elif buy == 'no':
            # Prints message
            print('Thank you. Next buyer please.')
        # If answer is not "yes" or "no"
        else:
            # Prints message asking for a proper input
            print('Invalid input. Please enter "yes" or "no".')

    # Prints when all tickets are sold
    print('All tickets have been sold out.')
    # Prints how many buyers bought tickets
    print(f'Total number of buyers: {total_buyers}')

# Calls the main function to start program
if __name__ == '__main__':
    main()

