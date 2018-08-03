import subprocess
import tempfile

with tempfile.TemporaryFile() as tempf:
    proc = subprocess.Popen(['echo', 'a', 'b'], stdout=tempf)
    proc.wait()
    tempf.seek(0)
    print tempf.read()

"""
import subprocess
import tempfile

with tempfile.TemporaryFile() as tempf:
    proc = subprocess.Popen(['cd', '/home/robert/Documents/workspace/polaris/ros', '&&', './jetson'], stdout=tempf)
    proc.wait()
    tempf.seek(0)
    print tempf.read()
"""