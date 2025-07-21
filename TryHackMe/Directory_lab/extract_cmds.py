#!/usr/bin/env python3
import sys
import base64
import re
from pathlib import Path

def extract_and_decode_arguments(xml_path: str, output_folder: str):
    xml_content = Path(xml_path).read_text()

    # Find all commands with <rsp:Arguments>...</rsp:Arguments>
    base64_blobs = re.findall(r"<rsp:Arguments>(.*?)</rsp:Arguments>", xml_content, re.DOTALL)

    # Make sure there are commands if none are found, there may be an issue with the file
    if not base64_blobs:
        print("[-] No <rsp:Arguments> Base64 blobs found.")
        return

    # Create an output_folder if needed
    Path(output_folder).mkdir(parents=True, exist_ok=True)

    # Loop through all commands and decode them
    for idx, blob in enumerate(base64_blobs, 1):
        try:
            # Clean any newlines or spaces
            cleaned = blob.strip().replace("\n", "")

            # Base64 decode
            decoded = base64.b64decode(cleaned)

            decoded_text = decoded.decode("utf-8", errors="replace")

            # Store full XML
            out_path = Path(output_folder) / f"command_xml_{idx:02}.txt"
            out_path.write_text(decoded_text, encoding="utf-8")

            # Extract the given command out of the XML
            match = re.search(r'<S N="V">(.+?)</S>', decoded_text, re.DOTALL)
            if match:
                command_only = match.group(1).strip()
            else:
                command_only = "[Could not extract command]"

            out_path = Path(output_folder) / f"command_{idx:02}.txt"
            out_path.write_text(command_only, encoding="utf-8")

            print(f"[+] Extracted and saved command_{idx:02}.txt")
        except Exception as e:
            print(f"[!] Failed to decode blob {idx}: {e}")

# Usage extract_cmds.py winrm_decrypted.xml decoded_commands
if len(sys.argv) != 3:
    print("Usage: extract_cmds.py <xml_path> <output_folder> ")
else:
    extract_and_decode_arguments(sys.argv[1], sys.argv[2])
