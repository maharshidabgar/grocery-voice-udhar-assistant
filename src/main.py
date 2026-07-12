from database import create_tables
from customer_manager import CustomerManager


def main():

    create_tables()

    customer = CustomerManager()

    print("=" * 45)
    print(" Grocery Voice Udhar Assistant ")
    print("=" * 45)

    while True:

        print("\n1. Add Customer")
        print("2. Show Customers")
        print("3. Exit")

        choice = input("\nEnter Choice : ")

        if choice == "1":

            name = input("Customer Name : ")
            mobile = input("Mobile Number : ")

            try:
                message = customer.add_customer(
                    name,
                    mobile
                )

                print(message)

            except Exception as e:
                print(e)

        elif choice == "2":

            customers = customer.get_all_customers()

            print()

            for row in customers:
                print(row)

        elif choice == "3":

            break

        else:
            print("Invalid Choice")


if __name__ == "__main__":
    main()