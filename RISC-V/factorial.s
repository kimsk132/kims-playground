Main:
	addi	a0, x0, 8		# Put function argument in a0
	jal		ra, Factorial 	# call Factorial
	jal		ra, PrintInt	# Print the result of Factorial
Exit:
	add		a1, x0, x0		# Set a1 = 0 to use as exit code
	addi	a0, x0, 10		# Set a0 = 10. ecall code 10 means exiting the program
	ecall

# Function Print Int
PrintInt:
	addi	a1, a0, 0		# Put the number we want to print in a1
	addi	a0, x0, 1		# Set a0 = 1. ecall code 1 means print integer
	ecall
	jalr	ra				# Return

# Function Factorial (iterative)
Factorial:
	add		a1, a0, x0		# Set a1 = a0
Loop:
	addi	a1, a1, -1		# Decrement a1
	beq		a1, x0, Done	# If a1 = 0, we're done
	mul		a0, a0, a1		# a0 = a0 * a1
	jal		x0, Loop		# go to Loop
Done:
	jalr	ra				# Return

# Function Factorial (recursive)
RecFactorial:
	# Save registers
	addi	sp, sp, -8		# Allocate 2 words on the stack
	sw		ra, 0(sp)		# Push RA on the stack
	sw		s0, 4(sp)		# Push s0 on the stack
	# Start function
	# Base case
	addi	s0, x0, 1		# Set s0 = 1
	beq		a0, s0, rDone 	# If a0 = 1 then we're done. Factorial of 1 is 1.
	# Recursive case
	add		s0, a0, x0		# Set s0 = a0
	addi	a0, a0, -1		# Decrement a0
	jal 	ra, RecFactorial # Recursive call RecFactorial
	mul		a0, a0, s0		# Set a0 = a0 * s0. This is our return value
rDone:
	lw		ra, 0(sp)		# Pop RA from stack
	lw		s0, 4(sp)		# Pop s0 from stack
	addi	sp, sp, 8		# Free 2 words from stack
	jalr	ra				# Return
