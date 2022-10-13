# Instructions for use

1. Make sure you have cURL installed
2. Navigate to samples/
3. Run the following code:
```sh
curl --location --request POST "https://famicy.azurewebsites.net/api/item/create" --header 'Content-Type:application/json' -d @test.json
```
4. Check to see if item was listed by navigating to https://famicy.azurewebsites.net/api/item/list/{password}
> replace {password} with "azure" (without quotes)