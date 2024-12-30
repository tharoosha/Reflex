import pytest
from ..core.services.testing_chat import TestService

@pytest.fixture
def test_service():
    """
    Fixture to initialize the TestService object for testing.
    """
    return TestService()

def test_service_with_custom_input(test_service):
    """
    Test the TestService with customer input.
    """
    # Define a customer input variable
    customer_input = "What is the capital of Japan?"
    
    # Call the testing method
    response = test_service.testing(customer_input)
    
    # Assert that the response is not None
    assert response is not None, "Response should not be None"
    
    # Print the response for manual validation
    print(f"Input: {customer_input}")
    print(f"Response: {response}")
