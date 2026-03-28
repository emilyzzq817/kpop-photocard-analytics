"""
NLP-based entity extraction for K-pop photocard item titles.
Identifies group names and member names from unstructured Mercari listing titles.
"""

import re
from typing import Optional, Tuple
from .config import GROUP_KEYWORDS, MEMBER_MAP


def identify_group(title: str) -> Optional[str]:
    """Extract K-pop group name from an item title.
    
    Uses keyword matching with padding to avoid partial matches.
    Falls back to member name lookup if no group keyword is found.
    
    Args:
        title: Raw item title string from Mercari listing
        
    Returns:
        Canonical group name or None if unidentified
    """
    t = " " + title.lower() + " "
    
    for group, keywords in GROUP_KEYWORDS.items():
        for kw in keywords:
            if kw in t:
                return group
    
    # Fallback: check member names
    for group, members in MEMBER_MAP.items():
        for member, aliases in members.items():
            for alias in aliases:
                if alias in t:
                    return group
    
    return None


def identify_member(title: str, group: str) -> Optional[str]:
    """Extract member name from an item title given a known group.
    
    Args:
        title: Raw item title string
        group: Canonical group name (from identify_group)
        
    Returns:
        Canonical member name or None if unidentified
    """
    if not group or group not in MEMBER_MAP:
        return None
    
    t = " " + title.lower() + " "
    found = []
    
    for member, aliases in MEMBER_MAP[group].items():
        for alias in aliases:
            if alias in t:
                found.append(member)
                break
    
    if len(found) == 1:
        return found[0]
    if len(found) > 1:
        return found[0]  # Take first match (usually the primary subject)
    
    return None


def parse_title(title: str) -> Tuple[Optional[str], Optional[str]]:
    """Parse a Mercari item title to extract group and member.
    
    Args:
        title: Raw item title string
        
    Returns:
        Tuple of (group_name, member_name), either may be None
    """
    group = identify_group(title)
    member = identify_member(title, group) if group else None
    return group, member


def extract_item_type(title: str) -> str:
    """Classify the type of item from the title.
    
    Returns one of: 'photocard', 'album', 'merch', 'set', 'other'
    """
    t = title.lower()
    
    if any(kw in t for kw in ["photocard", " pc ", " pc,", " pob", "pob ", "fansign"]):
        return "photocard"
    if any(kw in t for kw in ["album", "ver.", "version"]):
        return "album"
    if any(kw in t for kw in ["merch", "lightstick", "plush", "poster", "keychain"]):
        return "merch"
    if any(kw in t for kw in [" set", "set "]):
        return "set"
    
    return "other"
