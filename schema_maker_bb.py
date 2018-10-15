def schemaMaker(fieldName,dataType,multiValue,autoSuggest,isVariant):
	output=''
	output+='{\"fieldName\":\"'+fieldName+'\",'
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
	wrapper+=schemaMaker('categoryPath','text','f','f','f')
	wrapper+=schemaMaker('uniqueId','sku','f','f','f')
	wrapper+=schemaMaker('title','text','f','t','f')
	wrapper+=schemaMaker('brand','text','f','f','f')
	wrapper+=schemaMaker('features','text','t','f','f')
	wrapper+=schemaMaker('modelFamily','text','f','f','f')
	wrapper+=schemaMaker('modelNumber','text','f','f','f')
	wrapper+=schemaMaker('imgUrl','link','f','f','f')
	wrapper+=schemaMaker('price','decimal','f','f','f')
	wrapper=wrapper[0:-1]+']}}}'
	print wrapper


main()
