class ExamplePrompt:
    """
    Class for constructing the test prompt.
    """

    @staticmethod
    def construct(question: str, expected_answer: str, user_answer: str) -> str:
        """
        Construct the prompt for the LLM.
        """
        return (
            f"""test prompt
            """
        )
