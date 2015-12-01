result = r"""result = 'result = r"\""' + result + '"\""\n' + result
print result[:144] + result[145:162] + result[163:]"""
result = 'result = r"""' + result + '"""\n' + result
print result[:144] + result[145:162] + result[163:]
