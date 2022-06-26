def is_year_leap(yr):
    if yr % 4 == 0 and yr % 100 != 0 or yr % 400 == 0:
        return True
    else:
        return False


def days_in_month(yr, mo):
    treinta=[4,6,9,11]
    treinta_uno=[1,3,5,7,8,10,12]
    febrero=[2]
    if mo in treinta:
        return 30
    elif mo in treinta_uno:
        return 31
    elif mo in febrero:
        if is_year_leap(yr)==True:
            return 29
        else:
            return 28


yr=0
mo=0

test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
	yr = test_years[i]
	mo = test_months[i]
	print(yr, mo, "->", end="")
	result = days_in_month(yr, mo)
	if result == test_results[i]:
		print("OK")
	else:
		print("Fallido")