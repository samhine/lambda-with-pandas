import pandas

def lambda_handler(event):
	df = pandas.DataFrame(cols=["sample"])
	print(df)