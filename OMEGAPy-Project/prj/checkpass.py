from hashlib import sha256
import sys
from project_manager import passwd 
sha = sha256(str(f"{sys.argv[1]}" + 'OmegapyNotFound').encode()).hexdigest()
if sha == passwd():
    print("true")
else:
    print("false")
