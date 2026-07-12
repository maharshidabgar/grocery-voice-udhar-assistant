class CustomerError(Exception):
    """Base class for customer-related exceptions."""
    pass


class CustomerAlreadyExists(CustomerError):
    """Raised when a customer already exists."""
    pass


class CustomerNotFound(CustomerError):
    """Raised when customer is not found."""
    pass


class InvalidCustomerName(CustomerError):
    """Raised when customer name is invalid."""
    pass