from database import create_tables


def main():
    create_tables()

    print("=" * 50)
    print(" Grocery Voice Udhar Assistant ")
    print("=" * 50)

    print("Database Created Successfully")


if __name__ == "__main__":
    main()