from database import create_tables
from customer_manager import CustomerManager
from transaction_manager import TransactionManager


def main():

    create_tables()

    customer = CustomerManager()
    transaction = TransactionManager()

    print("=" * 50)
    print("     Grocery Voice Udhar Assistant")
    print("=" * 50)

    while True:

        print("\n========== Customer ==========")
        print("1. Add Customer")
        print("2. Show Customers")

        print("\n======== Transactions ========")
        print("3. Add Udhar")
        print("4. Add Payment")
        print("5. Customer Balance")

        print("\n==============================")
        print("0. Exit")

        choice = input("\nEnter Choice : ")

        # -------------------------------
        # Add Customer
        # -------------------------------
        if choice == "1":

            name = input("Customer Name : ")
            mobile = input("Mobile Number : ")

            try:

                message = customer.add_customer(
                    name,
                    mobile
                )

                print("\n", message)

            except Exception as e:

                print("\n", e)

        # -------------------------------
        # Show Customers
        # -------------------------------
        elif choice == "2":

            customers = customer.get_all_customers()

            print("\nCustomer List")
            print("-" * 40)

            if not customers:

                print("No customers found.")

            else:

                for row in customers:

                    print(
                        f"ID : {row[0]} | "
                        f"Name : {row[1]} | "
                        f"Mobile : {row[2]}"
                    )

        # -------------------------------
        # Add Udhar
        # -------------------------------
        elif choice == "3":

            try:

                customer_id = int(input("Customer ID : "))
                amount = float(input("Amount : "))
                item = input("Item Name : ")
                note = input("Note : ")

                message = transaction.add_udhar(
                    customer_id,
                    amount,
                    item,
                    note
                )

                print("\n", message)

            except Exception as e:

                print("\n", e)

        # -------------------------------
        # Add Payment
        # -------------------------------
        elif choice == "4":

            try:

                customer_id = int(input("Customer ID : "))
                amount = float(input("Amount : "))
                note = input("Note : ")

                message = transaction.add_payment(
                    customer_id,
                    amount,
                    note
                )

                print("\n", message)

            except Exception as e:

                print("\n", e)

        # -------------------------------
        # Customer Balance
        # -------------------------------
        elif choice == "5":

            try:

                customer_id = int(input("Customer ID : "))

                balance = transaction.get_balance(
                    customer_id
                )

                print("\nPending Balance : ₹", balance)

            except Exception as e:

                print("\n", e)

        # -------------------------------
        # Exit
        # -------------------------------
        elif choice == "0":

            print("\nThank you for using Grocery Voice Udhar Assistant.")
            break

        # -------------------------------
        # Invalid Choice
        # -------------------------------
        else:

            print("\nInvalid Choice.")


if __name__ == "__main__":
    main()