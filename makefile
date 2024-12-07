padded = $(shell printf "day%02d" $(day))

.PHONY: run test help

run:
	@python3.12 main/$(padded).py

test:
	@python3.12 -m tests.$(padded)

profile:
	@python3.12 -m cProfile -s cumulative main/$(padded).py

help:
	@echo "Usage:"
	@echo "  make run day=<day number>      # Run main file for the given day"
	@echo "  make test day=<day number>     # Run test file for the given day"
	@echo "  make profile day=<day number>  # Run code profiling for the given day"
	@echo "Examples:"
	@echo "  make run day=1"
	@echo "  make test day=1"
	@echo "  make profile day=1"
