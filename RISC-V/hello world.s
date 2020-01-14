.data
	my_text:	.asciiz "Hello World!\n"
	str1:		.byte 104, 101, 108, 108, 111, 32, 119, 111, 114, 108, 100, 33, 10, 0
.text
	# Printing string
	la a1, my_text
	addi a0, x0, 4
	ecall
	# Exit
	add		a1, x0, x0
	addi	a0, x0, 10
	ecall
