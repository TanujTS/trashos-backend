from fastapi import HTTPException, UploadFile, File, status
from pathlib import Path

TEMP_DIR = Path("temp")
MAX_FILE_SIZE=10*1024*1024
ALLOWED_EXTENSIONS = {".jpg", ".jpeg", ".png",".webp"}
ALLOWED_MIME_TYPES = {
    "image/jpeg", 
    "image/jpg", 
    "image/png", 
    "image/webp"
}

TEMP_DIR.mkdir(exist_ok=True)

def validate_image_file(file: UploadFile) -> None:
    """Validate uploaded image file"""
    if file.size and file.size > MAX_FILE_SIZE:
        raise HTTPException(
            status_code=status.HTTP_413_REQUEST_ENTITY_TOO_LARGE,
            detail="File size exceeds maximum allowed size of 10MB"
        )
    
    if file.content_type not in ALLOWED_MIME_TYPES:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid file type. Only image files are allowed"
        )
    
    if file.filename:
        file_extension = Path(file.filename).suffix.lower()
        if file_extension not in ALLOWED_EXTENSIONS:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Invalid file extension. Only jpg, png, gif, webp files are allowed"
            )
        

