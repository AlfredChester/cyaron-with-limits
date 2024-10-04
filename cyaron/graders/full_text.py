import hashlib
from .grader_registry import CYaRonGraders
from .mismatch import HashMismatch


@CYaRonGraders.grader("FullText")
def full_text(content, std):
    content_hash = hashlib.sha256(content.encode("utf-8")).hexdigest()
    std_hash = hashlib.sha256(std.encode("utf-8")).hexdigest()
    return (
        (True, None)
        if content_hash == std_hash
        else (False, HashMismatch(content, std, content_hash, std_hash))
    )
