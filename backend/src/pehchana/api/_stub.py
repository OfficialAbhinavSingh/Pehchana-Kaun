from fastapi import HTTPException, status


def not_implemented(owner: str) -> HTTPException:
    """Placeholder for endpoints whose contract is fixed but body isn't built yet."""
    return HTTPException(status.HTTP_501_NOT_IMPLEMENTED, detail=f"not implemented yet ({owner})")
