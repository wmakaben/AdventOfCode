r = [145852, 616942]
# r = [145852, 145900]
# r = [146000, 147000]
# r = [114567, 114567]


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
	lastDigit = get_digit(password, 0)
	digitCount = 1
	while i < 6:
		digit = get_digit(password, i)
		subPass = password % (10 ** (i + 1))
		n = digit * test[i - 1]
		
		if n > subPass:
			inc = n - subPass
			hasDouble = False
			i = 11
		elif digit == lastDigit:
			digitCount += 1
			if i == 5 and digitCount == 2:
				hasDouble = True
		else:
			if digitCount == 2:
				hasDouble = True
			digitCount = 1

		lastDigit = digit
		i += 1

	if hasDouble:
		print(password)
		count += 1

	password += inc

print(count)