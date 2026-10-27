image:
	docker build -t cboard/cboard .

run:
	docker run -p 5000:3000 cboard/cboard:latest
# Local security scan in a throwaway Incus container (replaces CodeQL).
# Use SAST_ARGS=--vm for a virtual machine instead.
sast:
	scripts/sast/run-in-incus.sh $(SAST_ARGS)

.PHONY: image run sast
