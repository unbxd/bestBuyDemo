def schemaMaker(fieldName,dataType,multiValue,autoSuggest,isVariant):
	output=''
	output+='{fieldName\":\"'+fieldName+'\",'
	output+='\"dataType\":\"'+dataType+'\",'
	if multiValue=='t':
		output+='\"multiValue\":\"true\",'
	else:
		output+='\"multiValue\":\"false\",'	
	if autoSuggest=='t':
		output+='\"autoSuggest\":\"true\",'
	else:
		output+='\"autoSuggest\":\"false\",'
	if isVariant=='t':
		output+='\"isVariant\":\"true\"}'
	else:
		output+='\"isVariant\":\"false\"},'
	return output

def main():
	wrapper='{\"feed\": {\"catalog\": {\"schema\": ['
	wrapper+=schemaMaker('uniqueId','sku','f','f','f')
	wrapper+=schemaMaker('title','text','f','t','f')
	wrapper+=wrapper[0:-1]+']}}}'
	print wrapper


main()
