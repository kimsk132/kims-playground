.data
	# Strings for testing
	# "Hello World!"
	str1:		.byte 72, 101, 108, 108, 111, 32, 87, 111, 114, 108, 100, 33, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
	# "words,dwords"
	str3:		.byte 119, 111, 114, 100, 115, 44, 100, 119, 111, 114, 100, 115, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
	# {'b','y','t','e','s',0,'&','&','&','&','&','&','&','&','&',0}
	str4:		.byte 98, 121, 116, 101, 115, 0, 38, 38, 38, 38, 38, 38, 38, 38, 38, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
	# {'1','2','3','4','5','6','7',0,'Z','Z','Z','Z','Z','Z','Z','Z','Z',0}
	str5:		.byte 49, 50, 51, 52, 53, 54, 55, 0, 90, 90, 90, 90, 90, 90, 90, 90, 90, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
	# {'A','B','C',0,'X','X','X','X','X','X','X','X','X','X','X','X',0}
	str6:		.byte 65, 66, 67, 0, 88, 88, 88, 88, 88, 88, 88, 88, 88, 88, 88, 88, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
	# {'h','e','l','l','o',0,'@','@','@','@','@','@','@','@','@',0}
	str7:		.byte 104, 101, 108, 108, 111, 0, 64, 64, 64, 64, 64, 64, 64, 64, 64, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
	# {' ','P','a','t',0,'@','@','@','@','@','@','@','@','@',0}
	str8:		.byte 32, 80, 97, 116, 0, 64, 64, 64, 64, 64, 64, 64, 64, 64, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
	# { 'Y','o','u',' ','s','h','o','u','l','d',' ','e','f','f','i','c','i','e','n','t',' ','c','o','d','e',0,'@','@','@','@','@','@','@','@','@',0 }
	str10:		.byte 89, 111, 117, 32, 115, 104, 111, 117, 108, 100, 32, 101, 102, 102, 105, 99, 105, 101, 110, 116, 32, 99, 111, 100, 101, 0, 64, 64, 64, 64, 64, 64, 64, 64, 64, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
	# { 'w','r','i','t','e',' ',0,'@','@','@','@','@','@','@','@','@',0 }
	str11:		.byte 119, 114, 105, 116, 101, 32, 0, 64, 64, 64, 64, 64, 64, 64, 64, 64, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
	# {'C','o','m','m','e','n','t','s',' ','h','e','l','p',' ','h','e','l','p',' ','m','a','k','e',' ','y','o','u','r',' ','c','o','d','e',' ','u','n','d','e','r','s','t','a','n','d','a','b','l','e','.',0,'@','@','@','@','@','@',0}
	str12:		.byte 67, 111, 109, 109, 101, 110, 116, 115, 32, 104, 101, 108, 112, 32, 104, 101, 108, 112, 32, 109, 97, 107, 101, 32, 121, 111, 117, 114, 32, 99, 111, 100, 101, 32, 117, 110, 100, 101, 114, 115, 116, 97, 110, 100, 97, 98, 108, 101, 46, 0, 64, 64, 64, 64, 64, 64, 0, 0, 0, 0
	# {'l','u','l','l','a',0,'@','@','@','@','@','@','@','@',0}
	str13:		.byte 108, 117, 108, 108, 97, 0, 64, 64, 64, 64, 64, 64, 64, 64, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
	# {'S','i','n','g',' ','a',' ',0,'@','@','@','@','@','@',0}
	str14:		.byte 83, 105, 110, 103, 32, 97, 32, 0, 64, 64, 64, 64, 64, 64, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
	# {'A','r','n','o','l','d',0,'@','@','@','@','@','@',0}
	str15:		.byte 65, 114, 110, 111, 108, 100, 0, 64, 64, 64, 64, 64, 64, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
	# {'W','h','o',' ','s','a','i','d',' ','I','\'','l','l',' ','b','e',' ','b','a','c','k','?',0,'@','@','@','@',0}
	str16:		.byte 87, 104, 111, 32, 115, 97, 105, 100, 32, 73, 39, 108, 108, 32, 98, 101, 32, 98, 97, 99, 107, 63, 0, 64, 64, 64, 64, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
	# {'T','a','y','l','o','r',' ','S','w','i','f','t',' ','i','s',' ','a',' ','g','o','o','d',' ','c','o','u','n','t','r','y',' ','s','i','n','g','e','r','.',0,'@','@','@','@',0}
	str17:		.byte 84, 97, 121, 108, 111, 114, 32, 83, 119, 105, 102, 116, 32, 105, 115, 32, 97, 32, 103, 111, 111, 100, 32, 99, 111, 117, 110, 116, 114, 121, 32, 115, 105, 110, 103, 101, 114, 46, 0, 64, 64, 64, 64, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
	# {'v','e','r','y',' ',0,'@','@','@','@','@','@',0}
	str18:		.byte 118, 101, 114, 121, 32, 0, 64, 64, 64, 64, 64, 64, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
	# { 'A','s','s','e','m','b','l','y',' ','i','s',' ','m','a','g','i','c','a','l',0,'#','#','#','#','#','#',0 }
	str19:		.byte 65, 115, 115, 101, 109, 98, 108, 121, 32, 105, 115, 32, 109, 97, 103, 105, 99, 97, 108, 0, 35, 35, 35, 35, 35, 35, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
	# { 'P','a','r','t','y','i','n','g',' ','i','s',' ','f','u','n',0,'#','#','#','#','#','#',0 }
	str20:		.byte 80, 97, 114, 116, 121, 105, 110, 103, 32, 105, 115, 32, 102, 117, 110, 0, 35, 35, 35, 35, 35, 35, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0

	# String prompts
	endl:		.asciiz "\n"
	prompt1:	.asciiz "After trying to copy 8 chars from str19 to str20, str20 contains"
	prompt2:	.asciiz "After trying to copy 400 chars from str16 to str15, str15 contains"
	prompt3:	.asciiz "Before copying to str3, str3 contains"
	prompt4:	.asciiz "After trying to copy 5 chars from str4 to str3, str3 contains"
	prompt5:	.asciiz "After trying to copy 8 chars from str5 to str3, str3 contains"
	prompt6:	.asciiz "After trying to copy 400 chars from str6 to str3, str3 contains"
	prompt7:	.asciiz "After appending str8 to str7, str7 contains"
	prompt8:	.asciiz "Before removing 5 characters from str12, str12 contains"
	prompt9:	.asciiz "After removing 5 characters from str12 starting at index 9, str12 contains"
	prompt10:	.asciiz "Before inserting str11 into str10, str10 contains"
	prompt11:	.asciiz "After inserting str11 into str10 at index 11, str10 contains"

.text

Main:
	la		a0, str1 # Hello World!
	jal 	PrintLine
	la 		a0, prompt1 # After trying to copy 8 chars from str19 to str20, str20 contains
	jal 	PrintLine
	# Perform the corresponding copy
	la 		a0, str20
	la 		a1, str19
	addi 	a2, x0, 8
	jal 	StrNCpyAsm
	# Print the result
	la 		a0, str20
	jal 	PrintLine
	# Next question
	la 		a0, prompt2 # After trying to copy 400 chars from str16 to str15, str15 contains
	jal 	PrintLine
	# Perform the corresponding copy
	la 		a0, str15
	la 		a1, str16
	addi 	a2, x0, 400
	jal 	StrNCpyAsm
	# Print the result
	la 		a0, str15
	jal 	PrintLine
	# Next question
	la 		a0, prompt3 # Before copying to str3, str3 contains
	jal 	PrintLine
	# Perform the corresponding Print
	la 		a0, str3
	jal 	PrintLine
	# Next question
	la 		a0, prompt4 # After trying to copy 5 chars from str4 to str3, str3 contains
	jal 	PrintLine
	# Perform the corresponding copy
	la 		a0, str3
	la 		a1, str4
	addi 	a2, x0, 5
	jal 	StrNCpyAsm
	# Print the result
	la 		a0, str3
	jal 	PrintLine
	# Next question
	la 		a0, prompt5 # After trying to copy 8 chars from str5 to str3, str3 contains
	jal 	PrintLine
	# Perform the corresponding copy
	la 		a0, str3
	la 		a1, str5
	addi 	a2, x0, 8
	jal 	StrNCpyAsm
	# Print the result
	la 		a0, str3
	jal 	PrintLine
	# Next question
	la 		a0, prompt6 # After trying to copy 400 chars from str6 to str3, str3 contains
	jal 	PrintLine
	# Perform the corresponding copy
	la 		a0, str3
	la 		a1, str6
	addi 	a2, x0, 400
	jal 	StrNCpyAsm
	# Print the result
	la 		a0, str3
	jal 	PrintLine
	# Next question
	la 		a0, prompt7 # After appending str8 to str7, str7 contains
	jal 	PrintLine
	# Perform the corresponding append
	la 		a0, str7
	la 		a1, str8
	jal 	StrCatAsm
	# Print the result
	la 		a0, str7
	jal 	PrintLine
	# Next question
	la 		a0, prompt8 # Before removing 5 characters from str12, str12 contains
	jal 	PrintLine
	# Perform the corresponding Print
	la 		a0, str12
	jal 	PrintLine
	# Next question
	la 		a0, prompt9 # After removing 5 characters from str12 starting at index 9, str12 contains
	jal 	PrintLine
	# Perform the corresponding remove
	la 		a0, str12
	addi 	a1, x0, 9
	addi 	a2, x0, 5
	jal 	StrRemove
	# Print the result
	la 		a0, str12
	jal 	PrintLine
	# Next question
	la 		a0, prompt10 # Before inserting str11 into str10, str10 contains
	jal 	PrintLine
	# Perform the corresponding Print
	la 		a0, str10
	jal 	PrintLine
	# Next question
	la 		a0, prompt11 # After inserting str11 into str10 at index 11, str10 contains
	jal 	PrintLine
	# Perform the corresponding insert
	la 		a0, str10
	la  	a1, str11
	addi 	a2, x0, 11
	jal 	StrInsertEC
	# Print the result
	la 		a0, str10
	jal 	PrintLine
	
Exit:
	add		a1, x0, x0
	addi	a0, x0, 10
	ecall

# ===========================================================================================
# ===========================================================================================
# ======================================== Functions ========================================
# ===========================================================================================
# ===========================================================================================

# Print string whose address is in a0
PrintStr:
	add 	a1, a0, x0
	addi	a0, x0, 4
	ecall
	jalr	ra

# Print string whose address is in a0 and a newline afterwards
PrintLine:
	add 	a1, a0, x0
	addi 	a0, x0, 4
	ecall
	la 		a1, endl
	addi 	a0, x0, 4
	ecall
	jalr 	ra

# Find the length of zero-terminated string whose address is in a0, not including the terminating zero
StrLenAsm:
	add 	a1, a0, x0 # Move string address to a1
	add 	a0, x0, x0 # Clear a0 to use as accumulator
  StrLenLoopTop:
	lb 		a2, 0(a1) # Load char at a1 into a2
	beq 	a2, x0, StrLenLoopBottom # If the loaded char is zero, then we're done
	addi	a0, a0, 1	# Increment accumulator
	addi 	a1, a1, 1 	# Increment string index
	j 		StrLenLoopTop
  StrLenLoopBottom:
	jalr 	ra

# Copy the zero-terminated string, including the terminating zero, whose address in a1 to address in a0
StrCpyAsm:
  StrCpyLoopTop:
    lb		t0, 0(a1) # Load char from a1 into t0
    sb 		t0, 0(a0) # Put char in t0 into a0
    beq 	t0, x0, StrCpyDone # If the current char is zero, then we're done
    addi 	a0, a0, 1 # Increment a0 index
    addi 	a1, a1, 1 # Increment a1 index
    j 		StrCpyLoopTop
  StrCpyDone:
    jalr 	ra

# Copy a2 chars from string whose address is in a1 to address a0
# If a2 > length of the string, then only copy the string.
# Does not zero-terminate the copied string unless we reach the end of source string
StrNCpyAsm:
  StrNCpyLoopTop:
    beq 	a2, x0, StrNCpyDone # If a2 == 0, then we're done
    lb 		t0, 0(a1) 	# Load char at a1 into t0.
    sb 		t0, 0(a0)	# Store char in t0 at a0
    beq 	t0, x0, StrNCpyDone # If current char is zero, then we're done.
    # Increment the indices, and decrement number of chars to copy
    addi 	a0, a0, 1
    addi 	a1, a1, 1
    addi 	a2, a2, -1
    j 		StrNCpyLoopTop
  StrNCpyDone:
    jalr ra

# Append string whose address in a1 to the end of string whose address in a0
# Puts in the terminating zero after concatenation
StrCatAsm:
    # Save ra so we can call a helper function
    addi 	sp, sp, -4
    sw 		ra, 0(sp)
  # increment a0 until we find its terminationg zero
  StrCatLoopTop:
    lb 		t0, 0(a0) # Load char at a0
    beq 	t0, x0, StrCatLoopDone # If the loaded char is zero, then we've foumd the end
    addi 	a0, a0, 1 # Increment a0
    j 		StrCatLoopTop
  StrCatLoopDone:
	# Copy str in a1 to the address a0
	jal 	StrCpyAsm
	# return
	lw 		ra, 0(sp)
	addi 	sp, sp, 4
	jalr 	ra

# Remove count a2 chars from string whose address in a0 starting at index a1
StrRemove:
	# Save ra so we can call a helper function
    addi 	sp, sp, -4
    sw 		ra, 0(sp)
    add 	a0, a0, a1 # Put a0 at the address to be deleted
    add 	a1, a0, a2 # Put a1 at the address to be deleted + count
	jal 	StrCpyAsm # Call StrCpyAsm
	# return
	lw 		ra, 0(sp)
	addi 	sp, sp, 4
	jalr 	ra

# Insert string1 at a1 into string0 at a0 starting at index a2
StrInsertEC:
	# Save registers so we can call helper functions
    addi 	sp, sp, -20
    sw 		ra, 0(sp)
    sw 		s1, 4(sp)
    sw 		s2, 8(sp)
    sw 		s3, 12(sp)
    sw 		s4, 16(sp)
    add 	s1, a0, x0 # s1 = addr string0
	add 	s2, a1, x0 # s2 = addr string1
	add 	s3, a2, x0 # s3 = target index a2

	# Make room for string1 inside string0
	# New length = length of str0 + str1.
	jal 	StrLenAsm # Get length of str0
	add 	s4, a0, x0 # Save length of str0 in s4
	add 	a0, s2, x0 # Get length of str1
	jal 	StrLenAsm
	add 	t1, a0, s4 # t1 = new length
	add 	t1, t1, s1 # t1 = new ending address
	add 	t0, s1, s4 # t0 = old ending address
	# Next, find the address where we stop the copy
	add 	t2, s1, s3 # t2 = stopping address = address of str0 + insert index
  # Copy the end of str0 to the end of "new string" then
  # decrement the pointers until we reach index a2 (address t2)
  StrInsertLoopTop:
  	# Copy the char
    lb 		t3, 0(t0)
    sb 		t3, 0(t1)
  	beq 	t0, t2, StrInsertCopyDone # If t0 == stopping address t2, then we're done
  	# Decrement the addresses
  	addi 	t0, t0, -1
  	addi 	t1, t1, -1
  	j 		StrInsertLoopTop
  StrInsertCopyDone:
    # Call StrNCpyAsm to do the insert, because the simple StrCpy puts in terminating zero, and we don't want that
    add 	a2, a0, x0 # a2 = a0 = length of str1 excluding the terminating zero
    add 	a0, s1, s3 # a0 = target address for StrNCpy
    add 	a1, s2, x0 # a1 = address of str1
    jal 	StrNCpyAsm
    # return
    lw 		ra, 0(sp)
    lw 		s1, 4(sp)
    lw 		s2, 8(sp)
    lw 		s3, 12(sp)
    lw 		s4, 16(sp)
    addi 	sp, sp, 20
    jalr 	ra
	