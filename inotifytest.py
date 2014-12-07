import subprocess
cmdtest = "inotifywait -e create -mrq /home/gardneli/test"
p = subprocess.Popen(cmdtest, shell=True, stderr=subprocess.PIPE)
while True:
	out = p.stderr.read(1)
	if out != '':
		sys.stdout.write(out)
		sys.stdout.flush()
