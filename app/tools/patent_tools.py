def search_patents(query: str) -> dict:
    """
    Search for patents related to a technology or keyword.

    Args:
        query: Search query (e.g "transformer neural networks" or "US10123456")

    Returns:
        Dictionary containing mock patent search results.
    """
    return {
        "query": query,
        "results": [
            {
                "patent_id": "US10123456B2",
                "title": "Attention-based Neural Network Architecture",
                "abstract": "A system for processing sequential data using multi-head attention...",
                "assignee": "Example Corp",
                "year": 2023,
            },
            {
                "patent_id": "US10987654A1",
                "title": "Efficient Transformer Training Method",
                "abstract": "Method for reducing computational cost of training large transformers...",
                "assignee": "Another Inc",
                "year": 2024,
            },
        ],
    }
