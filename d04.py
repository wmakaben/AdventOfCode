r = [145852, 616942]
# r = [145852, 145900]

test = [11, 111, 1111, 11111, 111111]

def get_digit(number, n):
	return number // 10**n % 10

count = 0
password = r[0]
while password <= r[1]:
	i = 1
	hasDouble = False
	updated = False
	inc = 1
	lastDigit = -1
	while i < 6:
		digit = get_digit(password, i)
		subPass = password % (10 ** (i + 1))
		n = digit * test[i - 1]

		if n > subPass:
			inc = n - subPass
			hasDouble = False
			i = 7
		elif digit == lastDigit or (i == 1 and n == subPass):
			hasDouble = True
		lastDigit = digit
		i += 1

	if hasDouble:
		print(password)
		count += 1

	password += inc

print(count)