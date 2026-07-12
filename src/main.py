from database import create_tables
from customer_manager import CustomerManager
from transaction_manager import TransactionManager


def main():

    create_tables()

    customer = CustomerManager()
    transaction = TransactionManager()

    print("=" * 55)
    print("      Grocery Voice Udhar Assistant")
    print("=" * 55)

    while True:

        print("\n========== Customer ==========")
        print("1. Add Customer")
        print("2. Show Customers")

        print("\n======== Transactions ========")
        print("3. Add Udhar")
        print("4. Add Payment")
        print("5. Customer Balance")
        print("6. Customer Ledger")
        print("7. Today's Report")

        print("\n==============================")
        print("0. Exit")

        choice = input("\nEnter Choice : ").strip()

        # ======================================
        # 1. Add Customer
        # ======================================

        if choice == "1":

            name = input("Customer Name : ").strip()
            mobile = input("Mobile Number : ").strip()

            try:

                message = customer.add_customer(
                    name,
                    mobile
                )

                print("\n" + message)

            except Exception as e:

                print("\nError :", e)

        # ======================================
        # 2. Show Customers
        # ======================================

        elif choice == "2":

            customers = customer.get_all_customers()

            print("\n========== Customer List ==========\n")

            if not customers:

                print("No customers found.")

            else:

                for row in customers:

                    print(
                        f"ID : {row[0]} | "
                        f"Name : {row[1]} | "
                        f"Mobile : {row[2]}"
                    )


        # ======================================
        # 3. Add Udhar
        # ======================================

        elif choice == "3":

            try:

                customer_id = int(input("Customer ID : "))
                amount = float(input("Amount : "))
                item = input("Item Name : ").strip()
                note = input("Note : ").strip()

                message = transaction.add_udhar(
                    customer_id,
                    amount,
                    item,
                    note
                )

                print("\n" + message)

            except ValueError:

                print("\nInvalid amount or customer ID.")

            except Exception as e:

                print("\nError :", e)

        # ======================================
        # 4. Add Payment
        # ======================================

        elif choice == "4":

            try:

                customer_id = int(input("Customer ID : "))
                amount = float(input("Amount : "))
                note = input("Note : ").strip()

                message = transaction.add_payment(
                    customer_id,
                    amount,
                    note
                )

                print("\n" + message)

            except ValueError:

                print("\nInvalid amount or customer ID.")

            except Exception as e:

                print("\nError :", e)


                    # ======================================
        # 5. Customer Balance
        # ======================================

        elif choice == "5":

            try:

                customer_id = int(input("Customer ID : "))

                balance = transaction.get_balance(customer_id)

                print("\n" + "=" * 40)
                print(f"Pending Balance : ₹ {balance:.2f}")
                print("=" * 40)

            except ValueError:

                print("\nInvalid Customer ID.")

            except Exception as e:

                print("\nError :", e)

        # ======================================
        # 6. Customer Ledger
        # ======================================

        elif choice == "6":

            try:

                customer_id = int(input("Customer ID : "))

                ledger = transaction.get_customer_ledger(customer_id)

                print("\n========== CUSTOMER LEDGER ==========\n")

                if not ledger:

                    print("No transactions found.")

                else:

                    for row in ledger:

                        print("-" * 60)
                        print(f"Transaction ID : {row[0]}")
                        print(f"Type           : {row[1]}")
                        print(f"Amount         : ₹ {row[2]}")
                        print(f"Item           : {row[3]}")
                        print(f"Note           : {row[4]}")
                        print(f"Date           : {row[5]}")

                    print("-" * 60)

            except ValueError:

                print("\nInvalid Customer ID.")

            except Exception as e:

                print("\nError :", e)

        # ======================================
        # 7. Today's Report
        # ======================================

        elif choice == "7":

            try:

                report = transaction.get_today_transactions()

                print("\n========== TODAY'S REPORT ==========\n")

                if not report:

                    print("No transactions today.")

                else:

                    for row in report:

                        print("-" * 60)
                        print(f"Customer ID : {row[0]}")
                        print(f"Type        : {row[1]}")
                        print(f"Amount      : ₹ {row[2]}")
                        print(f"Item        : {row[3]}")
                        print(f"Note        : {row[4]}")
                        print(f"Date        : {row[5]}")

                    print("-" * 60)

            except Exception as e:

                print("\nError :", e)


                    # ======================================
        # 0. Exit
        # ======================================

        elif choice == "0":

            print("\nThank you for using Grocery Voice Udhar Assistant.")
            break

        # ======================================
        # Invalid Choice
        # ======================================

        else:

            print("\nInvalid Choice! Please try again.")


if __name__ == "__main__":
    main()

   