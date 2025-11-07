"""
File Organizer Module

This module provides functions to automate file organization tasks such as:
- Organizing files in a directory by file type
- Renaming files in bulk
- Finding and removing duplicate files
- Cleaning up temporary files
"""

import os
import shutil
from pathlib import Path
from datetime import datetime
import hashlib
import logging
from typing import List, Dict, Set, Optional

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler('file_organizer.log')
    ]
)
logger = logging.getLogger(__name__)

# Common file types and their corresponding folders
FILE_TYPES = {
    'images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg', '.webp'],
    'documents': ['.pdf', '.doc', '.docx', '.txt', '.rtf', '.odt', '.xls', '.xlsx', '.ppt', '.pptx'],
    'archives': ['.zip', '.rar', '.7z', '.tar', '.gz'],
    'audio': ['.mp3', '.wav', '.ogg', '.m4a'],
    'video': ['.mp4', '.avi', '.mov', '.mkv', '.wmv', '.flv'],
    'code': ['.py', '.js', '.html', '.css', '.java', '.c', '.cpp', '.h', '.sh'],
    'data': ['.json', '.csv', '.xml', '.db', '.sqlite'],
}

def organize_downloads(downloads_path: str = None) -> None:
    """
    Organize files in the Downloads folder into subdirectories based on file types.
    
    Args:
        downloads_path: Path to the Downloads directory. If None, uses the default Downloads folder.
    """
    if downloads_path is None:
        # Default to user's Downloads folder
        downloads_path = str(Path.home() / 'Downloads')
    
    downloads = Path(downloads_path)
    
    if not downloads.exists():
        logger.error(f"Directory not found: {downloads}")
        return
    
    logger.info(f"Organizing files in: {downloads}")
    
    # Create category directories if they don't exist
    for category in FILE_TYPES.keys():
        (downloads / category).mkdir(exist_ok=True)
    
    # Other files will go here
    (downloads / 'other').mkdir(exist_ok=True)
    
    # Move files to appropriate directories
    for item in downloads.iterdir():
        if item.is_file() and not item.name.startswith('.'):
            file_ext = item.suffix.lower()
            moved = False
            
            # Find the appropriate category
            for category, extensions in FILE_TYPES.items():
                if file_ext in extensions:
                    dest = downloads / category / item.name
                    safe_move(item, dest)
                    moved = True
                    break
            
            # If file type not in our categories, move to 'other'
            if not moved:
                dest = downloads / 'other' / item.name
                safe_move(item, dest)
    
    logger.info("File organization complete!")

def safe_move(src: Path, dest: Path) -> None:
    """Safely move a file, handling name conflicts."""
    if not src.exists():
        return
        
    if dest.exists():
        # If file exists, add timestamp to filename
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        new_name = f"{dest.stem}_{timestamp}{dest.suffix}"
        dest = dest.with_name(new_name)
    
    try:
        shutil.move(str(src), str(dest))
        logger.info(f"Moved: {src.name} -> {dest}")
    except Exception as e:
        logger.error(f"Error moving {src}: {e}")

def find_duplicates(directory: str) -> Dict[str, List[str]]:
    """
    Find duplicate files in a directory based on file content hash.
    
    Args:
        directory: Path to the directory to search for duplicates
        
    Returns:
        Dictionary with file hashes as keys and lists of duplicate file paths as values
    """
    hashes = {}
    
    for root, _, files in os.walk(directory):
        for filename in files:
            file_path = Path(root) / filename
            try:
                file_hash = get_file_hash(file_path)
                if file_hash in hashes:
                    hashes[file_hash].append(str(file_path))
                else:
                    hashes[file_hash] = [str(file_path)]
            except (IOError, OSError) as e:
                logger.error(f"Error reading {file_path}: {e}")
    
    # Filter to only include duplicates
    return {k: v for k, v in hashes.items() if len(v) > 1}

def get_file_hash(file_path: Path, block_size: int = 65536) -> str:
    """Generate a hash for a file to detect duplicates."""
    hasher = hashlib.sha256()
    
    with open(file_path, 'rb') as f:
        buf = f.read(block_size)
        while len(buf) > 0:
            hasher.update(buf)
            buf = f.read(block_size)
    
    return hasher.hexdigest()

def clean_empty_directories(directory: str) -> None:
    """Recursively remove empty directories."""
    directory = Path(directory)
    
    for item in directory.iterdir():
        if item.is_dir():
            clean_empty_directories(item)
    
    # Remove if directory is empty
    try:
        if directory.is_dir() and not any(directory.iterdir()):
            directory.rmdir()
            logger.info(f"Removed empty directory: {directory}")
    except OSError as e:
        logger.error(f"Error removing directory {directory}: {e}")

if __name__ == "__main__":
    # Example usage
    print("=== Python File Organizer ===")
    print("1. Organize Downloads folder")
    print("2. Find duplicate files")
    print("3. Clean empty directories")
    
    choice = input("Enter your choice (1-3): ")
    
    if choice == "1":
        path = input("Enter directory path (leave empty for Downloads): ").strip()
        if not path:
            organize_downloads()
        else:
            organize_downloads(path)
    elif choice == "2":
        path = input("Enter directory to scan for duplicates: ").strip()
        if path:
            duplicates = find_duplicates(path)
            if duplicates:
                print("\nFound duplicate files:")
                for file_hash, files in duplicates.items():
                    print(f"\nHash: {file_hash[:8]}...")
                    for file_path in files:
                        print(f"  - {file_path}")
            else:
                print("No duplicate files found.")
    elif choice == "3":
        path = input("Enter directory to clean (leave empty for current directory): ").strip()
        if not path:
            path = "."
        clean_empty_directories(path)
        print("Cleaning complete!")
    else:
        print("Invalid choice. Please try again.")
