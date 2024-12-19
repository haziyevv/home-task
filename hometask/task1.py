from difflib import SequenceMatcher

def search_query_in_texts(text1: str, text2: str, query: str, similarity_threshold: float = 0.9) -> bool:
    """
    Search for a query text in two given texts with approximate matching.
    
    Args:
        text1 (str): First text to search in
        text2 (str): Second text to search in
        query (str): Query text to search for
        similarity_threshold (float): Minimum similarity ratio (0.0 to 1.0) to consider a match
        
    Returns:
        bool: True if query exists in both texts with similarity >= threshold, False otherwise
    """
    def find_best_match_ratio(text: str, query: str) -> float:
        # Convert to lowercase for case-insensitive comparison
        text = text.lower()
        query = query.lower()
        
        # Split text into words
        words = text.split()
        
        # Find the best matching ratio among all possible word combinations
        best_ratio = 0
        query_words = len(query.split())
        
        for i in range(len(words)):
            # Take chunks of text the same length as the query
            text_chunk = ' '.join(words[i:i + query_words])
            ratio = SequenceMatcher(None, text_chunk, query).ratio()
            best_ratio = max(best_ratio, ratio)
            
        return best_ratio
    
    # Find best match ratios for both texts
    ratio1 = find_best_match_ratio(text1, query)
    ratio2 = find_best_match_ratio(text2, query)
    
    # Return True if both texts have matches above the threshold
    return ratio1 >= similarity_threshold and ratio2 >= similarity_threshold, ratio1, ratio2

