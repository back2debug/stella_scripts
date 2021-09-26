API_KEY="YOUR API KEY"
CONTENT_HEADER="Content-Type: application/json"
API_KEY_HEADER="x-api-key: $API_KEY"
URL="ENDPOINT"
CUSTOMER_EMAIL="testing_customer@testing.com"
BRAND="keene"
CHANNEL="phone"
EMP_EMAIL="testing_employee@testing.com"
DATA="{\"customer\": {\"name\": \"Amy\",\"email\": \"$CUSTOMER_EMAIL\"},\"do_not_send\": false,\"employee\": {\"email\": \"$EMP_EMAIL\"}, \"brand\": \"$BRAND\",\"language\": \"en\", \"channel\": \"$CHANNEL\"}"


for i in 1 2 3 4 5
do
  curl -X POST --header "$CONTENT_HEADER" --header "$API_KEY_HEADER" -d "$DATA" "$URL"
  echo "Sent $i"
done