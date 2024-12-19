import difflib


def search_query_in_texts(first_text: str, second_text: str) -> list[dict]:
    """
    Search for a query text in two given texts and return differences.
    
    Args:
        first_text (str): First text to search in
        second_text (str): Second text to search in
        
    Returns:
        list[dict]: List of dictionaries containing differences, where each dict has
                   'first_doc' and 'second_doc' keys with corresponding sentences
    """
    # Generate a unified diff
    diff = difflib.unified_diff(
        first_text.splitlines(), 
        second_text.splitlines(), 
        lineterm="\n", 
        fromfile="first_text",
        tofile="second_text"
    )
    
    differences = []
    current_pair = {"first_text": None, "second_text": None}
    for line in diff:
        if line.startswith('-'):
            current_pair["first_text"] = line[1:].strip()
        elif line.startswith('+'):
            current_pair["second_text"] = line[1:].strip()
            if current_pair["first_text"] is not None:
                differences.append(current_pair.copy())
                current_pair = {"first_text": None, "second_text": None}
    
    if len(differences) > 1:
        return differences[1:]
    else:
        return []
