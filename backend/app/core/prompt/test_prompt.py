class ExamplePrompt:
    """
    Class for constructing the test prompt.
    """

    @staticmethod
    def construct(question: str) -> str:
        """
        Construct the prompt for the LLM.
        """
        return (
            f"""{question}
            """
        )
