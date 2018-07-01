"Mini script for opening google files (.gdoc, .gsheet, .gform)."

import json
import subprocess
import sys

if __name__ == "__main__":
    file = sys.argv[1]

    with open(file) as j:
        j = json.loads(j.read())
        url = j['url']
        subprocess.Popen(['open', url])
