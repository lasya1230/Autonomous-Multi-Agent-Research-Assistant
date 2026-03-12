from typing import List


def chunk_text(text: str, chunk_size: int = 200, overlap: int = 50) -> List[str]:
    """
    Split text into chunks while preserving full words.
    This prevents cutting words like 'predictive' into 'pre' and 'dictive'.
    """

    if not text or not text.strip():
        return []

    words = text.split()
    chunks = []
    current_chunk = []
    current_length = 0

    for word in words:
        word_length = len(word) + 1  # account for space

        if current_length + word_length <= chunk_size:
            current_chunk.append(word)
            current_length += word_length
        else:
            # Save current chunk
            chunks.append(" ".join(current_chunk))

            # Apply overlap using last few words
            overlap_words = current_chunk[-10:] if len(current_chunk) > 10 else current_chunk

            current_chunk = overlap_words + [word]
            current_length = sum(len(w) + 1 for w in current_chunk)

    if current_chunk:
        chunks.append(" ".join(current_chunk))

    return chunks