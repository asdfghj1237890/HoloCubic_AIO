#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generate a safe 1000-character set by removing CMD special characters
生成安全的 1000 字符集（移除 CMD 特殊字符）
"""

# Read original characters
with open('tc_important_1000.txt', 'r', encoding='utf-8') as f:
    original_chars = f.read()

# Remove CMD special characters that cause issues
# Keep ASCII letters, digits, and safe punctuation
unsafe_chars = '<>|&^%'
safe_chars = []

for char in original_chars:
    if char not in unsafe_chars:
        safe_chars.append(char)

# Add back these characters as Unicode escapes if needed in the actual font
# But for now, let's just exclude them from the command line

safe_charset = ''.join(safe_chars)

# Save safe charset
with open('tc_safe_1000.txt', 'w', encoding='utf-8') as f:
    f.write(safe_charset)

print("="*70)
print("Generated Safe Character Set")
print("="*70)
print(f"\nOriginal characters: {len(original_chars)}")
print(f"Removed unsafe CMD chars: {len(original_chars) - len(safe_charset)}")
print(f"Safe characters: {len(safe_charset)}")
print(f"\nRemoved characters: {unsafe_chars}")
print(f"\nSaved to: tc_safe_1000.txt")

# Count breakdown
ascii_count = sum(1 for c in safe_charset if ord(c) < 128)
chinese_count = sum(1 for c in safe_charset if ord(c) >= 0x4e00 and ord(c) <= 0x9fff)
other_count = len(safe_charset) - ascii_count - chinese_count

print(f"\nBreakdown:")
print(f"  ASCII: {ascii_count}")
print(f"  Chinese: {chinese_count}")
print(f"  Other: {other_count}")
print(f"  Total: {len(safe_charset)}")
print("="*70)

